def insert_records():
    import requests
    import json

    url = 'https://www.zohoapis.in/crm/v2/Hospitals'

    headers = {
        'Authorization': 'Zoho-oauthtoken 1000.ceb13990b74dab96e35fa26759d45812.edaf760d7294f93b2bdb0e14a833d144',
    }

    request_body = dict()
    record_list = list()

    record_object_1 = {
        'Name': 'Zylker',
        'Email': 'p.daly@zylker.com'
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