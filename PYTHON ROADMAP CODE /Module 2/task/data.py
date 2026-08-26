import requests
from bs4 import BeautifulSoup
import json

PAGE_URL = "https://scaletech.xyz"

response = requests.get(PAGE_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

scripts = soup.find_all("script")

for script in scripts:
    print(script.get("src"))

api_response = requests.get(
    "https://admin.scaletech.xyz/api/testimonials?populate=*"
)
api_response.raise_for_status()

data = api_response.json()

print(json.dumps(data, indent=4))