#import requests

#url = "https://pokeapi.co/api/v2/"
#def pokeapi(name):
  #  pokeurl = f"{url}pokemon/{name}"
   # response = requests.get(pokeurl)
   # print(response)
   # if response.status_code == 200:
   #     data = response.json()
   #     return data
   # else:
    #    print("error")






#pokemon_name = "pikachu"
#info = pokeapi(pokemon_name)
#if info:
#    print(f"Name: {info["name"]}")
#    print(f"height: {info["height"]}")
#   print(f"id: {info["id"]}")
#   print(f"weight: {info["weight"]}")

#__________________________________________________________________________________-e

#mport requests

#base_url= "https://api.freeapi.app/api/v1/public/randomusers/user/random"

#def user_info():
# url=base_url
#  response= requests.get(url)
#  print(response)

# if response.status_code==200:
#    data=response.json()
#   user_data=data["data"]
#    user_name=user_data["name"]["first"]
#    country=user_data["location"]["country"]
#   return user_name,country

#  else:
#    print("Failed to fetch data")

#information=user_info()

#if information:
  #user_name,country=information
  #print(f"Name: {user_name}")
# _print(f"Country: {country}")

#________________________________________________________________________
import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

def getusername():
    response = requests.get(url)
    
    if response.status_code == 200:
        info = response.json()
        user_info = info["data"]
        username = info["data"]["name"]["first"]
        longitude = info["data"]["location"]["coordinates"]["longitude"]
        latitude = info["data"]["location"]["coordinates"]["latitude"]
        return username, longitude, latitude
    else: 
        print("failed to access data")

information = getusername()
if information:
    username, longitude, latitude = information
    print(f"Name: {username}")
    print("Current Coordinates:     ")
    print(f"Current longitude: {longitude}")
    print(f"Current Latidude: {latitude}")




