def get_file():
    import requests
    import os

    url = 'https://www.zohoapis.in/crm/v2/files'

    headers = {
        'Authorization': 'Zoho-oauthtoken 1000.bf6d1e66ce448437d058bb87b3e132f5.212333fdbf02f9f1a7b9384423634f8a'
    }

    parameters = {
        'id': '13e85e75a9e2d06a10ea7491733d4bdee9bc1a805194a387d4a944518f23ba31'
    }

    response = requests.get(url=url, headers=headers, params=parameters)

    if response is not None:
        print(f"HTTP Status Code : {response.status_code}")

        if 'Content-Disposition' in response.headers:
            file_name = ''
            content_disposition = response.headers['Content-Disposition']

            if "'" in content_disposition:
                start_index = content_disposition.rindex("'")
                file_name = content_disposition[start_index + 1:]

            elif '"' in content_disposition:
                start_index = content_disposition.rindex('=')
                file_name = content_disposition[start_index + 1:].replace('"', '')

            destination_file = os.path.join('./', file_name)

            with open(destination_file, 'wb') as f:
                for chunk in response:
                    f.write(chunk)

        else:
            print(response.json())

get_file()


