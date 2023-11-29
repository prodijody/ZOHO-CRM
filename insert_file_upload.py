import requests
import json
from config import ACCESS_TOKEN


def update_record(record_id, file_ids):

    url = f'https://www.zohoapis.in/crm/v2/Responses/{record_id}'

    headers = {
        'Authorization': ACCESS_TOKEN,
    }

    request_body = dict()

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body = {
        'data': [
            {
                'documents': file_ids,
            }
        ],
        'trigger': trigger,
    }
    response = requests.put(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))

    if response is not None:
        print(f"HTTP Status Code : {response.status_code}")

        #print(response.json())

        return response.json()