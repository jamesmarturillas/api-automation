# coding utf8
import pytest
import requests
import logging
import global_data
import csv
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

logging.basicConfig(level=logging.INFO)

baseUrl = global_data.baseUrl
company_search = global_data.companysearch
company_url = baseUrl + company_search
contact_search = global_data.contactsearch
contact_url = baseUrl + contact_search

key = global_data.key
subscriptionid = global_data.subscriptionid
orgid = global_data.orgid
ContentType = global_data.ContentType
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

country = global_data.COUNTRY
product = global_data.PRODUCT1
product2 = global_data.PRODUCT2
industry = global_data.INDUSTRY
subIndustry = global_data.SUBINDUSTRY
title = global_data.TITLE
seniority = global_data.SENIORITY
seniority2 = global_data.SENIORITY2
parentDepartment = global_data.PARENTDEPARTMENT


#===============================================================================
# @pytest.mark.companycreatefile
#===============================================================================
#===============================================================================
# def test_companycreatenamewebsite500():
#     """Search HQ companies by product"""
#     param = {"product": product, "onlyHQ": "true"}
#     logging.info("Search HQ company by product %s returns 500 records" % product)
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companyname_website.csv
#     f = open('./datasource/companyname_website500.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(('Company', 'Website'))
#         for i in range(0, len(resp)):
#             writer.writerow((resp[i]["companyName"], resp[i]["websiteExactName"]))
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.companycreatefile
#===============================================================================
#===============================================================================
# def test_companycreateId500():
#     """Search HQ companies by product"""
#     param = {"product": product2, "onlyHQ": "true"}
#     logging.info("Search HQ company by product %s returns 500 records" % product2)
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companyId.csv
#     f = open('./datasource/companyId500.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['CompanyId'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["companyId"]])
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.companycreatefile
# def test_companycreateId2000():
#     """Search HQ companies by product"""
#     size = 2000
#     param = {"product": product2, "onlyHQ": "true", "resultSize": size}
#     logging.info("Search HQ company by product %s returns %s records" % (product2, size))
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companyId.csv
#     f = open('./datasource/companyId2000.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['CompanyId'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["companyId"]])
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.companycreatefile
# def test_companycreatename2000():
#     """Search HQ companies by industry"""
#     size = 2000
#     param = {"industry": industry, "onlyHQ": "true"}
#     logging.info("Search HQ company by industry %s returns %s records" % (industry, size))
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companyname.csv
#     f = open('./datasource/companyname2000.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['Company'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["companyName"]])
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.companycreatefile
# def test_companycreatename10000():
#     """Search HQ companies by industry"""
#     size = 10000
#     param = {"industry": industry, "onlyHQ": "true", "resultSize": size}
#     logging.info("Search HQ company by industry %s returns %s records" % (industry, size))
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companyname.csv
#     f = open('./datasource/companyname10000.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['Company'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["companyName"]])
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.companycreatefile
# def test_companycreatewebsite500():
#     """Search HQ companies by subIndustry"""
#     param = {"subIndustry": subIndustry, "onlyHQ": "true"}
#     logging.info("Search HQ company by subIndustry %s returns 500 records" % subIndustry)
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companywebsite.csv
#     f = open('./datasource/companywebsite500.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['Website'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["websiteExactName"]])
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.companycreatefile
# def test_companycreatewebsite5000():
#     """Search HQ companies by subIndustry"""
#     size = 5000
#     param = {"subIndustry": subIndustry, "onlyHQ": "true", "resultSize": size}
#     logging.info("Search HQ company by subIndustry %s returns %s records" % (subIndustry, size))
#     r = requests.get(company_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create companywebsite.csv
#     f = open('./datasource/companywebsite5000.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['Website'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["websiteExactName"]])
#     finally:
#         f.close()
#===============================================================================


@pytest.mark.contactcreatefile
def test_contactfullnamecompanyname500():
    """Search contacts by title"""
    param = {"title": title, "onlyHQ": "true"}
    logging.info("Search contact by title %s returns 500 records" % title)
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    # Create contactfullcompanyname.csv
    f = open('./datasource/contactfullcompanyname500.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('Full Name', 'Company Name'))
        for i in range(0, len(resp)):
            writer.writerow((resp[i]["contactExactName"], resp[i]["companyName"]))
    finally:
        f.close()


@pytest.mark.contactcreatefile
def test_contactfullnamecompanyname1000():
    """Search contacts by title"""
    size = 1000
    param = {"title": title, "onlyHQ": "true", "resultSize": size}
    logging.info("Search contact by title %s returns %s records" % (title, size))
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    # Create contactfullcompanyname.csv
    f = open('./datasource/contactfullcompanyname1000.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('Full Name', 'Company Name'))
        for i in range(0, len(resp)):
            writer.writerow((resp[i]["contactExactName"], resp[i]["companyName"]))
    finally:
        f.close()


@pytest.mark.contactcreatefile
def test_contactfullnamewebsite500():
    """Search contacts by parentDepartment"""
    param = {"parentDepartment": parentDepartment, "onlyHQ": "true"}
    logging.info("Search contact by parentDepartment %s returns 500 records" % parentDepartment)
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    #print len(resp)

    # Create contactfullnamewebsite.csv
    f = open('./datasource/contactfullnamewebsite500.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('Full Name', 'Website'))
        for i in range(0, len(resp)):
            website = resp[i]["urlExactName"].rsplit('/', 1)[-1] + '.com'
            writer.writerow((resp[i]["contactExactName"], website))
    finally:
        f.close()


@pytest.mark.contactcreatefile
def test_contactfirstlastcompanyname500():
    """Search contacts by seniority"""
    param = {"seniority": seniority, "onlyHQ": "true"}
    logging.info("Search contact by seniority %s returns 500 records" % seniority)
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    # Create contactfirstlastcompanyname.csv
    f = open('./datasource/contactfirstlastcompanyname500.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('First Name', 'Last Name', 'Company Name'))
        for i in range(0, len(resp)):
            writer.writerow((resp[i]["firstExactName"], resp[i]["lastExactName"], resp[i]["companyName"]))
    finally:
        f.close()

@pytest.mark.contactcreatefile
def test_contactfirstlastwebsite500():
    """Search contacts by product"""
    param = {"product": product, "onlyHQ": "true"}
    logging.info("Search contacts by product %s returns 500 records" % product)
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    # Create contactfirstlastwebsite.csv
    f = open('./datasource/contactfirstlastwebsite500.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('First Name', 'Last Name', 'Website'))
        for i in range(0, len(resp)):
            website = resp[i]["urlExactName"].rsplit('/', 1)[-1] + '.com'
            writer.writerow((resp[i]["firstExactName"], resp[i]["lastExactName"], website))
    finally:
        f.close()


@pytest.mark.contactcreatefile
def test_contactfirstlastwebsite2000():
    """Search contacts by product"""
    size = 2000
    param = {"product": product, "onlyHQ": "true", "resultSize": size}
    logging.info("Search contacts by product %s returns %s records" % (product, size))
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    # Create contactfirstlastwebsite.csv
    f = open('./datasource/contactfirstlastwebsite2000.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(('First Name', 'Last Name', 'Website'))
        for i in range(0, len(resp)):
            website = resp[i]["urlExactName"].rsplit('/', 1)[-1] + '.com'
            writer.writerow((resp[i]["firstExactName"], resp[i]["lastExactName"], website))
    finally:
        f.close()


@pytest.mark.contactcreatefile
def test_contactcreateId500():
    """Search contacts by seniority"""
    param = {"seniority": seniority, "onlyHQ": "true"}
    logging.info("Search contacts by seniority %s returns 500 records" % seniority)
    r = requests.get(contact_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    # Create contactId.csv
    f = open('./datasource/contactId500.csv', 'w')
    try:
        writer = csv.writer(f)
        writer.writerow(['contactId'])
        for i in range(0, len(resp)):
            writer.writerow([resp[i]["contactId"]])
    finally:
        f.close()


#===============================================================================
# @pytest.mark.contactcreatefile
# def test_contactcreateemailId500():
#     """Search contacts by product"""
#     param = {"product": product2, "onlyHQ": "true"}
#     logging.info("Search contacts by product %s returns 500 records" % product2)
#     r = requests.get(contact_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create contactcreateemailId.csv
#     f = open('./datasource/contactcreateemailId500.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['emailId'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["emailExactName"]])
#     finally:
#         f.close()
#===============================================================================


#===============================================================================
# @pytest.mark.contactcreatefile
# def test_contactcreateemailId5000():
#     """Search contacts by product"""
#     size = 5000
#     param = {"product": product2, "onlyHQ": "true", "resultSize": size}
#     logging.info("Search contacts by product %s returns %s records" % (product2, size))
#     r = requests.get(contact_url, params=param, headers=header)
#     assert r.status_code == 200
#     resp = r.json()
# 
#     # Create contactcreateemailId.csv
#     f = open('./datasource/contactcreateemailId5000.csv', 'w')
#     try:
#         writer = csv.writer(f)
#         writer.writerow(['emailId'])
#         for i in range(0, len(resp)):
#             writer.writerow([resp[i]["emailExactName"]])
#     finally:
#         f.close()
#===============================================================================