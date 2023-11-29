import requests
from config import ACCESS_TOKEN

def delete_an_attachment(record_id, ids):
    for attachment_id in ids:
        url = f'https://www.zohoapis.in/crm/v2/Responses/{record_id}/Attachments/{attachment_id}'

        headers = {
            'Authorization': ACCESS_TOKEN
        }

        response = requests.delete(url=url, headers=headers)

        if response is not None:
            print(f"HTTP Status Code : {response.status_code}")

            #print(response.json())
            print("Deleted")

# delete_an_attachment()