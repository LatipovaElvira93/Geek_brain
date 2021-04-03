import requests
import json
from datetime import datetime


def curency_rate(code):
    upper_code = code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = json.loads(response.content)
    return_valute = data['Valute'].get(upper_code)

    if return_valute:
        value = return_valute['Value']
        return value

print(curency_rate('usd'))