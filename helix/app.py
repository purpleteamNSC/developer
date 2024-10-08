import os
from dotenv import load_dotenv
from Helix import Helix_T
from pprint import pprint

load_dotenv()

org = os.getenv('X_ORG')
helix_id = os.getenv('X_HELIX_ID')
client_id = os.getenv('X_CLIENT_ID')
secret = os.getenv('X_SECRET')
scope = os.getenv('X_SCOPE')

x = Helix_T(org, helix_id, client_id, secret, scope)

results = x.get_search_saved().get('results',[])[0]
# pprint(results)

name = results['name']
query = results['query']

print(name)
print(query)

