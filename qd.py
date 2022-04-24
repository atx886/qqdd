import json
import time

import requests


def gettoken(r):
    t = r.text
    p = t[t.index("bPfmSW"):t.index("\"}")].encode('ascii').decode('utf-8')
    print(p)
    return p


session = requests.session()

session.get('https://www.chaojijishi.com')

url = 'https://www.chaojijishi.com/api/login'

data = {
    'mobile': 17000651668,
    'password': 123456,
    'XDEBUG_SESSION_START': 'PHPSTORM',
    'timestamp': int(round(time.time() * 1000))
}
# ck = 'eyJpdiI6Ikoyc2FrRGoyQzBIdFk3cEVVM2pBRVE9PSIsInZhbHVlIjoiQm44RUo5SWtjcGlwbXdBUkRuZHhSKzV5VEV3QjJaMVRObTh5emdDekYxQnRjczlwYzJxbXVKdW82TGJXYXJCUCIsIm1hYyI6IjEwNjk4ZGQzM2M2MjM0Y2RmMzRhZWUyNjc1ZmEwNmFmZTY2MDk4ZWRkZWM3YjQ4ZjNiMTMzYzNmNTEyMGY4NzEifQ%3D%3D'
r = session.post(url, data=data)
print(r.status_code)
ck = session.cookies.get_dict()
print(ck)

tk = gettoken(r)

data1 = {
    'mobile': 17000651668,
    'password': 123456,
    'XDEBUG_SESSION_START': "PHPSTORM",
    'timestamp': int(round(time.time() * 1000)),
    'token': tk

}

header = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'content-type': 'application/json;charset=UTF-8',
    # 'Authorization': 'Bearer bPfmSWNULUfPf4FAL7tYR0IdFf+YEAV+7HuQ1P0c131ySHgPnZ5TS1UO9hjcdq9lIkbXDak6YRPXH7aOSfFZxw==',
    'token':tk,
    'b': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.chaojijishi.com/h5/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'

    # """"
    #
    # bPfmSWNULUfPf4FAL7tYR+r+GSiu3ZLA5u3Rgv42x/vMbc5RMFaBPRSwXuJi/IbrIkbXDak6YRPXH7aOSfFZxw==
    #
    # """"

}

header11 = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'content-type': 'application/x-www-form-urlencoded',
    'Content-Length': '160',
    'Origin': 'https://www.chaojijishi.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.chaojijishi.com/h5/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
}

url2 = 'https://www.chaojijishi.com/api/task/reward_info'
r = session.get(url2, headers=header)
res = r.content.decode('utf-8')
res = json.loads(res)
print(res)

url1 = 'https://www.chaojijishi.com/api/task/complete_task'

r = session.post(url1, data=data1, headers=header11)
res = r.content.decode('utf-8')
res = json.loads(res)
print(res)
