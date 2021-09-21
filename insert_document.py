# def upload_files_to_zfs():
#     import requests

#     url = 'https://www.zohoapis.in/crm/v2/files'

#     headers = {
#         'Authorization': 'Zoho-oauthtoken 1000.77b3d457ccaec9a82c764eaba6cd9ba6.c43c5a43da41e47379a0509817abd950'
#     }

#     parameters = {
#         'type': 'inline'
#     }

#     request_body = []
#     file_1_tuple = ('file', open('D:/Abhinav/Images/wallpaper.png', 'rb'))
#     request_body.append(file_1_tuple)

#     response = requests.post(url=url, files=request_body, headers=headers, params=parameters)

#     if response is not None:
#         print("HTTP Status Code : " + str(response.status_code))

#         print(response.json())

# upload_files_to_zfs()

# #id = 13e85e75a9e2d06a10ea7491733d4bde65cc217b3f2b2c9f93f4976c5818558e

def update_record():
    import requests
    import json

    url = 'https://www.zohoapis.in/crm/v2/Responses/245366000000271058'

    headers = {
        'Authorization': 'Zoho-oauthtoken 1000.e7f500c2890dd90ec1ff9b10325da0c2.cfa021f58f559cffae56b9ac723ca4bb',
    }

    request_body = dict()

    file_id = '13e85e75a9e2d06a10ea7491733d4bde7293b5843db1baaec02118afb81e96a4'

    request_body = {
    'data': [
        {
            'documents': [file_id],
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

        print(response.json())

update_record()