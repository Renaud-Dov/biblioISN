import json
def bytitle(mot):
    '''
    Recherche par titre
    '''
    result=[]
    with open('data/title.json', 'r') as outfile:
        var=json.load(outfile)
        for key,value in var.items():
            if mot.casefold() in value.casefold(): #casefold -> minuscule
                result.append(key)
    return result

def byauthor(mot):
    result=[]
    with open('data/authors.json', 'r') as outfile:
        var=json.load(outfile)
        for key,value in var.items():
            for o in value:
                if mot.casefold() in o.casefold(): #casefold -> minuscule
                    result.append(key)
    return result

def recherche(data,nb):
    resultats=[];liste=[]
    data=data.split(' ') #on sépare tous les mots dans une liste
    for o in data: #pour chaque mot on cherche...
        resultats+=bytitle(o) #...dans les titres
        resultats+=byauthor(o) #...dans les auteurs

    resultats=list(set(resultats)) #supprime les doublons ->set()
    for i in range(0,len(resultats),nb): #création de la liste découpée (en 6 la plupart du temps) EX :[[1,2,53,5,8,6],[9,7,5,6,8,2]]
        liste.append(resultats[i:i+nb]) #on découpe la liste en liste en x listes de nb ISBN (pour gérer les ISBN à afficher sur chaque page) 
    return resultats,liste

def data(ISBN):
    '''
    Récupère les données rapides pour l'affichage des minis fiches dans la barre de recherche
    '''
    with open('data/livres/{}.json'.format(ISBN), 'r') as outfile:
        var=json.load(outfile)
        title=var['Book']['Titre']
        auteur=var['Book']['Auteur']
        synopsis=var['Book']['Synopsis']
        image=var['Book']['img']
        disponible=var['Book']["taken"]
    return [ISBN,title,auteur,synopsis,image,disponible] #retour sous liste