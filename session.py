import requests
from getpass import getpass

URL = 'https://httpbin.org/basic-auth/roman/1234'

password = getpass('Ingresa la contraseña: ')

session = requests.Session()
session.auth = ('roman', password)

response = session.get(URL)

if response.status_code == 200:
    print(response.text)
    
if response.status_code == 401:
    print('Unsuccessful authentication')