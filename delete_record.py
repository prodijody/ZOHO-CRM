def delete_record():
    import requests

    url = 'https://www.zohoapis.com/crm/v2/Leads/245366000000223001'

    headers = {
        'Authorization': 'Zoho-oauthtoken 1000.ceb13990b74dab96e35fa26759d45812.edaf760d7294f93b2bdb0e14a833d144',
    }

    parameters = {
        'wf_trigger': 'true'
    }

    response = requests.delete(url=url, headers=headers, params=parameters)

    if response is not None:
        print(f"HTTP Status Code : {response.status_code}")

        print(response.json())

delete_record()