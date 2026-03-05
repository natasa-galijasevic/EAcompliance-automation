
from atlassian import Confluence

url = "https://wiki.rbinternational.com/confluence"
username = "natasa.galijasevic@raiffeisengroup.ba"   # PAT zahtijeva e-mail
password = "ConfluenceToken"                             # pravi Confluence API token

confluence = Confluence(
    url=url,
    username=username,
    password=token,
    verify_ssl=False,  # čest problem u internim mrežama
)

space_key = "RBBHIT"

try:
    space = confluence.get_space(space_key)
    print(space)
except Exception as e:
    print("Error:", e)
