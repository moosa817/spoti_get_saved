import requests,base64
from config import *
def liked(access_code):

    


    client_creds = f"{client_id}:{client_secret}"
    client_creds_bs64 = base64.b64encode(client_creds.encode())



    token_url = "https://accounts.spotify.com/api/token"
    method = "POST"
    token_data = {
        "grant_type":"client_credentials"
    }
    header = {
        "Authorization": f"Basic {client_creds_bs64.decode()}"
    }
    data = {
    'grant_type': 'authorization_code',
    'code': access_code,
    'redirect_uri': 'http://localhost:8000'
    }

    r = requests.post(token_url,data=data,headers=header)
    print(r.text)
    # repsonse1 = r.json()
    
    # token1 = repsonse1["access_token"]
    # token2 = repsonse1["refresh_token"]
    # # S = []
    # # print(r.text)
    # sauce = "https://api.spotify.com/v1/me/tracks?offset=0&limit=50"

    # a = token1
    # header = {
    #     "content_type": "appliaction/json",
    #     "Authorization": f"Bearer {a}",
        
    # }


    # r = requests.get(sauce,headers=header)
    # S = []
    
    # stuff = r.json()
    # # print(stuff["next"])
    # for k in range(0,len(stuff["items"])):
    #     S.append(stuff["items"][k]["track"]["name"])

    # a = []

    # while stuff["next"]!=None:
    #     sauce = stuff["next"]
    #     r = requests.get(sauce,headers=header)
    #     stuff = r.json()
    #     O = stuff["items"]
    #     for k in range(0,len(O)):
    #         artist = O[k]["track"]["artists"][0]["name"]
    #         song = stuff["items"][k]["track"]["name"]
    #         P = song + artist
    #         S.append(P)


    return "S"

# print(liked("AQAPLUAOn3tbMU7_ASlSAWwwdr6dsb0oOR2p8i7iubgYNw_fNT_LcXi2GwEl3KoP-8c8fXhz5hQhVUwC7L69LnfK6AugJCi26LxrBExdXw_-OxlmrSWquQZPVTGD9dr8EjLh9qp7S5XBG0IQNpzkpm2TNdBKaHktLKl8ossD7VeZicxnYa-FLos4Ldk"))