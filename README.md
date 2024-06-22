Curl es una herramienta de línea de comandose en donde, entre muchas otras cosas, se pueden mandar peticiones HTTP. Y la página [httpbin](https://httpbin.org/#/HTTP_Methods) hace echo de las peticiones que le llegan, httpbin.org/get y httpbin.org/post para los verbos respectivos.


curl https://httpbin.org/get   
Por defecto se hacen peticiones get

```
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.81.0",
    "X-Amzn-Trace-Id": "Root=1-6675f44a-4b5d6e374d78e539628f49d6"
  },
  "origin": "181.209.89.84",
  "url": "https://httpbin.org/get"
}
```

curl "https://httpbin.org/get?name=Pepe&course=Python"  
Si mandamos queryparams podemos ver que se mandan en args

```
{
"args": {
"course": "Python",
"name": "Pepe"
},
"headers": {
"Accept": "_/_",
"Host": "httpbin.org",
"User-Agent": "curl/7.81.0",
"X-Amzn-Trace-Id": "Root=1-6675f629-650d425003587c224f6a60ed"
},
"origin": "181.209.89.84",
"url": "https://httpbin.org/get?name=Pepe&course=Python"
}
```


curl "https://httpbin.org/get?name=Pepe" -H "Accept: application/json"  
Para mandar algún header(s) se usa la opción -H

```
{
"args": {
"name": "Pepe"
},
"headers": {
"Accept": "application/json",
"Host": "httpbin.org",
"User-Agent": "curl/7.81.0",
"X-Amzn-Trace-Id": "Root=1-6675f818-5fb4015677914147693f9a6d"
},
"origin": "181.209.89.84",
"url": "https://httpbin.org/get?name=Pepe"
}
```

curl "https://httpbin.org/get?name=Pepe" -H "Accept: application/json" -i  
Con la opción -i vemos la cabecera y el cuerpo de la respuesta

```
HTTP/2 200
date: Fri, 21 Jun 2024 22:02:42 GMT
content-type: application/json
content-length: 300
server: gunicorn/19.9.0
access-control-allow-origin: \*
access-control-allow-credentials: true

{
"args": {
"name": "Pepe"
},
"headers": {
"Accept": "application/json",
"Host": "httpbin.org",
"User-Agent": "curl/7.81.0",
"X-Amzn-Trace-Id": "Root=1-6675f882-0b3106cf1cfd61ed7511257b"
},
"origin": "181.209.89.84",
"url": "https://httpbin.org/get?name=Pepe"
}
```
curl -X POST "https://httpbin.org/post"  
Con la opción -X seleccionamos el tipo de petición

```
{
"args": {},
"data": "",
"files": {},
"form": {},
"headers": {
"Accept": "_/_",
"Host": "httpbin.org",
"User-Agent": "curl/7.81.0",
"X-Amzn-Trace-Id": "Root=1-6675fbef-2ef05d167155eefd6dc62952"
},
"json": null,
"origin": "181.209.89.84",
"url": "https://httpbin.org/post"
}
```

curl -X POST "https://httpbin.org/post" -d '{"username": "Pepe", "email":"pepe@gmail.com"}'  
Con la opción -d podemos mandar datos que se ven en el form

```
{
"args": {},
"data": "",
"files": {},
"form": {
"{\"username\": \"Pepe\", \"email\":\"pepe@gmail.com\"}": ""
},
"headers": {
"Accept": "_/_",
"Content-Length": "46",
"Content-Type": "application/x-www-form-urlencoded",
"Host": "httpbin.org",
"User-Agent": "curl/7.81.0",
"X-Amzn-Trace-Id": "Root=1-6675fd79-3bbb19f501357158587ccdcc"
},
"json": null,
"origin": "181.209.89.84",
"url": "https://httpbin.org/post"
}
```