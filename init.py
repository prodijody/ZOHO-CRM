import requests, json

def authenticate_crm():


    url = 'https://accounts.zoho.in/oauth/v2/token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # one time self-client token here -
    request_body = {
        "code": "1000.6032cb11b6a20df6df307cca07f84aed.ad1be850058ac6fa5acbfa6cc8de5171",
        "redirect_uri": "http://example.com/yourcallback",
        "client_id": "1000.IMEPYR7NACO7YZ8DOQCQZTDFZKLG0W",
        "client_secret": "3a250a77a55e78fbfbbf998db72c7db589f581ba72",
    " grant_type": "authorization_code"
    }

    #response = requests.post(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))
    response = requests.post(url=url, headers=headers, data=json.dumps(request_body).encode('utf-8'))
    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))
        print(response.json())

authenticate_crm()