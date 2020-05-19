from random import choice,randint
import random
import json
homme=['Michel','Didier','Patrick','Franck','Marc','Bernard','Richard','François','Pierre','Théo','Thomas','Emmanuel','Laurent','Gabriel','Raphaël','Louis','Lucas','Hugo','Benoit','Jules','Adam','Arthur','Ethan','Paul','Nathan','Antoine','Enzo','Noé','Victor','Valentin','Clément','Baptiste','Rayan','Samuel','Maxime','Maxence','Gaspard','Elliot','Alexandre','Mathieu','Mathéo','Rémi']
femme=['Claire','Emma','Jade','Alice','Louise','Chloé','Lina','Léa','Rose','Anna','Inès','Ambre','Julie','Julia','Léna','Manon','Juliette','Capucine','Mathilde','Anaïs','Yasmine','Lisa','Elsa','Noémie','Zoé','Camille','Lou','Lola','Lucie','Jeanne','Marie','Roxane','Adèle','Sofia','Maya','Clémence','Margot','Laura','Océane','Sarah','Salomé','Emmy','Candice','Juliette']
nom=['Capet-Virbel','Devers','Dupuis','Laroche','Martin','Bernard','Durand','Dubois','Moreau','Prevost','Lemoine','Gaillard','Fournier','Bonnet','Dupont','Girard','Nickels','Leclerc','Lambert','Marchal','Leblanc','Leveque','Breton','Rodriguez','Garnier','Mercier','Garcia','Collin','Dumont','Lemaire','Lapetre','Ossart','Regent','Tran','Dejoue','Chaplain','Marques','Naudot','Chalumeau','Dufourt']

file='a_voir/user.json'   

var={}

def mdp():
    mot=str()
    for o in range(6):
        if choice(['number','lettre']) is'number':
            mot+=str(randint(0,9))
        else:
            mot+=choice(list(map(chr, range(97, 113))))
    return mot

for loop in range(1,500):
    name=choice(homme) or choice(femme)
    surname=choice(nom)

    data={
        "name":name,
        "surname":surname,
        "age":randint(13,18),
        "mdp":mdp(),
        "emprunts_actuels":0
    }
    var[name.casefold()+'_'+surname.casefold()]=data

var["dov_devers"]={
        "name":"Dov",
        "surname":"Devers",
        "age":17,
        "mdp":"dovdevers",
        "emprunts_actuels":0
    }
var["ysilde_capet-virbel"]={
        "name":"Ysilde",
        "surname":"Capet-Virbel",
        "age":17,
        "mdp":"ysilde",
        "emprunts_actuels":0
    }

with open('non_implemente/user/user.json', 'w') as outfile:
    json.dump(var, outfile)
    outfile.close()
    print('Terminé')