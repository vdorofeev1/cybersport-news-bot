import json
import re
import requests


def slug_request(slug, url='https://www.cybersport.ru/api/materials/slug/'):
    url = url + slug

    response = requests.get(url)
    response_data = response.json()["data"]

    answer = {"status_code": response.status_code,
              "data": response_data}

    return answer


def clean_text(text):
    pattern = r'<.*?>'
    result = re.sub(pattern, '', text)

    return result.replace("&nbsp;", " ")
