import requests
from lol_version import get_lol_version

api_key="RGAPI-5459bfa7-3738-47e6-a20b-bfea5a039644"


def get_summoner_info(sum_name="QiyanaEqual FF15", region="euw1", api_key=api_key):
    # Get summoner info
    api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{sum_name}?api_key={api_key}"
    sum_name_resp = requests.get(api_url)

    if sum_name_resp.status_code == 403:
        print("change api key")
        return None, sum_name

    if sum_name_resp.status_code == 200:
        sum_info = sum_name_resp.json()
        
        if 'id' in sum_info:
            # get summoner ranks
            sum_puuid = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{sum_info['id']}?api_key={api_key}"
            sum_puuid_resp = requests.get(sum_puuid)
            
            if sum_puuid_resp.status_code == 200:
                summoner_ranks = sum_puuid_resp.json()



                # find rank in soloQ only
                desired_rank = None
                for rank in summoner_ranks:
                    if rank["queueType"] == "RANKED_SOLO_5x5":
                        desired_rank = rank
                        break
                

                # sum icon
                icon_id = sum_info["profileIconId"]
                icon_url = f"https://ddragon.leagueoflegends.com/cdn/{get_lol_version()}/img/profileicon/{icon_id}.png"



                return desired_rank, sum_name, icon_id
    
    # return None if api fail
    return None, sum_name






