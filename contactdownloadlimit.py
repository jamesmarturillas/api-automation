# coding utf8
import pytest
import requests
import logging
import global_data
from pymongo import MongoClient
from time import sleep

logging.basicConfig(level=logging.INFO)

downloadlimit = global_data.downloadlimit
entityType = global_data.contact_entityType

baseUrl = global_data.baseUrl
subscription = global_data.subscription
contact_search = global_data.contactsearch

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
def test_mongoremovecontactid():
    # Connect to database contacts_stg
    client = MongoClient("10.40.11.75", 27017)
    db = client.user

    # Handle to collection
    downloadedContact = db.downloadedContact

    # Query matchSource
    downloadedContactId = downloadedContact.find({"contactId": global_data.CONTACTID0}).count()
    logging.info("Count contactId returns: %d" % downloadedContactId)
    if downloadedContactId == 1:
        downloadedContact.remove({"contactId": global_data.CONTACTID0})
        sleep(1)
    else:
        pass
    downloadedContactId = downloadedContact.find({"contactId": global_data.CONTACTID0}).count()
    assert downloadedContactId == 0
    logging.info("In collection downloadedContact of MongoDB reset contactId: %s, %s" % (global_data.CONTACTID0, downloadedContactId))

    # Query matchSource
    downloadedContact1 = db.downloadedContact
    downloadedContactId1 = downloadedContact1.find({"contactId": global_data.CONTACTID1}).count()
    logging.info("Count contactId returns: %d" % downloadedContactId1)
    sleep(1)
    if downloadedContactId1 == 1:
        downloadedContact.remove({"contactId": global_data.CONTACTID1})
        sleep(1)
    else:
        pass
    downloadedContactId1 = downloadedContact1.find({"contactId": global_data.CONTACTID1}).count()
    assert downloadedContactId1 == 0
    logging.info("In collection downloadedContact of MongoDB reset contactId: %s, %s" % (global_data.CONTACTID1, downloadedContactId1))

    # Query matchSource
    downloadedContact2 = db.downloadedContact
    sleep(1)
    # contact_Id2 = '"' + contact_Ids[2] + '"'
    # print contact_Id2
    downloadedContactId2 = downloadedContact2.find({"contactId": global_data.CONTACTID2}).count()
    logging.info("Count contactId returns: %d" % downloadedContactId2)
    sleep(1)
    if downloadedContactId2 == 1:
        downloadedContact.remove({"contactId": global_data.CONTACTID2})
        sleep(1)
    else:
        pass
    downloadedContactId2 = downloadedContact2.find({"contactId": global_data.CONTACTID2}).count()
    assert downloadedContactId2 == 0
    logging.info("In collection downloadedContact of MongoDB reset contactId: %s, %s" % (global_data.CONTACTID2, downloadedContactId2))

    # Query matchSource
    downloadedContact3 = db.downloadedContact
    sleep(1)
    downloadedContactId3 = downloadedContact3.find({"contactId": global_data.CONTACTID3}).count()
    logging.info("Count contactId returns: %d" % downloadedContactId3)
    sleep(1)
    if downloadedContactId3 == 1:
        downloadedContact.remove({"contactId": global_data.CONTACTID3})
        sleep(1)
    else:
        pass
    downloadedContactId3 = downloadedContact3.find({"contactId": global_data.CONTACTID3}).count()
    assert downloadedContactId3 == 0
    logging.info("In collection downloadedContact of MongoDB reset contactId: %s, %s" % (global_data.CONTACTID3, downloadedContactId3))


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
def test_onecontactdownloadlimit():
    """Contact download limit for one not used contact"""
    url = baseUrl + downloadlimit
    # contactId = '"' + contact_Ids[0] + '"'
    querystring = {"entityType": entityType, "ids": global_data.CONTACTID0}
    logging.info("Contact download limit for one not used contact: %s" % global_data.CONTACTID0)
    sleep(1)
    r = requests.put(url, params=querystring, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'



@pytest.mark.downloadlimit
def test_onecontactdownloadlimitagain():
    """Contact download limit for one used contact"""
    url = baseUrl + downloadlimit
    # contactId = '"' + contact_Ids[0] + '"'
    querystring = {"entityType": entityType, "ids": global_data.CONTACTID0}
    logging.info("Contact download limit for one not used contact: %s" % global_data.CONTACTID0)
    sleep(1)
    r = requests.put(url, params=querystring, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'

@pytest.mark.downloadlimit
def test_multicontactdownloadlimit():
    """Contact download limit for multiple not used contacts"""
    url = baseUrl + downloadlimit
    multi_contactIds = "583a548d97efa5ed6e05d5ed,575a98872866166e593ae3f9,575a87e12866166e59596e74"
    querystring = {"entityType": entityType, "ids": multi_contactIds}
    logging.info("Contact download limit for multiple not used contacts: %s" % multi_contactIds)
    sleep(1)
    r = requests.put(url, params=querystring, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'




