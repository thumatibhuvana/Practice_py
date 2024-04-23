import requests
api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)
resp = response.json()
print(resp)
print(response.status_code)


data = {
    "title":"New post",
    "body":"New post created",
    "UserID":1
}
response1 = requests.post(api_url, data=data)
print(response1.status_code)
response2 = requests.get(api_url)  #Here we are not getting what we passed becoz of dummy api_url but in real time passed data will appear
resp1 = response2.json()
print(resp1)
