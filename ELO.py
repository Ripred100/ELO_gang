import json
import requests


#takes python dictionary and writes it to the json file
def write_json(new_data, filename='players.json'):
    with open(filename, 'w') as file:
        json.dump(new_data, file, indent = 4)


#this function takes a name and an ign and adds the player to the players.json file
def AddPlayer(Name, IGN, filename='players.json'):

    #default ranking values of skill (IQ)=100, and skill confidence (Bungo)=33.3
    Dict = dict([('name', Name), ('ign', IGN), ('IQ', 100.0), ('Bungo', 100.0/3.0)])
    print(Dict)

    with open(filename) as f:
        data = json.load(f)
        temp = data['players']
        temp.append(Dict)
        f.close()

    write_json(data)

#playing with Riot API
#takes a game ID and returns a bunch of data in the form of a json file
def requestMatchData(GameID, APIKey="RGAPI-cbb98062-5c17-4480-92e7-77b8929052c3"):#please don't steal my API key :)
    URL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + GameID + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response







