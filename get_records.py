def get_record():
    import requests

    url = 'https://www.zohoapis.in/crm/v2/Hospitals/245366000000223001'

    headers = {
        'Authorization': 'Zoho-oauthtoken 1000.ceb13990b74dab96e35fa26759d45812.edaf760d7294f93b2bdb0e14a833d144',

    }

    # parameters = {
    #     'approved': 'both',
    #     'converted': 'both',
    #     'cvid': '3409643000002804006',
    #     'uid': '3409643000002804154',
    #     'fields': 'Name,Email',
    #     'territory_id': '3409643000002804205',
    #     'include_child': 'false',
    # }

    response = requests.get(url=url, headers=headers)

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

        print(response.json())


get_record()