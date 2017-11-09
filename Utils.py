# coding utf8
#!/usr/bin/env python3
import requests
import mimetypes
import global_data
import logging
import json

logging.basicConfig(level=logging.DEBUG)

key = global_data.key
subscriptionid = global_data.subscriptionid
orgid = global_data.orgid
licensetype = global_data.licensetype
adminUserId = global_data.adminUserId

def post_multipart(url, fields, file):
    #===========================================================================
    # content_type, body = encode_multipart_formdata(fields, files)
    #===========================================================================
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Content-Type": "multipart/form-data",
        "Connection": "keep-alive",
        "x-api-key": key,
        "subscriptionid": subscriptionid,
        "orgid": orgid,
        "licensetype": licensetype,
        "userid": adminUserId
        }
    logging.info("header: %s" % headers)
    res = requests.post(url=url, files=file, headers=headers, json=fields)
    return res.status_code, res.json()

def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------bound@ry_$'
    CRLF = '\r\n'
    L = []
 #   for (key, value) in fields.iteritems():
    for (key, value) in fields.items():
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(str(L))
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'