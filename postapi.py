#import requests 
#url = "https://reqres.in/api/register"

#response = requests.post(url)
#print(response)
import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())


