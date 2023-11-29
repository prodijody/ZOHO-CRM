import requests
from config import ACCESS_TOKEN


def upload_files_to_zfs(paths):

    url = 'https://www.zohoapis.in/crm/v2/files'

    headers = {
        'Authorization': ACCESS_TOKEN
    }

    parameters = {
        'type': 'inline'
    }

    request_body = []
    for attachment in paths:
        file_1_tuple = ('file', open(attachment, 'rb'))
        request_body.append(file_1_tuple)

    response = requests.post(url=url, files=request_body, headers=headers, params=parameters)

    if response is not None:
        ids = []
        print(f"HTTP Status Code : {response.status_code}")

        #print(response.json())
        for obj in response.json()['data']:
            obj2 = obj['details']
            ids.append(obj2['id'])
        return ids

# print(upload_files_to_zfs())