import requests
import json


def materials_request(token, refresh_token,
                      url='https://www.cybersport.ru/api/materials?page%5Blimit%5D=5&filter%5Bmain%5D=true'):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9',
        'Cookie': f'ipp_uid2=xKJh1hKIcKqaVuRp/lO47bmAvOiy2KcCPiVCvHw==; ipp_uid1=1633615519280; '
                  f'ipp_uid=1633615519280/xKJh1hKIcKqaVuRp/lO47bmAvOiy2KcCPiVCvHw==; _ym_uid=1633615520875521723; '
                  f'p4s_p_push_subscription_status=blocked; last_visit=1643790903213::1643801703213; '
                  f'tmr_lvid=83b18816f58590e3cd0a9e46ce3120f8; tmr_lvidTS=1633615521094; _ym_d=1686669889; '
                  f'ipp_sign=59bfd496dc7371dc3f088d6222bee5a5_2076041217_b24319f0d3a891192d1b46c7e37042db; '
                  f'ipp_key=v1697347971780/v33947245ba5adc7a72e273/cCcChTQdSdGIpE/De/R9Kg==; '
                  f'rerf=AAAAAGU//uKIg2a9AwMYAg==; refresh-token={refresh_token}; _ga=GA1.2.1585135284.1633615520; '
                  f'_gid=GA1.2.286728567.1699267574; _ym_visorc=b; _ym_isad=2; tmr_detect=0%7C1699267578713; '
                  f'INGRESSCOOKIE=1699268336.147.32.38716|9ac2779136aafb631a39615b5bb7d9e4; token={token}; '
                  f'_gat_gtag_UA_22666504_1=1; _ga_36V5CDT1NB=GS1.1.1699267574.361.1.1699268518.0.0.0',
        'Referer': 'https://www.cybersport.ru',
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

    response = requests.get(url, headers=headers)

    response_text = json.loads(response.text)
    answer = {"status_code": response.status_code,
              "data": response_text["data"]}

    return answer
