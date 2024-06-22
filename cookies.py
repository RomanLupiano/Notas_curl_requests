import requests

URL = 'https://httpbin.org/cookies'


cookies = {
    'session': 'abc123',
    'name': 'Roman',
    'email': 'roman@gmail.com'
}

response = requests.get(URL, cookies=cookies)

if response.status_code == 200:
    print(response.text)