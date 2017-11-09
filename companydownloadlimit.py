# coding utf8
import pytest
import requests
import logging
import global_data
from pymongo import MongoClient
from time import sleep

logging.basicConfig(level=logging.INFO)

downloadlimit = global_data.downloadlimit
entityType = global_data.company_entityType

baseUrl = global_data.baseUrl
subscription = global_data.subscription
company_search = global_data.companysearch

key = global_data.key
orgid = global_data.orgid
ContentType = global_data.ContentType
licensetype = global_data.licensetype
subscriptionid = global_data.subscriptionid
adminUserId = global_data.adminUserId

header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}

global download_limit


@pytest.mark.viewsubscription
def test_viewsubscriptionbefore():
    """view subscription"""
    url = baseUrl + subscription
    logging.info("view subscription")
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    download_limit = resp["downloadlimit"]
    global downloaded_count_before
    downloaded_count_before = resp["downloadedCount"]
    assert resp["id"] == subscriptionid and downloaded_count_before < download_limit
    logging.info("DownloadLimit is %s. Download count is: %s" % (download_limit, downloaded_count_before))


@pytest.mark.mongodb
def test_mongoremovecompanyId():
    # Connect to database contacts_stg
    client = MongoClient("10.40.11.75", 27017)
    db = client.user

    # Handle to collection
    downloadedCompany = db.downloadedCompany

    # Query matchSource
    downloadedCompanyId = downloadedCompany.find({"companyId": global_data.COMPANYID0}).count()
    logging.info("Count companyId returns: %d" % downloadedCompanyId)
    if downloadedCompanyId == 1:
        downloadedCompany.remove({"companyId": global_data.COMPANYID0})
        sleep(1)
    else:
        pass
    downloadedCompanyId = downloadedCompany.find({"companyId": global_data.COMPANYID0}).count()
    assert downloadedCompanyId == 0
    logging.info("In collection downloadedCompany of MongoDB reset companyId: %s, %s" % (global_data.COMPANYID0, downloadedCompanyId))

    # Query matchSource
    downloadedCompany1 = db.downloadedCompany
    downloadedCompanyId1 = downloadedCompany1.find({"companyId": global_data.COMPANYID1}).count()
    logging.info("Count companyId returns: %d" % downloadedCompanyId1)
    sleep(1)
    if downloadedCompanyId1 == 1:
        downloadedCompany.remove({"companyId": global_data.COMPANYID1})
        sleep(1)
    else:
        pass
    downloadedCompanyId1 = downloadedCompany1.find({"companyId": global_data.COMPANYID1}).count()
    assert downloadedCompanyId1 == 0
    logging.info("In collection downloadedCompany of MongoDB reset companyId: %s, %s" % (global_data.COMPANYID1, downloadedCompanyId1))

    # Query matchSource
    downloadedCompany2 = db.downloadedCompany
    sleep(1)
    # contact_Id2 = '"' + contact_Ids[2] + '"'
    # print contact_Id2
    downloadedCompanyId2 = downloadedCompany2.find({"companyId": global_data.COMPANYID2}).count()
    logging.info("Count companyId returns: %d" % downloadedCompanyId2)
    sleep(1)
    if downloadedCompanyId2 == 1:
        downloadedCompany.remove({"companyId": global_data.COMPANYID2})
        sleep(1)
    else:
        pass
    downloadedCompanyId2 = downloadedCompany2.find({"companyId": global_data.COMPANYID2}).count()
    assert downloadedCompanyId2 == 0
    logging.info("In collection downloadedCompany of MongoDB reset companyId: %s, %s" % (global_data.COMPANYID2, downloadedCompanyId2))

    # Query matchSource
    downloadedCompany3 = db.downloadedCompany
    sleep(1)
    downloadedCompanyId3 = downloadedCompany3.find({"companyId": global_data.COMPANYID3}).count()
    logging.info("Count companyId returns: %d" % downloadedCompanyId3)
    sleep(1)
    if downloadedCompanyId3 == 1:
        downloadedCompany.remove({"companyId": global_data.COMPANYID3})
        sleep(1)
    else:
        pass
    downloadedCompanyId3 = downloadedCompany3.find({"companyId": global_data.COMPANYID3}).count()
    assert downloadedCompanyId3 == 0
    logging.info("In collection downloadedCompany of MongoDB reset companyId: %s, %s" % (global_data.COMPANYID3, downloadedCompanyId3))


@pytest.mark.viewsubscription
def test_viewsubscriptionafter():
    """view subscription"""
    url = baseUrl + subscription
    logging.info("view subscription")
    sleep(1)
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    download_limit = resp["downloadlimit"]
    global downloaded_count
    downloaded_count = resp["downloadedCount"]
    assert resp["id"] == subscriptionid and downloaded_count < download_limit
    logging.info("Download count is: %s" % downloaded_count)


@pytest.mark.downloadlimit
def test_onecompanydownloadlimit():
    """Company download limit for one not used company"""
    url = baseUrl + downloadlimit
    querystring = {"entityType": entityType, "ids": global_data.COMPANYID0}
    logging.info("Company download limit for one not used company: %s" % global_data.COMPANYID0)
    sleep(1)
    r = requests.put(url, params=querystring, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'




@pytest.mark.downloadlimit
def test_onecompanydownloadlimitagain():
    """Company download limit for one used company"""
    url = baseUrl + downloadlimit
    querystring = {"entityType": entityType, "ids": global_data.COMPANYID0}
    logging.info("Company download limit for one not used company: %s" % global_data.COMPANYID0)
    sleep(1)
    r = requests.put(url, params=querystring, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'


@pytest.mark.downloadlimit
def test_multicompanydownloadlimit():
    """Company download limit for multiple not used companies"""
    url = baseUrl + downloadlimit
    multi_companyIds =  "sigCmp1904841857606976958,sigCmp1735991659806090244,sigCmp1741658610137490408" # "sigCmpfc9da0b526,sigCmp3595906298177638,sigCmpfc9da0b526"
    querystring = {"entityType": entityType, "ids": multi_companyIds}
    logging.info("Company download limit for multiple not used companies: %s" % multi_companyIds)
    sleep(1)
    r = requests.put(url, params=querystring, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'


