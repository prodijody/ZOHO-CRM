def get_file():
    import requests
    import os

    url = 'https://www.zohoapis.in/crm/v2/files'

    headers = {
        'Authorization': 'Zoho-oauthtoken 1000.334a8616f1ee1a3a85f790b99ef112e3.e02ab75b6aaa5869070b2ae9eb84294a'
    }

    parameters = {
        'id': '13e85e75a9e2d06a10ea7491733d4bde7293b5843db1baaec02118afb81e96a4'
    }

    response = requests.get(url=url, headers=headers, params=parameters)

    if response is not None:
        print("HTTP Status Code : " + str(response.status_code))

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


