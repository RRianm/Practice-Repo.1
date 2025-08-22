import requests

url = "https://api.freeapi.app/api/v1/public/meals/meal/random"

def getameal():
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    print("Raw response:")
    print(response.text)

    try:
        data = response.json()
        codedata = data["data"]
        return codedata
    except Exception as e:
        print("Failed to parse JSON:", e)
        return None

instructions = getameal()

if instructions:
    print(f"\n🍽️  Your meal:\n{instructions}")
else:
    print("No meal found.")
