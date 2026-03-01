import requests
from requests.auth import HTTPBasicAuth

base_url=""
page_id=""
email ="natasa.galijasevic.raiffeisengroup.ba"
api_tokem = ""

response = requests.get(
  f"{base_url}/{page_id}?expand=body.storage",
  auth=HTTPBasicAuth(email, api_token)
  )
  if response.status_code == 200:
    page = response.json()
    title = page["title"]
  content = page["body"]["storage"]["value"]
    print(f"Page title: {title}\n")
    print(f"Content (prvoh 500 karaktera):\n{content[:500]}...")
  else:
    print(f"Failed to fetch page: {response.status_code} - {response.text}")
