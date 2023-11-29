import requests
from config import ACCESS_TOKEN


def get_attachments(record_id):

    url = f'https://www.zohoapis.in/crm/v2/Responses/{record_id}/Attachments'

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
        print(f"HTTP Status Code : {response.status_code}")
        print(response.json())
        return [obj['id'] for obj in response.json()['data']]

#get_attachments()