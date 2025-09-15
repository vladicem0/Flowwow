import logging
import json
import time
from parsing import request, save


def get_time(in_filename: bool = False) -> str:
    system_time = str(time.strftime('%d.%m.%Y %H:%M:%S', time.localtime()))
    return system_time.replace(':', '_') if in_filename else system_time


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='logs.log', format='%(asctime)s %(levelname)s %(message)s')

    with open('logs.log', 'a') as file:
        file.write(f'\nStart time {get_time()}\n')

    with open('api_key.txt', 'r') as file:
        api_key = file.read()

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    json_data = request(url)

    with open(f'backup\\{get_time(in_filename=True)}.json', 'w') as file:
        json.dump(json_data, file)

    save(json_data['conversion_rates'])
