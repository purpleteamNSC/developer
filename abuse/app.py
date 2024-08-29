import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


class Abuse:

    def __init__(self, api):
        self.api = api

    def get_black_list(self):
        # Defining the api-endpoint
        url = "https://api.abuseipdb.com/api/v2/blacklist"

        querystring = {"confidenceMinimum": "90"}

        headers = {"Accept": "application/json", "Key": os.getenv("menir")}

        response = requests.request(
            method="GET", url=url, headers=headers, params=querystring
        )

        # Formatted output
        decodedResponse = json.loads(response.text)

        print(json.dumps(decodedResponse, sort_keys=True, indent=4))


class Helix:
    def __init__(self, id_helix, apikey):
        self.id_helix = id_helix
        self.apikey = apikey

    def create_list(self, name):
        pass

    def get_list(self):
        pass

    def delete_list(self, number):
        pass


print(os.getenv("menir"))
