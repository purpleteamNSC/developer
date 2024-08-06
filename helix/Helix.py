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

    def get_index(self, query):
        """
        Executa a pesquisa no índice e salva os resultados.
        
        Args:
            name (str): Nome da pesquisa.
            query (str): Query da pesquisa.
        """
        try:
            url = f"https://apps.fireeye.com/helix/id/{self.helix_id}/api/v1/search"
            headers = {
                "Content-Type": "application/json",
                "x-trellix-api-token": f"Bearer {self.get_access_token()}",
            }
            payload = {"query": f"start='1 month ago' {query}"}
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()

            results = response.json().get('results', {}).get('aggregations', {}).items()
            
            data = None
            for _, v in results:
                if 'buckets' in v:
                    data = v['buckets']

            if data:
                # save_index(company, name, query, data)
                print(data)
            else:
                # logging.warning(f"{company} - Sem dados para a pesquisa '{name}'")
                print('error ao salvar em data')
        except requests.exceptions.RequestException as e:
            # logging.warning(f"{company} - Erro na requisição ao endpoint '{name}': {e}")
            print(e)
        except Exception as e:
            # logging.warning(f"{company} - Erro ao obter índice para a pesquisa '{name}': {e}")
            print(e)
        
        return None


class Helix_F:
    def __init__(self, organization, helix_id, apikey):
        self.base_url = 'https://apps.fireeye.com'
        self.organization = organization
        self.helix_id = helix_id
        self.apikey = apikey

    def get_search_saved(self):
        """
        Busca todas as pesquisas salvas na API para um helix_id específico.
        """
        try:
            url = f"{self.base_url}/helix/id/{self.helix_id}/api/v3/search/saved/?limit=50"
            headers = {
                "x-fireeye-api-key": self.apikey,
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
    

    def get_archive_id(self):
        """
        Busca pesquisa feita no archive por id.
        """
        try:
            url = f"{self.base_url}/helix/id/{self.helix_id}/api/v3/search/saved/?limit=50"
            headers = {
                "x-fireeye-api-key": self.apikey,
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
    
    