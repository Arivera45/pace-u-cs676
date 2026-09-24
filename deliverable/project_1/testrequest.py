import requests

url = "https://www.biorxiv.org/content/10.1101/2020.01.01.0000"

response = requests.get(url, timeout=5)

print(response.text[:5000])
