import requests

url = "http://172.105.87.133:3160/hello"

response = requests.get(url)

print(response)
print(response.content)



