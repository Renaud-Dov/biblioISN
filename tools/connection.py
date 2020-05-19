import json
def connection(username,password):
    connecte=False
    with open('data/user.json', 'r') as outfile:
        var=json.load(outfile)
    if username in var:
        if var[username]['mdp']==password:
            connecte=True
    return connecte
    
def name(username):
    with open('data/user.json', 'r') as outfile:
        var=json.load(outfile)
    return var[username]["name"],var[username]["surname"]

def read_emprunt(username):
    with open('data/user.json', 'r') as outfile:
        var=json.load(outfile)
    return var[username]['emprunts_actuels']

# print(connection('dov_devers','dovdevers'))
# print(read_emprunt('dov_devers'))
