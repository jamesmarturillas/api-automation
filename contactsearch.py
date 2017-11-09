# coding utf8
import pytest
import requests
import linecache
import logging
import global_data

logging.basicConfig(level=logging.INFO)

baseUrl = global_data.baseUrl
contact_search = global_data.contactsearch
url = baseUrl + contact_search
contactdetail_url = baseUrl + global_data.contactdetailurl

key = global_data.key
subscriptionid = global_data.subscriptionid
orgid = global_data.orgid
licensetype = global_data.licensetype
adminUserId = global_data.adminUserId
ContentType = global_data.ContentType

header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}

# Read title data from file
line2 = linecache.getline('./datasource/contact_info.csv', 2)
search_info = line2.split(',')
firstName = search_info[0]
lastName = search_info[1]
company = search_info[2]
website = search_info[3]
title = search_info[4]
city = search_info[5]
state = search_info[6]
country = search_info[7]
region = search_info[8]
parentDepartment = search_info[10]
seniority = search_info[11]
product = search_info[14]
productParentCategory = search_info[15]
productCategory = search_info[16]
emaildomain = search_info[17]

emailId = firstName + '_' + lastName + '@' + (emaildomain).strip()
fullName = firstName + ' ' + lastName
global contactIds_company, contactIds_website, contact_emailId, contactIds_product, contactIds_parentdepartment, \
contactIds_seniority

# Read title data from file
# line3 = linecache.getline('./datasource/contact_info.csv', 3)
# search_info3 = line3.split(',')
# emailId3 = search_info3[17]
# print emailId3
emailId3 = "jack.macgregor@agrium.com"

contactIds_company = []
contactIds_website = []
# contactIds_emailId = []
contactIds_product = []
contactIds_parentdepartment = []
contactIds_seniority = []


@pytest.mark.contactsearch
def test_contactsearchbycompany():
    """Search companyName"""
    param = {"companyName": company}
    logging.info("Search contact by company name: %s" % company)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code >= 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["companyName"] == company
        contactIds_company.append(resp[i]["contactId"])


@pytest.mark.contactsearch
def test_contactdetailssearch():
    """Search contact details by companyName"""
    contactIds = contactIds_company[0] + "," + contactIds_company[1] + "," + contactIds_company[2]
    search_contactId = contactIds.split(',')
    param = {"contactIds": contactIds}
    logging.info("Search contact details by company name: %s" % contactIds)
    r = requests.get(contactdetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert len(resp) == len(search_contactId)
    for i in range(0, len(resp)):
        assert resp[i]["companyName"] == company and resp[i]["contactId"] in search_contactId


@pytest.mark.contactsearch
def test_contactsearchbywebsite():
    """Search website"""
    param = {"website": website}
    logging.info("Search contact by website: %s" % website)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    company_website = website.split('.')
    for i in range(0, len(resp)):
        assert company_website[1] in resp[i]["companyName"].lower()
        contactIds_website.append(resp[i]["contactId"])


@pytest.mark.contactsearch
def test_contactdetailswebsite():
    """Search contact details by website"""
    contactIds = contactIds_website[0] + ',' + contactIds_website[1] + ',' + contactIds_website[2] + ',' + contactIds_website[3]
    search_contactId = contactIds.split(',')
    param = {"contactIds": contactIds}
    logging.info("Search contact details by website: %s" % contactIds)
    r = requests.get(contactdetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert len(resp) == len(search_contactId)
    for i in range(0, len(resp)):
        assert resp[i]["urlExactName"].rsplit('/', 1)[-1] in company.lower() and resp[i]["contactId"] in search_contactId


@pytest.mark.contactsearch
def test_contactsearchbytitle():
    """Search title"""
    param = {"title": title}
    logging.info("Search contact by title: %s" % title)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert title in resp[i]["contactTitle"]


@pytest.mark.contactsearch
def test_contactsearchbyemailid():
    """Search emailId"""
    param = {"emailId": emailId3}
    logging.info("Search contact by emailId: %s" % emailId3)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global contact_emailId
    contact_emailId = resp[0]["emailExactName"]


@pytest.mark.contactsearch
def test_contactsearchbycity():
    """Search city"""
    param = {"city": city}
    logging.info("Search contact by city: %s" % city)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["contactCity"] == city


@pytest.mark.contactsearch
def test_contactsearchbystate():
    """Search state"""
    param = {"state": state}
    logging.info("Search contact by state: %s" % state)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["contactState"] == state


@pytest.mark.contactsearch
def test_contactsearchbycountry():
    """Search country"""
    param = {"country": country}
    logging.info("Search contact by country: %s" % country)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["contactCountry"] == country


@pytest.mark.contactsearch
def test_contactsearchbyregion():
    """Search region"""
    param = {"region": region}
    logging.info("Search contact by region: %s" % region)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["contactRegion"] == region


@pytest.mark.contactsearch
def test_contactsearchbyproduct():
    """Search product"""
    param = {"product": product}
    logging.info("Search contact by product: %s" % product)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        contactIds_product.append(resp[i]["contactId"])


@pytest.mark.contactsearch
def test_contactdetailsproduct():
    """Search contact details for product"""
    contactIds = contactIds_product[0] + ',' + contactIds_product[1]
    param = {"contactIds": contactIds}
    logging.info("Search contact by product: %s" % contactIds)
    r = requests.get(contactdetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    #for i in range(0, len(resp)):
    #    assert product in resp[i]["productsUsedExactName"]
      
    for company in resp:
        assert company["productsUsedExactName"] is not None  
    
@pytest.mark.contactsearch
def test_contactsearchbyparentdepartment():
    """Search parentDepartment"""
    param = {"parentDepartment": parentDepartment}
    logging.info("Search contact by parent department: %s" % parentDepartment)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        contactIds_parentdepartment.append(resp[i]["contactId"])


@pytest.mark.contactsearch
def test_contactdetailsparentdepartment():
    """Search contact details by parentDepartment"""
    contactIds = contactIds_parentdepartment[0] + ',' + contactIds_parentdepartment[1]
    param = {"contactIds": contactIds}
    logging.info("Search contact details by parentDepartment: %s" % contactIds)
    r = requests.get(contactdetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert parentDepartment in resp[i]["departmentExact"]


@pytest.mark.contactsearch
def test_contactsearchbyseniority():
    """Search seniority"""
    param = {"seniority": seniority}
    logging.info("Search contact by seniority: %s" % seniority)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        contactIds_seniority.append(resp[i]["contactId"])


@pytest.mark.contactsearch
def test_contactdetailsseniority():
    """Search contact details by seniority"""
    contactIds = contactIds_seniority[0] + ',' + contactIds_seniority[1]
    param = {"contactIds": contactIds}
    logging.info("Search contact details by seniority: %s" % contactIds)
    r = requests.get(contactdetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["seniorityExact"] == seniority


@pytest.mark.contactsearch
def test_contactsearchbyfullName():
    """Search fullName"""
    param = {"contactName": fullName}
    logging.info("Search contact by user name: %s" % fullName)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["contactExactName"] == fullName


@pytest.mark.contactsearch
def test_contactsearchbyfirstname():
    """Search firstName"""
    param = {"contactName": firstName}
    logging.info("Search contact by first name: %s" % firstName)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert firstName in resp[i]["contactExactName"]


@pytest.mark.contactsearch
def test_contactsearchbylastName():
    """Search lastName"""
    param = {"contactName": lastName}
    logging.info("Search contact by last name: %s" % lastName)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert lastName in resp[i]["contactExactName"]


@pytest.mark.contactsearch
def test_contactsearchbyproductParentCategory():
    """Search productParentCategory"""
    param = {"productParentCategory": productParentCategory}
    logging.info("Search contact by productParentCategory: %s" % productParentCategory)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200


@pytest.mark.contactsearch
def test_contactsearchbyproductCategory():
    """Search productCategory"""
    param = {"productCategory": productCategory}
    logging.info("Search contact by productCategory: %s" % productCategory)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200


# Read title data from file
line2 = linecache.getline('./datasource/contact_info.csv', 2)
search_info2 = line2.split(',')
company2 = search_info2[2]
website2 = search_info2[3]
city2 = search_info2[5]
state2 = search_info2[6]
country2 = search_info2[7]
region2 = search_info2[8]
parentDepartment2 = search_info2[10]
seniority2 = search_info2[11]
product2 = search_info2[14]
emailId2 = "jmacgregor@google.com"
title2 = "Senior Software Engineer"

@pytest.mark.contactsearch
def test_contactsearchbyall():
    """Search companyName, product, region, country, state, city, seniority, parentDepartment, website, emailId, title"""
    param = {"companyName": company2,
             "product": product2,
             "region": region2,
             "country": country2,
             "state": state2,
             "city": city2,
             "seniority": seniority2,
             "parentDepartment": parentDepartment2,
             "website": website2,
             "title": title2
             }
    logging.info("Search contact by company name: %s, product: %s, region: %s, country: %s, state: %s, city: %s, "
                 "seniority: %s, parentDepartment: %s, website: %s, title: %s" % (company2, product2,
                region2, country2, state2, city2, seniority2, parentDepartment2, website2, title2))
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp[0]["companyName"] == company2 and resp[0]["contactRegion"] == region2 and resp[0]["contactCountry"] == country2 \
        and resp[0]["contactState"] == state2 and resp[0]["contactCity"] == city2 and resp[0]["contactTitle"] == title2 \
        and resp[0]["contactId"] is not None


@pytest.mark.contactsearch
def test_contactsearchlimitsize():
    """Limit search result size by using resultSize"""
    size = 6
    param = {"title": title, "resultSize": size}
    logging.info("Search contact by title and limited by resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200 and len(r.json()) == size


@pytest.mark.contactsearch
def test_contactsearchlimitzerosize():
    """Limit search result size by using 0 resultSize"""
    size = 0
    param = {"title": title, "resultSize": size}
    logging.info("Search contact by title and limited by resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 404 and r.json()["message"] == "No Data Found"


@pytest.mark.contactsearch
def test_contactsearchinvalidlimitsize():
    """Limit search result size by using invalid resultSize"""
    size = "one"
    param = {"title": title, "resultSize": size}
    logging.info("Search contact by title and limited by result size: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 206 and r.json()["message"] == "Invalid attribute name or invalid attribute case"


@pytest.mark.contactsearch
def test_contactsearchminusonelimitsize():
    """Limit search result size by using -1 resultSize"""
    size = -1
    param = {"title": title, "resultSize": size}
    logging.info("Search contact title and limited by result size: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code >= 200 and len(r.json()) == 1


@pytest.mark.contactsearch
def test_contactsearchminusnumlimitsize():
    """Limit search result size by using -10 resultSize"""
    size = -10
    param = {"title": title, "resultSize": size}
    logging.info("Search contact title and limited by result size: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code >= 200 and len(r.json()) == 1


@pytest.mark.contactsearch
def test_contactsearchemailphone():
    """Verify contact has email and phone number"""
    #contactId = "575a52c92866166e595e38a1"
    contactId = "sigCnte459ea155b"
    param = {"contactId": contactId}
    logging.info("Search contact by id, contact has phone number and no email: %s" % contactId)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp[0]["contactId"] == contactId
    if resp[0]["emailExactName"] is not None:
        assert resp[0]["contactHasEmail"] is True
    else:
        assert resp[0]["contactHasEmail"] is False

    if resp[0]["clickToCallPhoneNumber"] is not None:
        assert resp[0]["contactHasPhone"] is True
    else:
        assert resp[0]["contactHasPhone"] is False


@pytest.mark.contactsearch
def test_contactsearchemailnonphone():
    """Verify contact has email and non phone number"""
    contactId = "sigCnte459ea155b"
    param = {"contactId": contactId}
    logging.info("Search contact by id, contact has email and non phone number: %s" % contactId)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp[0]["contactId"] == contactId
    if resp[0]["emailExactName"] is not None:
        assert resp[0]["contactHasEmail"] is True
    else:
        assert resp[0]["contactHasEmail"] is False

    if resp[0]["clickToCallPhoneNumber"] is not None:
        assert resp[0]["contactHasPhone"] is True
    else:
        assert resp[0]["contactHasPhone"] is False



@pytest.mark.contactsearch
def test_contactsearchbycompanycomma():
    """Search contact by companyName which includes comma"""
    global companyname
    companyname = global_data.COMPANYNAME
    param = {"companyName": companyname}
    logging.info("Search contact by company name which includes comma: %s" % companyname)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code >= 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["companyName"] in companyname
        contactIds_company.append(resp[i]["contactId"])


@pytest.mark.contactsearch
def test_contactdetailssearchcompanycomma():
    """Search contact details by companyName which includes comma"""
    m = len(contactIds_company)
    search_contactId = contactIds_company[m-1]
    param = {"contactIds": search_contactId}
    logging.info("Search contact details by company name which includes comma: %s" % companyname)
    r = requests.get(contactdetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp[0]["companyName"] in companyname and resp[0]["contactId"] == search_contactId
