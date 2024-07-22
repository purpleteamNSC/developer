import os
from dotenv import load_dotenv
from Helix import Helix_T

load_dotenv()

org = os.getenv('ORG')
helix_id = os.getenv('HELIX_ID')
client_id = os.getenv('CLIENT_ID')
secret = os.getenv('SECRET')
scope = os.getenv('SCOPE')

nsc = Helix_T(org, helix_id, client_id, secret, scope)

# token = nsc.get_access_token()

researches = nsc.get_search_saved()
# for r in researches.get('results', []):
#     print(f"{r['name']} - {r['query']}")