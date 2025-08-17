import requests

url = "https://api.freeapi.app/api/v1/public/randomusers"

def getuserid(userId):
    
    baseurl = f"{url}/{userId}"
    response = requests.get(baseurl)
    print(response)
    
    if response.status_code == 200:
        data = response.json()
        super_data = data["data"]
        first_name = super_data["name"]["first"]
        country = super_data["location"]["country"]
        city = super_data["location"]["city"]
        return first_name, country, city

    else:
        print("error")


Get_the_id = int(input("Enter the id: "))
information = getuserid(Get_the_id)


if information:
    first_name, country, city = information
    print(f"first name: {first_name}")
    print(f"Country: {country}")
    print(f"City: {city}")
else:
    print("new error")


    

