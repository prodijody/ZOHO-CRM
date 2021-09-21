from config import ACCESS_TOKEN


def insert_records():
    import requests
    import json

    url = 'https://www.zohoapis.in/crm/v2/Queries'

    headers = {
        'Authorization': ACCESS_TOKEN,
    }

    request_body = dict()
    record_list = list()

    record_object_1 = {
        'Name1': 'Zylker',
        'Mobile': '8367272772',
        'Query': "I have headache",
        'Status': "New",
        'partner_name': "Justin Bieber"
    }


    record_list.append(record_object_1)


    request_body['data'] = record_list

    trigger = [
        'approval',
        'workflow',
        'blueprint'
    ]

    request_body['trigger'] = trigger

    response = requests.post(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())

insert_records()