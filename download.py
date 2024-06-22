import requests

URL = 'https://i.pinimg.com/originals/95/35/4b/95354b272e88562a97642eb381c6c191.jpg'

response = requests.get(URL, stream=True)

if response.status_code == 200:
    with open('./images/image.png', 'wb') as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)