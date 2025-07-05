import requests

url = "https://hermes--co.com/connectionsws?os_id=2"
r = requests.get(url)
print(r.status_code)
print(r.text)
