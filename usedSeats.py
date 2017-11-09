# coding utf8
import pytest
import requests
from random import randint
import random
import json
import string
import logging
from bson import ObjectId
from pymongo import MongoClient
import global_data

logging.basicConfig(level=logging.INFO)

"""
1. Search subscriptionid db.getCollection('subscription').find({"_id" : ObjectId("586e997fe4b0a8d2912fd8b7")})
2. Add orgid to subscription collection
3. Find a admin user db.getCollection('user').find({"emailId" : "thais.li@salesify.com"})
4. Add subscriptionid to above user
5. Create a new user having above subscriptonid
6. Verify userIds increase
7. Delete the user
8. Verify userIds decrease
9. Create users more than seats
"""


baseUrl = global_data.baseUrl
# baseUrl = "http://192.168.20.75:8080/rest/"
activation = global_data.activation
subscription = global_data.subscription
userurl = global_data.userurl
listurl = global_data.listurl
contact_mapping = global_data.contact_mapping
company_mapping = global_data.company_mapping
bulkuser = global_data.bulkuser

key = "RU6j8qgmGf9ROIGthDN7W7WdifevcsDZ4aaIZhvU"
subscriptionid = "5890e183e4b09dff05f82d05"
orgid = "salesforce123"
ContentType = "application/json"
licensetype = "Enterprise"
adminUserId = "jojo.baguio@salesify.com"

recordId = randint(1000, 9999)
randomNum = randint(100, 999)

# numbers of bulk users
n = 7

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

# first_name, last_name, email_id
first_name = 'Ted'
last_name = 'Warner'
user_name = first_name + ' ' + last_name
email_id = first_name + '-' + last_name + '@' + company + '.com'

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


@pytest.mark.mongodb
def test_mongoinitialseats():
    # Connect to database contacts_stg
    client = MongoClient("10.40.11.75", 27017)
    db = client.user

    # Handle to collection
    subscription = db.subscription

    # Query matchSource
    subscription_list = subscription.find({"_id": ObjectId(subscriptionid)})
    for item in subscription_list:
        global initalSeats_mongo
        initalSeats_mongo = len(item["userIds"])
        global seats_mongo
        seats_mongo = item["seats"]
        logging.info("In MongoDB this subscription has %s Seats and %s userIds" % (seats_mongo, initalSeats_mongo))


@pytest.mark.subscription
def test_initialseats():
    """View subscription"""
    url = baseUrl + subscription
    logging.info("View Subscription: %s" % subscriptionid)
    r = requests.get(url, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp["id"] == subscriptionid
    global seats
    seats = resp["seats"]
    global usedSeats_start
    usedSeats_start = resp["seatsUsed"]
    assert seats is not None
    logging.info("This subscription has %s Seats and %s UsedSeats" % (seats, usedSeats_start))

@pytest.mark.bulkuser
def test_createbulkuser():
    """Create bulk users"""
    url = baseUrl + bulkuser
    payload = bulkUser_payload
    r = requests.post(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 201
    resp = r.json()
    for j in range(0, len(resp)):
        assert resp[j]["userName"] in bulkUserNames and resp[j]["message"] == 'Success'
    logging.info("Bulk create users successfully")


@pytest.mark.bulkuser
def test_deletebulkuser():
    """Delete bulk users"""
    url = baseUrl + bulkuser
    payload = {"usernames": bulkUserNames}
    r = requests.delete(url, data=json.dumps(payload), headers=header)
    assert r.status_code == 200
    resp = r.json()
    for j in range(0, len(resp)):
        assert resp[j]["userName"] in bulkUserNames and resp[j]["message"] == 'Success'
    logging.info("Bulk delete users successfully")

