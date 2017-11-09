# coding utf8
import pytest
import requests
from random import randint
import random
import json
import string
import logging
import global_data

logging.basicConfig(level=logging.INFO)

baseUrl = global_data.baseUrl
# baseUrl = "http://192.168.20.75:8080/rest/"
activation = global_data.activation
subscription = global_data.subscription
userurl = global_data.userurl
listurl = global_data.listurl
contact_mapping = global_data.contact_mapping
company_mapping = global_data.company_mapping
bulkuser = global_data.bulkuser

key = global_data.key
orgid = global_data.orgid
ContentType = global_data.ContentType
licensetype = global_data.licensetype
subscriptionid = global_data.subscriptionid
adminUserId = global_data.adminUserId

recordId = randint(1000, 9999)
randomNum = randint(100, 999)

# numbers of bulk users
n = 3

activation_header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'Content-Type': ContentType
}

header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}

# Read user info data from file
with open('./datasource/user_info.csv', 'r') as f:
    lines = f.readlines()[1:]

line = random.choice(lines).rstrip()
userinfo = line.split(',')
firstName = userinfo[0]
lastName = userinfo[1]
company = userinfo[2]
userName = firstName + '.' + lastName + str(randomNum)
emailId = userName + '@' + company + '.com'

activation_payload = {
  "firstName": firstName,
  "lastName": lastName,
  "licenseType": licensetype,
  "userName": emailId,
  "emailId": emailId,
  "recordId": recordId
}

user_payload = activation_payload

bulkUser_payload = []
bulkUserNames = []
for i in range(0, n):
    userFirstName = firstName + random.choice(string.ascii_letters)
    userLastName = lastName + random.choice(string.ascii_letters)
    eachUserName = userFirstName + '.' + userLastName + str(i)
    eachEmailId = eachUserName + '@' + company + '.com'
    bulkUserNames.append(eachEmailId)
    recordId = randint(1000, 9999)
    eachUser_payload = {
        "firstName": userFirstName,
        "lastName": userLastName,
        "licenseType": licensetype,
        "userName": eachEmailId,
        "emailId": eachEmailId,
        "recordId": recordId
    }
    bulkUser_payload.append(eachUser_payload)

contact_attributes = {
  "name": None,
  "firstName": None,
  "lastName": None,
  "title": None,
  "seniority": None,
  "url": None,
  "email": None,
  "companyPhoneList": None,
  "company": None,
  "empRange": None,
  "revenueRange": None,
  "parentIndustry": None,
  "industry": None,
  "roleMap": None,
  "productMap": "",
  "numberOfProducts": 0,
  "location": None,
  "id": None,
  "city": "",
  "department": None,
  "productsCount": 0,
  "address": "",
  "state": "",
  "country": "",
  "region": ""
}

sorted_contact_attributes = sorted(contact_attributes.keys())

company_attributes = {
  "masterCompanyName": None,
  "parentIndustry": None,
  "industry": None,
  "companyDesc": None,
  "companyCategory": None,
  "companyType": None,
  "empRange": None,
  "revenueRange": None,
  "location": None,
  "companyPhoneList": None,
  "website": None,
  "url": None,
  "sicCode": None,
  "naicsCode": None,
  "companyProductMap": "",
  "id": None,
  "city": "",
  "productsCount": 0,
  "address": "",
  "state": "",
  "country": "",
  "region": ""
}

sorted_company_attributes = sorted(company_attributes.keys())

# new_firstName, new_lastName, new_emailId
new_firstName = 'Edward'
new_lastName = 'Smith'
new_emailId = new_firstName + '.' + new_lastName + '@' + company + '.com'

# first_name, last_name, email_id
first_name = 'Tina'
last_name = 'Virgina'
user_name = first_name + ' ' + last_name
email_id = first_name + '-' + last_name + '@' + company + '.com'

# @pytest.mark.subscription #####
# def test_activatesubscription():
#     url = baseUrl + activation
#     headers = activation_header
#     payload = activation_payload
#     r = requests.post(url, data=json.dumps(payload), headers=headers)
#     assert r.status_code == 200
#     resp = r.text
#     assert resp == 'Success'

@pytest.mark.subscription
def test_viewsubscription():
    url = baseUrl + subscription
    logging.info("View Subscription Info: %s" % subscriptionid)
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["id"] == subscriptionid


@pytest.mark.createuser
def test_createuser():
    """Create a single user"""
    url = baseUrl + userurl
    payload = user_payload
    logging.info("Create a user: %s" % payload)
    r = requests.post(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 201
    resp = r.text
    assert resp == 'Success'


@pytest.mark.retrieveuser
def test_retrieveuser1():
    """Retrieve a single user's info"""
    url = baseUrl + userurl + emailId
    logging.info("View Created User Info: %s" % emailId)
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["userName"] == emailId and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] \
        == subscriptionid and resp["isActive"] is True and resp["source"] == "publicapi"


@pytest.mark.createuser
def test_createuserduplicate():
    """Verify create a single duplicate user"""
    url = baseUrl + userurl
    payload = user_payload
    logging.info("Try to create an existing user: %s" % payload)
    r = requests.post(url, data=json.dumps(payload), headers=header)
    assert r.status_code >= 400
    resp = r.json()
    #[Jojo 3.29] assert resp["message"].strip() == 'User already exists with this username'
    assert resp["message"].strip() == 'User already exist!'

@pytest.mark.updateuser
def test_firstname():
    """Update a user's firstName"""
    url = baseUrl + userurl
    new_name = 'Boom';
    payload = {
        'firstName': new_name,
        'lastName': 'Hammond',
        'licenseType': 'Enterprise',
        'userName': 'Ann.Hammond761@pieology.com',
        'emailId': 'Ann.Hammond761@pieology.com',
        'recordId': 3105}
    logging.info("Update a user's firstName to: %s" % new_firstName)
    r = requests.put(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    print(resp)
    assert resp["userName"] == emailId and resp["lastName"] == lastName and resp["firstName"] == new_name \
        and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] == subscriptionid and \
        resp["isActive"] is True and resp["emailId"] == emailId

@pytest.mark.updateuser
def test_lastname():
    """Update a user's lastName"""
    url = baseUrl + userurl
    payload = {'lastName': new_lastName}
    logging.info("Update a user's lastName to: %s" % new_lastName)
    r = requests.put(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["userName"] == emailId and resp["lastName"] == new_lastName and resp["firstName"] == new_firstName \
        and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] == subscriptionid and \
        resp["isActive"] is True and resp["source"] == "publicapi" and resp["emailId"] == emailId


@pytest.mark.updateuser
def test_emailId():
    """Update a user's emailId"""
    url = baseUrl + userurl
    update_email = new_lastName + '.' + new_firstName + '@' + company + '.com'
    payload = {'emailId': update_email}
    logging.info("Update a user's emailId to: %s" % update_email)
    r = requests.put(url, data=json.dumps(payload), headers=header)
    assert r.status_code >= 200
    resp = r.json()
    assert resp["userName"] == emailId and resp["lastName"] == new_lastName and resp["firstName"] == new_firstName \
        and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] == subscriptionid and \
        resp["isActive"] is True and resp["source"] == "publicapi" and resp["emailId"] == update_email


@pytest.mark.updateuser
def test_updateall():
    """Update a user's firstName, lastName and emailId"""
    url = baseUrl + userurl
    payload = {'firstName': firstName, 'lastName': lastName, 'emailId': emailId}
    logging.info("Update a user's firstName to: %s, lastName to: %s and emailId to: %s" % (firstName, lastName, emailId))
    r = requests.put(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["userName"] == emailId and resp["lastName"] == lastName and resp["firstName"] == firstName \
           and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] == subscriptionid and \
           resp["isActive"] is True and resp["source"] == "publicapi" and resp["emailId"] == emailId


@pytest.mark.deleteuser
def test_deleteuser():
    """Delete a single user"""
    url = baseUrl + userurl + emailId
    logging.info("Delete a user: %s" % emailId)
    r = requests.delete(url, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'


@pytest.mark.deleteuser
def test_deleteusernonexist():
    """Delete a single non-existing user"""
    url = baseUrl + userurl + emailId
    logging.info("Try to delete a non-existing user: %s" % emailId)
    r = requests.delete(url, headers=header)
    assert r.status_code == 404
    resp = r.json()
    assert resp["message"].strip() == 'User not found'


@pytest.mark.retrieveuser
def test_verifydeleteduser():
    """Verify the deleted user not found"""
    url = baseUrl + userurl + emailId
    logging.info("Try to view a non-existing user: %s" % emailId)
    r = requests.get(url, headers=header)
    assert r.status_code == 404
    resp = r.json()
    assert "not found" in resp["message"]


@pytest.mark.bulkuser
def test_createbulkuser():
    """Create bulk users"""
    url = baseUrl + bulkuser
    payload = bulkUser_payload
    logging.info("Bulk create users")
    r = requests.post(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 201
    resp = r.json()
    for j in range(0, len(resp)):
        assert resp[j]["userName"] in bulkUserNames and resp[j]["message"] == 'Success'


@pytest.mark.subscription
def test_viewsubscription():
    """View subscription"""
    url = baseUrl + subscription
    logging.info("View Subscription: %s" % subscriptionid)
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["id"] == subscriptionid


@pytest.mark.listuser
def test_listuser():
    """Verify list of users"""
    url = baseUrl + userurl + listurl
    logging.info("List users")
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    if resp is None:
        pass
    else:
        user_num = len(resp)
        for k in range(0, user_num):
            assert resp[k]['subscriptionIds'][0] == subscriptionid


@pytest.mark.bulkuser
def test_deletebulkuser():
    """Delete bulk users"""
    url = baseUrl + bulkuser
    payload = {"usernames": bulkUserNames}
    logging.info("Bulk delete users: %s" % bulkUserNames)
    r = requests.delete(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    for j in range(0, len(resp)):
        assert resp[j]["userName"] in bulkUserNames and resp[j]["message"] == 'Success'


@pytest.mark.bulkusernegative
def test_deletebulkusernonexisting():
    """Delete bulk non-existing users"""
    url = baseUrl + bulkuser
    payload = {"usernames": bulkUserNames}
    logging.info("Try to delete non-existing bulk users: %s" % bulkUserNames)
    r = requests.delete(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    for j in range(0, len(resp)):
        assert resp[j]["userName"] in bulkUserNames and resp[j]["message"].strip() == 'User not found'


@pytest.mark.createuser
def test_createuser3():
    """Create a user for partial create bulk users test cases"""
    url = baseUrl + userurl
    payload = {
        "firstName": first_name,
        "lastName": last_name,
        "licenseType": licensetype,
        "userName": user_name,
        "emailId": email_id,
        "recordId": recordId
    }
    logging.info("Create a user")
    r = requests.post(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 201
    resp = r.text
    assert resp == 'Success'


@pytest.mark.retrieveuser
def test_retrieveuser2():
    """Verify the newly created user"""
    url = baseUrl + userurl + user_name
    logging.info("View created user: %s" % user_name)
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["userName"] == user_name and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] \
        == subscriptionid and resp["isActive"] is True and resp["source"] == "publicapi"

@pytest.mark.deleteuser
def test_deleteoneuser():
    """Delete a user for partial delete bulk users test cases"""
    url = baseUrl + userurl + user_name
    logging.info("Delete the newly created user: %s" % user_name)
    r = requests.delete(url, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'


