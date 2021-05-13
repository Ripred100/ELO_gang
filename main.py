import ELO
import json

with open('players.json', 'r') as f:
    data = json.load(f)
    old_data = data
    with open('players_old.json', 'w') as old:
        json.dump(old_data, old, indent = 4)
        old.close()
    for player in data['players']:
        player['Bungo'] = (100.0/3.0)
    f.close()



with open('players.json', 'w') as f:
    json.dump(data, f, indent = 4)
    f.close()