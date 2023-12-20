import requests
import json


def materials_request(url='https://www.cybersport.ru/api/materials?page%5Blimit%5D=5&filter%5Bmain%5D=true'):

    response = requests.get(url)

    response_text = json.loads(response.text)
    answer = {"status_code": response.status_code,
              "data": response_text["data"]}

    return answer
