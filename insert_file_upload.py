import requests
import json
from config import ACCESS_TOKEN


def update_record(record_id, file_ids):

    url = 'https://www.zohoapis.in/crm/v2/Responses/'+ record_id

    headers = {
        'Authorization': ACCESS_TOKEN,
    }

    request_body = dict()

    request_body = {
    'data': [
        {
            'documents': [file_ids[0], file_ids[1]],
        }
    ],
}
    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.put(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        #print(response.json())

        return response.json()