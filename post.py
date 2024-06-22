import requests 

URL = 'https://httpbin.org/post'

data = {
    'username': 'roman',
    'password': '123456'
}

params = {
    'platform': 'test'
}

headers = {
    'course': 'Curso de Python',
    'version': '2.0',
    'author': 'Namor'
}

response = requests.post(URL, data=data, headers=headers, params=params)

if response.status_code == 200:
    print(response.text)

    payload = response.json()

    print(payload)