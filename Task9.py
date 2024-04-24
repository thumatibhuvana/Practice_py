#1st
import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)
resp = response.json()
print(resp)
print(response.status_code)

#2nd
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


#3rd
def get_all_data(api_url):
    response3 = requests.get(api_url)
    resp3 = response3.json()
    return resp3

resp3 = get_all_data("https://jsonplaceholder.typicode.com/todos")
print(resp3)



#4rth
def get_all_data_by_id(api_url, id):
    response4 = requests.get(f"{api_url}/{id}")
    resp4 = response4.json()
    return resp4


resp4 = get_all_data_by_id("https://jsonplaceholder.typicode.com/todos", 2)
print(resp4)


#5th
def save_data(d):
        with open('text2.txt', 'a') as af:
            d1 = str(d)
            af.write(d1)
            af.write('\n')
            return af

a = save_data(resp4)
print(a)



#6th
data = {
    "title":"Test",
    "completed":"true",
    "id":10000,
    "userId":10000
}
response7 = requests.post(api_url, data=data)
print(response7.status_code)
resp8 = get_all_data_by_id(api_url,10000)
print(resp8)

