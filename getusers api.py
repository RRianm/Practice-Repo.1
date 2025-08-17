# import requests

# url = "https://api.freeapi.app/api/v1/public/randomusers"

# def get_users():
#     response = requests.get(url)
#     print(response)

#     if response.status_code == 200:
#         user_response = response.json()
#         info = user_response["data"]["data"]
#         info_number = info[5]
#         gender = info_number["gender"]
#         first_name = info_number["name"]["first"]
#         last_name = info_number["name"]["last"]
#         return gender, first_name, last_name
#     else:
#         print("Error")


# information = get_users()

# if information:
#     gender, first_name, last_name = information
#     print(f"gender: {gender}")
#     print(f"first name: {first_name}")
#     print(f"last name: {last_name}")
        
# else:
#     print("another error")


import requests


def get_playlist():

    url = "https://api.freeapi.app/api/v1/public/youtube/playlists"
    response = requests.get(url)
    if response.status_code == 200:
        got_playlist = response.json()
        info = got_playlist["data"]["data"]
        get_standards = info[0]
        url = get_standards["snippet"]["thumbnails"]["standard"]["url"]
        height = get_standards["snippet"]["thumbnails"]["standard"]["height"]
        width = get_standards["snippet"]["thumbnails"]["standard"]["width"]
        return url, height, width
    else:
        print("error")

information =get_playlist()
if information:
    url, height, width = information
    print(f"Url: {url}")
    print(f"height: {height}")
    print(f"width: {width}")
else:
    print("new error")
        



    

