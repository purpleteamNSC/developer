import os
from dotenv import load_dotenv
from Helix import Helix_T

load_dotenv()

org = os.getenv('X_ORG')
helix_id = os.getenv('X_HELIX_ID')
client_id = os.getenv('X_CLIENT_ID')
secret = os.getenv('X_SECRET')
scope = os.getenv('X_SCOPE')

x = Helix_T(org, helix_id, client_id, secret, scope)

# token = nsc.get_access_token()
# print(token)
# researches = nsc.get_index('class=analytics | groupby analytic')
# for r in researches.get('results', []):
#     print(f"{r['name']} - {r['query']}")

# x.get_index('class=analytics | groupby analytic')
print(x.get_search_saved())
