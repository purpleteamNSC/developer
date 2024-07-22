import requests

class Helix_T:
    def __init__(self, organization, helix_id, apikey):
        self.organization = organization
        self.helix_id = helix_id
        self.apikey = apikey
        
    def get_access_token(self, client_id, client_secret, scope):
        url = 'https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'client_credentials',
            'scope': scope
        }

        auth = (client_id, client_secret)
        
        try:
            response = requests.post(url, headers=headers, auth=auth, data=data)
            response.raise_for_status()
            
            return response.json()['access_token']
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        
        return None
    

    def get_alert(self):
        pass