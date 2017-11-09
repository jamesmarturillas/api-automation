# coding utf8
import pytest
import requests
import logging
import global_data

logging.basicConfig(level=logging.INFO)

baseUrl = global_data.baseUrl
company_search = baseUrl + global_data.companysearch
com_prodmapping = company_search + global_data.product_mapping
contact_search = baseUrl + global_data.contactsearch
con_prodmapping = contact_search + global_data.product_mapping


key = global_data.key
subscriptionid = global_data.subscriptionid
ContentType = global_data.ContentType
orgid = global_data.orgid
licensetype = global_data.licensetype
adminUserId = global_data.adminUserId

header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}


# Read companyId from file
# with open('./datasource/companyId18.csv', 'r') as f:
#     lines = f.readlines()[1:]
# companyId = random.choice(lines).rstrip()
#
#
# # Read contactId from file
# with open('./datasource/contactId18.csv', 'r') as f:
#     lines = f.readlines()[1:]
# contactId = random.choice(lines).rstrip()

companyId = global_data.COMPANYID
contactId = global_data.CONTACTID

 
@pytest.mark.companyproductsearch
def test_searchcompanybyid():
    """Search company by companyId"""
    logging.info("Search company by companyId: %s" % companyId)
    param = {"companyId": companyId}
    r = requests.get(company_search, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global product_num
    product_num = resp[0]["numOfProducts"]
    assert resp[0]["companyId"] == companyId and len(resp) == 1
    logging.info("The number of products used by this company %s is: %d" % (resp[0]["companyName"], product_num))
  
  
@pytest.mark.contactproductsearch
def test_searchcontactbyid():
    """Search contact by contactId"""
    logging.info("Search contact by contactId: %s" % contactId)
    param = {"contactId": contactId}
    r = requests.get(contact_search, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()   
    global product_num2
    product_num2 = resp[0]["noOfProductsUsed"]
    assert resp[0]["contactId"] == contactId and len(resp) == 1
    logging.info("The number of products used by this contact %s is: %d" % (resp[0]["contactExactName"], product_num2))   
    

    
    