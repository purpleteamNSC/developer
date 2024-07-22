import requests

class Helix_T:
    def __init__(self, organization, helix_id, client_id, secret, scope):
        self.base_url = 'https://apps.fireeye.com'
        self.organization = organization
        self.helix_id = helix_id
        self.client_id = client_id
        self.secret = secret
        self.scope = scope
        
    def get_access_token(self):
        url = 'https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'grant_type': 'client_credentials',
            'scope': self.scope
        }

        auth = (self.client_id, self.secret)
        
        try:
            response = requests.post(url, headers=headers, auth=auth, data=data)
            response.raise_for_status()
            
            return response.json()['access_token']
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        
        return None
    
    def get_search_saved(self):
        """
        Busca todas as pesquisas salvas na API para um helix_id específico.
        """
        try:
            url = f"{self.base_url}/helix/id/{self.helix_id}/api/v3/search/saved/"
            headers = {
                "x-trellix-api-token": f"Bearer {self.get_access_token()}",
                "accept": "application/json"
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        
        return None

class Helix_F:
    def __init__(self, organization, helix_id, apikey):
        self.organization = organization
        self.helix_id = helix_id
        self.apikey = apikey