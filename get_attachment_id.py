import requests
from config import ACCESS_TOKEN


def get_attachments(record_id):

    url = 'https://www.zohoapis.in/crm/v2/Responses/' + record_id + '/Attachments'

    headers = {
        'Authorization': ACCESS_TOKEN
    }
    parameters = {
        'fields': 'id,Modified_Time',
        'page': 1,
        'per_page': 20
    }
    response = requests.get(url=url, headers=headers, params=parameters)
    if response is not None:
        ids = []
        print("HTTP Status Code : " + str(response.status_code))
        print(response.json())
        for obj in response.json()['data']:
            ids.append(obj['id'])
        return ids

#get_attachments()