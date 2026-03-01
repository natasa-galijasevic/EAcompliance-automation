import requests
from requests.auth import HTTPBasicAuth

base_url="https://wiki.rbinternational.com/"
page_id="5330309263"
email ="natasa.galijasevic.raiffeisengroup.ba"
import os
api_token=os.environ.get("ConfluenceToken")

response = requests.get(
  f"{base_url}/{page_id}?expand=body.storage",
  auth=HTTPBasicAuth(email, api_token)
  )
# if response.status_code == 200:
    # page = response.json()
    # title = page["title"]
    # content = page["body"]["storage"]["value"]
    # print(f"Page title: {title}\n")
    # print(f"Content (prvoh 300 karaktera):\n{content[:500]}...")
# else:
    # print(f"Failed to fetch page: {response.status_code} - {response.text}")

print("STATUS CODE:")
print(response.status_code)

print("RESPONSE TEXT:")
print(response.text[:500])
