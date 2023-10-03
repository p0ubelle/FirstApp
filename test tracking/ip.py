from requests import get


ip = get('https://api.ipify.org').content.decode('utf8')
print("My public IP address is", ip)


req = get(f"https://ipapi.co/{ip}/json/")
test = req.json()


print(test)