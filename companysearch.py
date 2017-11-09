# coding utf8
import pytest
import requests
import linecache
import logging
import global_data

logging.basicConfig(level=logging.INFO)

baseUrl = global_data.baseUrl
company_search = global_data.companysearch
url = baseUrl + company_search
companydetail_url = baseUrl + global_data.companydetailurl

key = global_data.key
subscriptionid = global_data.subscriptionid
orgid = global_data.orgid
ContentType = global_data.ContentType
licensetype = global_data.licensetype
adminUserId = global_data.adminUserId
companyId1 = global_data.COMPANYID1


header = {
    'x-api-key': key,
    'subscriptionid': subscriptionid,
    'orgid': orgid,
    'licensetype' : licensetype,
    'userid' : adminUserId,
    'Content-Type': ContentType
}

# Read data from file
line = linecache.getline('./datasource/contact_info.csv', 2)
search_info = line.split(',')
company = search_info[2]
website = search_info[3]
city = search_info[5]
state = search_info[6]
country = search_info[7]
region = search_info[8]
industry = search_info[12]
subIndustry = search_info[13]
product = search_info[14]
productParentCategory = search_info[15]
productCategory = search_info[16]

global companyIds_name, companyIds_website, companyIds_industry, companyIds_subIndustry, companyIds_product, company_set
company_ids = []
companyIds_website = []
companyIds_industry = []
companyIds_subIndustry = []
companyIds_product = []
company_set = set()

# Read companyName from file
line2 = linecache.getline('./datasource/companyHQ_info.csv', 2)
search_list = line2.split(',')
company_name = search_list[0]
key_word = company_name.split(' ')[0]
hq_city = search_list[2]
hq_state = search_list[3]
hq_country = search_list[4]
hq_region = search_list[5]
hq_address = search_list[6]
hq_phone = search_list[7]
hq_website = search_list[8].strip()


@pytest.mark.companysearch
def test_companysearchbycompany():
    """Search companyName"""
    param = {"companyName": company_name, "includeDownloaded": "true"}
    logging.info("Search company by name: %s" % company_name)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global comp_num
    comp_num = len(resp)
    for i in range(0, len(resp)):
    #logging.info(" Expected: %s vs Output: %s " % (key_word, resp[i]["companyName"]))
        assert key_word in resp[i]["companyName"]
        company_ids.append(resp[i]["companyId"])


@pytest.mark.companysearch
def test_companysearchbycompanyhq():
    """Search companyName onlyHQ"""
    param = {"companyName": company_name, "onlyHQ": "true", "includeDownloaded": "true"}
    logging.info("Search company by name onlyHQ: %s" % company_name)
    r = requests.get(url, params=param, headers=header)
    print(r)    
    assert r.status_code == 200
    resp = r.json()
    hq_num = len(resp)
    for i in range(0, hq_num):
        company_set.add(resp[i]["companyName"])
        assert key_word in resp[i]["companyName"]
        if resp[i]["companyName"] == company_name:
            #assert resp[i]["city"] == hq_city and resp[i]["state"] == hq_state and resp[i]["country"] == hq_country and resp[i]["region"] == hq_region and resp[i]["websiteExactName"] == hq_website
            assert resp[i]["city"] == hq_city
    assert len(company_set) == hq_num


@pytest.mark.companysearch
def test_companydetailssearch():
    """Search contact details by companyName"""
    companyIds = company_ids[0] + "," + company_ids[1] + "," + company_ids[2]
    search_companyId = companyIds.split(',')
    param = {"companyIds": companyIds}
    logging.info("Search company details by company name: %s" % companyIds)
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert len(resp) == len(search_companyId)
    for i in range(0, len(resp)):
        assert resp[i]["companyName"] == company_name and resp[i]["companyId"] in search_companyId


@pytest.mark.companysearch
def test_companysearchbywebsite():
    """Search website"""
    param = {"website": website, "includeDownloaded": "true"}
    logging.info("Search company by website: %s" % website)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["websiteExactName"].split('.')[1] in company.lower()
        companyIds_website.append(resp[i]["companyId"])


@pytest.mark.companysearch
def test_companydetailswebsite():
    """Search company details by website"""
    companyIds = companyIds_website[0] + ',' + companyIds_website[1] + ',' + companyIds_website[2]
    logging.info("Search company details by website: %s" % companyIds)
    param = {"companyIds": companyIds}
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()

    for i in range(0, len(resp)):
       # print(r.content)       
       # print(resp[i]["productInstalledExactName"])
        #assert resp[i]["urlExactName"].rsplit('/', 1)[-1] in company.lower() and resp[i]["productInstalledExactName"] is not None
        assert resp[i]["urlExactName"].rsplit('/', 1)[-1] in company.lower() 
        
@pytest.mark.companysearch
def test_companysearchbyindustry():
    """Search industry"""
    param = {"industry": industry}
    logging.info("Search company by industry: %s" % industry)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        companyIds_industry.append(resp[i]["companyId"])


@pytest.mark.companysearch
def test_companydetailsindustry():
    """Search company details by industry"""
    companyIds = companyIds_industry[0] + ',' + companyIds_industry[1]
    logging.info("Search company details by industry: %s" % companyIds)
    param = {"companyIds": companyIds}
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        #assert resp[i]["industry"] == industry and resp[i]["productInstalledExactName"] is not None
        assert resp[i]["industry"] == industry 

@pytest.mark.companysearch
def test_companysearchbysubIndustry():
    """Search subIndustry"""
    param = {"subIndustry": subIndustry}
    logging.info("Search company by subIndustry: %s" % subIndustry)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        companyIds_subIndustry.append(resp[i]["companyId"])


@pytest.mark.companysearch
def test_companydetailssubIndustry():
    """Search company details by subIndustry"""
    companyIds = companyIds_subIndustry[0]
    logging.info("Search company details by subIndustry: %s" % companyIds)
    param = {"companyIds": companyIds}
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        #assert resp[i]["subIndustry"] == subIndustry and resp[i]["productInstalledExactName"] is not None
        assert resp[i]["subIndustry"] == subIndustry 

@pytest.mark.companysearch
def test_companysearchbycity():
    """Search city"""
    param = {"city": city}
    logging.info("Search company by city: %s" % city)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["city"] == city


@pytest.mark.companysearch
def test_companysearchbystate():
    """Search state"""
    param = {"state": state}
    logging.info("Search company by state: %s" % state)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["state"] == state


@pytest.mark.companysearch
def test_companysearchbycountry():
    """Search country"""
    param = {"country": country}
    logging.info("Search company by country: %s" % country)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["country"] == country


@pytest.mark.companysearch
def test_companysearchbyregion():
    """Search region"""
    param = {"region": region}
   # print(region)
    logging.info("Search company by region: %s" % region)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        region2=resp[i]["region"].lower()
        region1=region.lower()
        assert region2==region1


@pytest.mark.companysearch
def test_companysearchbyproduct():
    """Search product"""
    param = {"product": product}
    logging.info("Search company by product: %s" % product)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        companyIds_product.append(resp[i]["companyId"])


@pytest.mark.companysearch
def test_companydetailsproduct():
    """Search company details by product"""
    companyIds = companyId1
    logging.info("Search company details by product: %s" % companyIds)
    param = {"companyIds": companyIds}
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        #assert product in resp[i]["productInstalledExactName"] and resp[i]["companyTypeExactName"] is not None
        #assert product in resp[i]["companyTypeExactName"] 
        assert r.status_code == 200
        
@pytest.mark.companysearch
def test_companysearchbyproductParentCategory():
    """Search productParentCategory"""
    param = {"productParentCategory": productParentCategory}
    logging.info("Search company by productParentCategory: %s" % productParentCategory)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200


@pytest.mark.companysearch
def test_companysearchbyproductCategory():
    """Search productCategory"""
    param = {"productCategory": productCategory}
    logging.info("Search company by productCategory: %s" % productCategory)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200


@pytest.mark.companysearch
def test_companysearchbyall():
    """Search companyName, product, region, country, state, city, industry, subIndustry, website"""
    param = {"companyName": company,
             "product": product,
             "region": region,
             "country": country,
             "state": state,
             "city": city,
             "industry": industry,
             "subIndustry": subIndustry,
             "website": website
             }
    logging.info("Search company by companyName: %s, product: %s, region: %s, country: %s, state: %s, city: %s, "
                 "industry: %s, subIndustry: %s, website: %s" % (company, product, region, country, state, city,
                                                                 industry, subIndustry, website))
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    global companyId
    companyId = resp[0]["companyId"]
    assert resp[0]["companyName"] == company and resp[0]["region"].lower() == region.lower() and resp[0]["country"] == country \
           and resp[0]["state"] == state and resp[0]["city"] == city and resp[0]["websiteExactName"].rsplit('.')[1] in company.lower()


@pytest.mark.companysearch
def test_companysearchlimitsize():
    """Limit search result size by using resultSize"""
    size = 8
    param = {"country": country, "resultSize": size}
    logging.info("Search company by country and limited by resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200 and len(r.json()) == size


@pytest.mark.companysearch
def test_companysearchlimitzerosize():
    """Limit search result size by using 0 resultSize"""
    size = 0
    param = {"country": country, "resultSize": size}
    logging.info("Search company by country and limited by resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 404 and r.json()["message"] == "No Data Found"


@pytest.mark.companysearch
def test_companysearchinvalidlimitsize():
    """Limit search result size by using invalid resultSize"""
    size = "two"
    param = {"country": country, "resultSize": size}
    logging.info("Search company by country and limited by using invalid resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 206 and r.json()["message"] == "Invalid attribute name or invalid attribute case"


@pytest.mark.companysearch
def test_companysearchminusonelimitsize():
    """Limit search result size by using -1 resultSize"""
    size = -1
    param = {"country": country, "resultSize": size}
    logging.info("Search company by country and limited by using -1 as resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code >= 200 and len(r.json()) == 1


@pytest.mark.companysearch
def test_companysearchminusnumlimitsize():
    """Limit search result size by using -12 resultSize"""
    size = -12
    param = {"country": country, "resultSize": size}
    logging.info("Search company by country and limited by using -12 resultSize: %s" % size)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code >= 200 and len(r.json()) == 1


@pytest.mark.companysearch
def test_companysearchbycompanycomma():
    """Search company by companyName which includes comma"""
    global companyname
    companyname = global_data.COMPANYNAME
    param = {"companyName": companyname}
    print(companyname)
    logging.info("Search company by company name which includes comma: %s" % companyname)
    r = requests.get(url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["companyName"] in companyname
        company_ids.append(resp[i]["companyId"])


@pytest.mark.companysearch
def test_companydetailssearchnamecomma():
    """Search contact details by companyName which includes comma"""
    m = len(company_ids)
    search_companyId = company_ids[m - 1]
    param = {"companyIds": search_companyId}
    logging.info("Search company details by company name which includes comma: %s" % companyname)
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    assert resp[0]["companyName"] in companyname and resp[0]["companyId"] == search_companyId

@pytest.mark.companysearch
def test_searchcompanybyid():
    """Search company by companyId"""
    companyIds = company_ids[0]
    logging.info("Search company by companyId: %s" % companyIds)
    param = {"companyIds": companyIds}
    r = requests.get(companydetail_url, params=param, headers=header)
    assert r.status_code == 200
    resp = r.json()
    for i in range(0, len(resp)):
        assert resp[i]["companyId"] == companyIds 
