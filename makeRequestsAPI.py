import requests

my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)

print(response)
palavras = response.json()

print (palavras[0])

