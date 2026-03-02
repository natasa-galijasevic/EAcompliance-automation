from atlassian import Confluence

url="https://wiki.rbinternational.com/confluence"
username = "IBAASNA"
token = "ConfluenceToken"

confluence = Confluence(
  url=url,
  username=username,
  password=token
)

space_key="RBBHIT"
space = confluence.get_space(space_key)
print(space)

