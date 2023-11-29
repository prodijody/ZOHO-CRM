import requests
import os
from config import ACCESS_TOKEN


def download_attachment(record_id, ids):
    paths = []
    for attachment_id in ids:
        url = f'https://www.zohoapis.in/crm/v2/Responses/{record_id}/Attachments/{attachment_id}'

        headers = {
            'Authorization': ACCESS_TOKEN
        }

        response = requests.get(url=url, headers=headers)

        if response is not None:
            print(f"HTTP Status Code : {response.status_code}")

            if 'Content-Type' in response.headers:
                content_type = response.headers['Content-Type'].split(';')[0]

                if content_type == 'application/json':
                    print(response.json())
                elif 'Content-Disposition' in response.headers:
                    file_name = ''
                    content_disposition = response.headers['Content-Disposition']

                    if "'" in content_disposition:
                        start_index = content_disposition.rindex("'")
                        file_name = content_disposition[start_index + 1:]

                    elif '"' in content_disposition:
                        start_index = content_disposition.rindex('=')
                        file_name = content_disposition[start_index + 1:].replace('"', '')

                    destination_file = os.path.join('./Attachments',file_name)
        paths.append(destination_file)

        with open(destination_file, 'wb') as f:
            for chunk in response:
                f.write(chunk)
    return paths

# print(download_attachment())