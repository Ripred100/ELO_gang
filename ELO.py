import json
import requests


def write_json(new_data, filename='players.json'):
    with open(filename, 'w') as file:
        json.dump(new_data, file, indent = 4)


def AddPlayer(Name, IGN, filename='players.json'):

    Dict = dict([('name', Name), ('ign', IGN), ('IQ', 100.0), ('Bungo', 100.0/3.0)])
    print(Dict)

    with open(filename) as f:
        data = json.load(f)
        temp = data['players']
        temp.append(Dict)
        f.close()

    write_json(data)

def requestMatchData(GameID, APIKey="RGAPI-cbb98062-5c17-4480-92e7-77b8929052c3"):
    URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + GameID + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response







