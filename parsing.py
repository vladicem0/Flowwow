import requests
import logging
import pandas as pd


def request(url: str, headers: dict[str, str] = None) -> dict:
    try:
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'}
        req = requests.get(url, headers=headers)
        data = req.json()
    except requests.ConnectionError:
        logging.error('Connection error', exc_info=True)
        data = {'conversion_rates': 'None'}
    return data


def save(json_data: dict, path: str = 'data') -> None:
    d = pd.DataFrame(data=json_data, index=['Rate_to_USD'])
    d.to_excel(f'{path}\\data.xlsx')
    d.to_csv(f'{path}\\data.csv')
