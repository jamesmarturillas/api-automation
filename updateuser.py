# coding utf8
import pytest
import requests
from random import randint
import random
import json
from bson import ObjectId
from pymongo import MongoClient
import logging
import global_data

logging.basicConfig(level=logging.INFO)

baseUrl = global_data.baseUrl
activation = global_data.activation
subscription = global_data.subscription
userurl = global_data.userurl
listurl = global_data.listurl
contact_mapping = global_data.contact_mapping
company_mapping = global_data.company_mapping
bulkuser = global_data.bulkuser

key = global_data.key
orgid = "CarSTGOrgID" # "salesforce123"
ContentType = global_data.ContentType # value = application/json
licensetype = global_data.licensetype # value = Enterprise
subscriptionid = "5890e183e4b09dff05f82d05"
adminUserId = "car.api" # "jojo.baguio@salesify.com"

recordId = randint(1000, 9999)
randomNum = randint(100, 999)

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

# new_firstName, new_lastName, new_emailId
new_firstName = 'Edward'
new_lastName = 'Smith'
new_emailId = new_firstName + '.' + new_lastName + '@' + company + '.com'

user_payload = {
  "firstName": firstName,
  "lastName": lastName,
  "licenseType": licensetype,
  "userName": emailId,
  "emailId": emailId,
  "recordId": recordId
}


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


@pytest.mark.updateuser
def test_updateall():
    """Update a user's firstName, lastName and emailId"""
    url = baseUrl + userurl + emailId
    payload = {'firstName': new_firstName, 'lastName': new_lastName, 'emailId': new_emailId}
    logging.info("Update a user's firstName to: %s, lastName to: %s and emailId to: %s" % (new_firstName, new_lastName, new_emailId))
    r = requests.put(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["userName"] == emailId and resp["lastName"] == new_lastName and resp["firstName"] == new_firstName \
           and resp["licenseType"] == licensetype and resp["subscriptionIds"][0] == subscriptionid and \
           resp["isActive"] is True and resp["source"] == "publicapi" and resp["emailId"] == new_emailId
    global user_id
    user_id = resp["id"]
    assert user_id is not None


@pytest.mark.listuser
def test_listuser():
    """Verify list of users"""
    url = baseUrl + userurl + listurl
    logging.info("List users")
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global user_ids
    user_ids = []
    if resp is None:
        pass
    else:
        user_num = len(resp)
        for k in range(0, user_num):
            assert resp[k]['subscriptionIds'][0] == subscriptionid
            if resp[k]["isActive"] is True:
                user_ids.append(resp[k]["id"])
        print (user_ids)
        assert user_id in user_ids


@pytest.mark.mongodb
def test_usedseatsincrease():
    # Connect to database contacts_stg
    client = MongoClient("10.40.11.75", 27017)
    db = client.user

    # Handle to collection
    subscription = db.subscription

    # Query matchSource
    subscription_list = subscription.find({"_id": ObjectId(subscriptionid)})
    for item in subscription_list:
        assert user_id in item["userIds"]


@pytest.mark.deleteuser
def test_deletemodifieduser():
    """Delete modified user"""
    url = baseUrl + userurl + emailId
    logging.info("Delete a user: %s" % new_emailId)
    r = requests.delete(url, headers=header)
    assert r.status_code == 200
    resp = r.text
    assert resp == 'Success'