import requests
#
# url = 'http://localhost:8000/hello'
# response = requests.get(url)
#
# print(response)
# print(response.content)
#
#
# url_post = 'http://localhost:8000/file'
# data = {'file_name':  'alex_fisier'}
# headers = {'file_name': 'fisier'}
# response = requests.post(url_post, data, headers=headers)

url_put = 'http://localhost:8000/file'
headers = {'file_name': 'fisier', 'content': 'hello'}
requests.delete(url_put, headers=headers)



