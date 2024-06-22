import requests

URL = 'https://randomuser.me/api/'

params = {
    'results': '100'
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    payload = response.json()
    
    results = payload.get('results')
    
    print(len(results))
    
    for user in results:
        name = user.get('name')
        print(f"{name['title']} {name['first']} {name['last']}")
        print("{title} {first} {last}".format(**name))