import json
import requests


def login_request(url='https://www.cybersport.ru/api/identity/login'):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://www.cybersport.ru',
        'Referer': 'https://www.cybersport.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'same-origin',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                      'YaBrowser/23.5.1.575 (beta) Yowser/2.5 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Linux'
    }

    # Data
    data = {
        'username': 'vdorofeev.of@gmail.com',
        'password': 'qwerty88AZ',
        'captchaToken': ''
    }

    response = requests.post(url, headers=headers, json=data)

    response_text = json.loads(response.text)
    answer = {"status_code": response.status_code,
              "token": response_text["token"],
              "refresh_token": response_text["refresh_token"]}

    return answer
