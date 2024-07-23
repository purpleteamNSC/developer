import os
import requests
from dotenv import load_dotenv
load_dotenv()

# curl -XPOST -H "Authorization: $APIKEY" -d '{ "class":"myclass", "rawmsg": "My message" }' https://helix-integrations.cloud.aws.apps.fireeye.com/api/upload

class Axur:
    def __init__(self,token):
        self.base_url = 'https://api.axur.com/gateway/1.0/api'
        self.token = token

    
    def get_types(self):
        url = f'{self.base_url}/tickets-core/fields/types'
 
        header = {
            'Content-Type': 'application/json',
            'Authorization': str.format("Bearer {}", self.token)
        }

        try:
            result = requests.get(url, headers=header)
            print(result.json())
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        

    def subscriptions(self):
        url = f'{self.base_url}/webhooks/subscriptions'
 
        header = {
            'Content-Type': 'application/json',
            'Authorization': str.format("Bearer {}", self.token)
        }

        try:
            result = requests.get(url, headers=header)
            print(result.status_code)
            print(result.text)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
