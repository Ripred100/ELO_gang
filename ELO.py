import json

def expected(eloA, eloB):


    Expo = (eloB - eloA)/400 
    AWin = 1.0/(1.0 + (10.0**Expo))

    return AWin


def write_json(new_data, filename='players.json'):
    with open(filename, 'w') as file:
        json.dump(new_data, file, indent = 4)


def AddPlayer(Name, IGN, filename='players.json'):

    Dict = dict([('name', Name), ('ign', IGN), ('ELO', 1500)])
    print(Dict)

    with open(filename) as f:
        data = json.load(f)
        temp = data['players']
        temp.append(Dict)
        f.close()

    write_json(data)





