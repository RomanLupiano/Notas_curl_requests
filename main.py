import requests 

URL = 'https://httpbin.org/get'

response = requests.get(URL) #GET por defecto

print(response) #response type
print(response.status_code) #int
print(response.text)    #str

payload = response.json()

print(payload)  #dict
print(payload.get('origin'))



#Mandando parametros por queary en url
URLConParametros = 'https://httpbin.org/get?name=marcos&email=roman@gmail.com'

response = requests.get(URLConParametros)

if response.status_code == 200:
    payload = response.text 
    
    print(payload)



#Mandando parametros por diccionario en get()
params = {
    'name': 'roman',
    'email': 'marcos@gmail.com'
}
response = requests.get(URL, params=params)

if response.status_code == 200:
    payload = response.text 
    
    print(payload)