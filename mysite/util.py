import os
BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
# 읽어올 json의 경로
SECRETS_PATH = os.path.join(BASE_DIR, 'server_info.json')

import json

def get_server_info_value(key: str):

    with open(SECRETS_PATH, mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for k, v in data.items():
            if k == key:
                return v
        raise ValueError('서버정보를 확인할 수 없습니다.')