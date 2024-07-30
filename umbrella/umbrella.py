from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()

key = os.getenv('UMBRELLA_KEY')
secret = os.getenv('UMBRELLA_SECRET')
list = os.getenv('LIST_ID')

def get_umbrella_token(key, secret):
    
    url = 'https://api.umbrella.com/auth/v2/token'

    auth = (key, secret)

    data = {
        'grant_type': 'client_credentials'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, auth=auth, data=data, headers=headers)

    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None

def get_networks(token):
    url = 'https://api.umbrella.com/deployments/v2/networks'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

def get_destination_list(token):
    url = 'https://api.umbrella.com/policies/v2/destinationlists'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        data = data['data']
        return data
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

def add_destination_to_list(token,ioc):
    url = f'https://api.umbrella.com/policies/v2/destinationlists/{list}/destinations'

    data = [
        {
            "destination": ioc,
            "comment": "MXDR"
        }
    ]

   
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token,
    }

    
    response = requests.post(url, json=data, headers=headers)

    
    if response.status_code == 200:
        print(response.status_code)
        print("Adicionado na lista com sucesso")
        return response.json()
    else:
        # Imprime a mensagem de erro caso ocorra algum problema
        print(f"Erro: {response.status_code} - {response.text}")
        return None


# HOMOLOGAÇÃO 
token = get_umbrella_token(key, secret)

if token:
    add_destination_to_list(token,'tinyurl.com')
    add_destination_to_list(token,'www.tinyurl.com')
    add_destination_to_list(token,'iti.itau')
    add_destination_to_list(token,'20.212.168.117')

