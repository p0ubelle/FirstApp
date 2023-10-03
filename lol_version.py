
import requests

def get_lol_version():
    link = 'https://ddragon.leagueoflegends.com/api/versions.json'
    resp = requests.get(link)

    lol_version = resp.json(); vs = lol_version[0] #[:-2]
    
    return vs  #.replace(".", "-")
