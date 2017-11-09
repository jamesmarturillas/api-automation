import requests
import time
import pytest
import logging
import global_data
import Utils
import json

logging.basicConfig(level=logging.INFO)

key = global_data.key
subscriptionid = global_data.subscriptionid
orgid = global_data.orgid
licensetype = global_data.licensetype
adminUserId = global_data.adminUserId
ContentType = global_data.ContentType

baseUrl = global_data.baseUrl
contact_search = global_data.contactsearch
contact_url = baseUrl + contact_search
contactdetail_url = baseUrl + global_data.contactdetailurl
upload = global_data.upload
download = global_data.download

company_search = global_data.companysearch
company_url = baseUrl + company_search
companydetail_url = baseUrl + global_data.companydetailurl

company_search2 = baseUrl + global_data.companydetailurl
contact_search2 = baseUrl + global_data.contactdetailurl

company_search = baseUrl + global_data.companysearch
com_prodmapping = company_search + global_data.product_mapping
contact_search = baseUrl + global_data.contactsearch
con_prodmapping = contact_search + global_data.product_mapping


header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}

company = "google"
country = "United States"


@pytest.mark.contactsearchtime
def test_contactsearch1():
    """Search contact details by parentDepartment"""
    contactId = global_data.CONTACTID
    param = {"contactIds": contactId}
    start = time.time()
    logging.info("Search contact details by parentDepartment: %s" % contactId)
    r = requests.get(contactdetail_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with 1 record returned: %.2f" % roundtrip)
 
 
# 6.8.2017 = both 9000 and 5000 contact search result are now not applicable as ES now have limit to max of 4000 only 
 
#===============================================================================
# @pytest.mark.contactsearchtime
# def test_contactsearch9000():
#     """Measure response time of search contacts having 9000 records returned"""
#     size = 9000
#     param = {"country": country, "resultSize": size}
#     start = time.time()
#     r = requests.get(contact_url, params=param, headers=header)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200
#     logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
#  
#  
# @pytest.mark.contactsearchtime
# def test_contactsearch5000():
#     """Measure response time of search contacts having 5000 records returned"""
#     size = 5000
#     param = {"country": country, "resultSize": size}
#     start = time.time()
#     r = requests.get(contact_url, params=param, headers=header)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200
#     logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
#===============================================================================
 
@pytest.mark.contactsearchtime
def test_contactsearch4000():
    """Measure response time of search contacts having 4000 records returned"""
    size = 4000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(contact_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.contactsearchtime
def test_contactsearch2000():
    """Measure response time of search contacts having 2000 records returned"""
    size = 2000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(contact_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.contactsearchtime
def test_contactsearch1500():
    """Measure response time of search contacts having 1500 records returned"""
    size = 1500
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(contact_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.contactsearchtime
def test_contactsearch1000():
    """Measure response time of search contacts having 1000 records returned"""
    size = 1000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(contact_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.contactsearchtime
def test_contactsearch500():
    """Measure response time of search contacts having 500 records returned"""
    size = 500
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(contact_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.contactsearchtime
def test_contactsearch100():
    """Measure response time of search contacts having 100 records returned"""
    size = 100
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(contact_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of contact search with %d records returned: %.2f" % (size, roundtrip))
 
 
#===============================================================================
# @pytest.mark.companysearch
# def test_searchcompanybyid1():
#     """Search company by companyId"""
#     #companyIds = company_ids[0]
#     companyIds = "sigCmpfc9da0b526"
#     logging.info("Search company by companyId: %s" % companyIds)
#     param = {"companyId": companyIds}
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
#     for i in range(0, len(resp)):
#         assert resp[i]["companyId"] == companyId       
#===============================================================================
        
  
@pytest.mark.companysearch
def test_searchcompanybyid1():
    """Search company by companyId"""
    #companyIds = company_ids[0]
    companyIds = "sigCmpfc9da0b526"
    logging.info("Search company by companyId: %s" % companyIds)
    param = {"companyIds": companyIds}
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["companyId"] == companyIds 
  
  
@pytest.mark.companysearchtime
def test_companysearch9000():
    """Measure response time of search company having 9000 records returned"""
    size = 9000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch4000():
    """Measure response time of search company having 4000 records returned"""
    size = 4000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch3000():
    """Measure response time of search company having 3000 records returned"""
    size = 3000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch2000():
    """Measure response time of search company having 2000 records returned"""
    size = 2000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch1500():
    """Measure response time of search company having 1500 records returned"""
    size = 1500
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch1000():
    """Measure response time of search company having 1000 records returned"""
    size = 1000
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch500():
    """Measure response time of search company having 500 records returned"""
    size = 500
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))
 
 
@pytest.mark.companysearchtime
def test_companysearch100():
    """Measure response time of search company having 100 records returned"""
    size = 100
    param = {"country": country, "resultSize": size}
    start = time.time()
    r = requests.get(company_url, params=param, headers=header)
    r.content  # wait until full content has been transfered
    roundtrip = time.time() - start
    assert r.status_code == 200
    logging.info("Response time of company search with %d records returned: %.2f" % (size, roundtrip))

@pytest.mark.companyproductsearch
def test_searchcompanyproductmapping():
    """Search company product mapping by companyId"""
    companyId = "sigCmpfc9da0b526"
    logging.info("Search company by companyId: %s" % companyId)
    param = {"companyIds": companyId}
    r = requests.get(company_search2, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global product_num
    product_num = resp[0]["numOfProducts"]
    assert resp[0]["companyId"] == companyId and len(resp) == 1
    logging.info("The number of products used by this company %s is: %d" % (resp[0]["companyName"], product_num))


@pytest.mark.contactproductsearch
def test_searchcontactproductmapping():
    """Search contact product mapping by contactId"""
    contactId = "sigCnte459ea155b"
    logging.info("Search contact by contactId: %s" % contactId)
    param = {"contactIds": contactId}
    r = requests.get(contact_search2, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global product_num2
    product_num2 = resp[0]["noOfProductsUsed"]
    assert resp[0]["contactId"] == contactId and len(resp) == 1
    logging.info("The number of products used by this contact %s is: %d" % (resp[0]["contactExactName"], product_num2))
    

#===============================================================================
# @pytest.mark.contactfile
# def test_uploadcontactfirstlastcompanyname1000():
#     """Upload contact first name, last name and company name file"""
#     url = baseUrl + upload
#     fileMapping = {"FirstName": "First Name", "LastName": "Last Name", "CompanyName": "Company Name"}
#     fields = {"fileType": "enrichcontact", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "contactfirstlastcompanyname1000.csv", open("./datasource/contactfirstlastcompanyname1000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     logging.info("Result of r: %s" % r)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_conflcn1000
#     tranid_conflcn1000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload contact file mapping by firstname, lastname and companyname with 1000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_downloadcontactfirstlastcompanyname1000():
#     """Download contact first name, last name and company name file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_conflcn1000}
#     time.sleep(1)
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download contact file mapping by firstname, lastname and companyname with 1000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_uploadcontactfirstlastwebsite2000():
#     """Upload contact first name, last name and website file"""
#     url = baseUrl + upload
#     fileMapping = {"FirstName": "First Name", "LastName": "Last Name", "Website": "Website"}
#     fields = {"fileType": "enrichcontact", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "contactfirstlastwebsite2000.csv", open("./datasource/contactfirstlastwebsite2000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_conflw2000
#     tranid_conflw2000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload contact file mapping by firstname, lastname and website with 2000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_downloadcontactfirstlastwebsite2000():
#     """Download contact first name, last name and website file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_conflw2000}
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download contact file mapping by firstname, lastname and companyname with 1000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_uploadcontactemailId5000():
#     """Upload contact emailId file"""
#     url = baseUrl + upload
#     fileMapping = {"Email": "emailId"}
#     fields = {"fileType": "enrichcontact", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "contactcreateemailId5000.csv", open("./datasource/contactcreateemailId5000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_conei5000
#     tranid_conei5000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload contact file mapping by emailId with 5000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_downloadcontactemailId5000():
#     """Download contact emailId file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_conei5000}
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download contact file mapping by emailId with 5000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_uploadcontactfullcompanyname9000():
#     """Upload contact full name and company name file"""
#     url = baseUrl + upload
#     fileMapping = {"FullName": "Full Name", "CompanyName": "Company Name"}
#     fields = {"fileType": "enrichcontact", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "contactfullcompanyname9000.csv", open("./datasource/contactfullcompanyname9000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_confcn9000
#     tranid_confcn9000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload contact file mapping by contact full name and company name with 9000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.contactfile
# def test_downloadcontactfullcompanyname9000():
#     """Download contact full name and company name file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_confcn9000}
#     time.sleep(1)
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download contact file mapping by contact full name and company name with 9000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_uploadcompanynamewebsite1000():
#     """Upload companyname_website file"""
#     url = baseUrl + upload
#     fileMapping = {"CompanyName": "Company", "Website": "Website"}
#     fields = {"fileType": "enrichcompany", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "companyname_website1000.csv", open("./datasource/companyname_website1000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_comnw1000
#     tranid_comnw1000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload company file mapping by company name and website with 1000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_downloadcompanynamewebsite1000():
#     """Download companyname_website file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_comnw1000}
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download company file mapping by company name and website with 1000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_uploadcompanyname2000():
#     """Upload companyname file"""
#     url = baseUrl + upload
#     fileMapping = {"CompanyName": "Company"}
#     fields = {"fileType": "enrichcompany", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "companyname2000.csv", open("./datasource/companyname2000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_comn2000
#     tranid_comn2000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload company file mapping by company name with 2000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_downloadcompanyname2000():
#     """Download companyname file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_comn2000}
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download company file mapping by company name with 2000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_uploadcompanywebsite5000():
#     """Upload companywebsite file"""
#     url = baseUrl + upload
#     fileMapping = {"Website": "Website"}
#     fields = {"fileType": "enrichcompany", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "companywebsite5000.csv", open("./datasource/companywebsite5000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_comw5000
#     tranid_comw5000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload company file mapping by company website with 5000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_downloadcompanywebsite5000():
#     """Download companywebsite file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_comw5000}
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download company file mapping by company website with 5000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_uploadcompanyname10000():
#     """Upload companyname file"""
#     url = baseUrl + upload
#     fileMapping = {"CompanyName": "Company"}
#     fields = {"fileType": "enrichcompany", "fileMapping": json.dumps(fileMapping)}
#     files = [("file", "companyname10000.csv", open("./datasource/companyname10000.csv").read())]
#     start = time.time()
#     r = Utils.post_multipart(url, fields, files)
#     assert r[0] == 200  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     global tranid_comn10000
#     tranid_comn10000 = r[1]["message"].split(':')[-1]
#     logging.info("Response time of upload company file mapping by company name with 10000 records: %.2f" % roundtrip)
#  
#  
# @pytest.mark.companyfile
# def test_downloadcompanyname10000():
#     """Download companyname file"""
#     url = baseUrl + download
#     params = {"transactionId": tranid_comn10000}
#     time.sleep(1)
#     start = time.time()
#     r = requests.get(url, params=params, headers=header, stream=True)
#     r.content  # wait until full content has been transfered
#     roundtrip = time.time() - start
#     assert r.status_code == 200 and r.raw is not None
#     logging.info("Response time of download company file mapping by company name with 10000 records: %.2f" % roundtrip)
#  
#===============================================================================
