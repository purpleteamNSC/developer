import os
from dotenv import load_dotenv
from Helix import Helix_T

load_dotenv()

client_id = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')
scope = os.getenv('SCOPE')

nsc = Helix_T('nsc', 123, 'a1b2c3')

token = nsc.get_access_token(client_id, secret, scope)

print(token)