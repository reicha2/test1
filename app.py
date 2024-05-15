import requests

response = requests.get('https://www.ynet.co.il')
print(response.text)
