#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import datetime
import time
import json
import sys



res = int(sys.argv[6])

#datetime_start = datetime.datetime.now()
#datetime_start_utc = datetime_start - datetime.timedelta(hours=8)  # 转换时区

datetime_start_utc = datetime.datetime.utcnow()
print(datetime_start_utc)


datetime_end_utc = datetime_start_utc + datetime.timedelta(minutes=res)  # 静默持续时间

url = "http://127.0.0.1:9093/api/v2/silences"

payload_dict = {
    "matchers": [
        {
            "name": "alertname",
            "value": sys.argv[1],
            "isRegex": False,
            "isEqual": True
        },
        {
            "name": "instance",
            "value": sys.argv[2],
            "isRegex": False,
            "isEqual": True

        },
        {
            "name":"job",
            "value": sys.argv[3],
            "isRegex": False,
            "isEqual": True
        },
        {
            "name":"nodename",
            "value": sys.argv[4],
            "isRegex": False,
            "isEqual": True
        },
        {
            "name":"severity",
            "value": sys.argv[5],
            "isRegex": False,
            "isEqual": True
        },


    ],
    "startsAt": datetime_start_utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
    "endsAt": datetime_end_utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
    "createdBy": "handsome",
    "comment": "gitlab_backup"
}
payload = json.dumps(payload_dict).encode('utf-8')

headers = {
#  'Authorization': 'Basic xxxxxxxxxxx',  # 认证
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

