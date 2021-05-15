import ELO
import json
import requests
from trueskill import Rating



def main():

    #ELO.AddPlayer('Ozzy','lololol')

    r1 = Rating(100.0, 100.0/3.0)
    print(r1)

    response = ELO.requestMatchData("3903754259")

    
    with open('players.json', 'r') as f:
        data = json.load(f)
        ELO.write_json(data,'players_old.json')
        #for player in data['players']:
           # player['Bungo'] = (100.0/3.0)
        f.close()



    with open('players.json', 'w') as f:
        json.dump(data, f, indent = 4)
        f.close()

if __name__ == "__main__":
    main()