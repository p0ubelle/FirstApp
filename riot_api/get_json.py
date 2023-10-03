import os
import requests


os.system("cls")

api_key = "RGAPI-5e181f00-7cf5-4cf1-9d71-0113d29ed54c"
def get_sum_id(sum_name):
    api_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{sum_name}"
    return api_url



api_url = get_sum_id(input("name : ")) + "?api_key=" + api_key
resp = requests.get(api_url)

sum_info = resp.json()


for key, value in sum_info.items():
    print(f'"{key}":"{value}"')






