import json
def bytitle(texte):
    result=[]
    with open('data/title.json', 'r') as outfile:
        var=json.load(outfile)
        for key,value in var.items():
            if texte.casefold() in value.casefold():
                result.append(key)
    return result

def byauthor(texte):
    result=[]
    with open('data/authors.json', 'r') as outfile:
        var=json.load(outfile)
        for key,value in var.items():
            for o in value:
                if texte.casefold() in o.casefold():
                    result.append(key)
    return result

def recherche(data,nb):
    resultats=[];liste=[]
    data=data.split(' ') #on sépare tous les mots dans une liste
    for o in data: #pour chaque mot on cherche...
        resultats+=bytitle(o) #...dans les titres
        resultats+=byauthor(o) #...dans les auteurs

    resultats=list(set(resultats)) #supprime les doublons
    for i in range(0,len(resultats),nb): #création de la liste découpée
        liste.append(resultats[i:i+nb])
    return resultats,liste

def data(ISBN):
    with open('data/livres/{}.json'.format(ISBN), 'r') as outfile:
        var=json.load(outfile)
        title=var['Book']['Titre']
        auteur=var['Book']['Auteur']
        synopsis=var['Book']['Synopsis']
        image=var['Book']['img']
        disponible=var['Book']["taken"]
    return [ISBN,title,auteur,synopsis,image,disponible]