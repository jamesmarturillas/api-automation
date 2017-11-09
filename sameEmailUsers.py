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

header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}


bulkUser_payload = []
bulkUserNames = []
for i in range(0, 1):
    userFirstName = 'Stephen' + random.choice(string.ascii_letters)
    userLastName = 'Wilson' + random.choice(string.ascii_letters)
    eachUserName = userFirstName + '.' + userLastName + str(i)
    eachEmailId = eachUserName + '@' + 'google' + '.com'
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


# new_firstName, new_lastName, new_emailId
new_firstName = 'Edward'
new_lastName = 'Smith'
new_emailId = new_firstName + '.' + new_lastName + '@' + 'google' + '.com'

# first_name, last_name, email_id
first_name = 'Stephen'
last_name = 'Wilson'
user_name = first_name + ' ' + last_name
email_id = first_name + '-' + last_name + '@' + 'google' + '.com'

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