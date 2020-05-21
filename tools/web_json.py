import isbnlib,requests
from os import path
from tools.data_isbn import newjson
#######################################
data={'Title':'','Authors':'','Publisher':'','Year':''}
img=str()
synopsis=str()
#######################################
def write_img(url,ISBN):
    # url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('img/{}.jpg'.format(ISBN), 'wb').write(r.content)
    return 'img/{}.jpg'.format(ISBN)
#######################################
def get_data(ISBN):
    # global synopsis
    '''
    On récupère les données d'un livre sur google Books
    (Titre, Auteur(s), synopsis, Editeur, date de plublication, image de couverture)
    openl,goob
    '''
    book = isbnlib.meta(ISBN)   #on récupère les informations suivantes : Titre, Auteur(s), Editeur, date de plublication, langue
    synopsis=isbnlib.desc(ISBN) #on récupère la description du livre
    url=isbnlib.cover(ISBN)     #on récupère le lien de l'image de couverture
    if url=={}:                 #si on n'a pas récupéré d'image, on applique l'image par défaut
        img='img/no_img.jpg'
    else:
        url=url['thumbnail']
        img=write_img(url,ISBN) #on écrit l'image

    return book,synopsis,img    #on retourne les informations obtenues
#######################################
def search(ISBN):
    '''
    Cette méthode va chercher, grâce au moteur de recherche inclus dans ISBNLIB, les informations utiles du livre.
    Si aucun livre n'a pu être trouvé, il retourne une erreur et des listes vides.
    '''
    global data,synopsis,img
    ajoute=False
    if path.isfile('data/livres/{}.json'.format(ISBN)):
        ajoute= 'existe'
    else:
        try:
            data,synopsis,img=get_data(ISBN) # lancement de la méthode get_data(ISBN) qui va récupérer les informations
            ajoute=newjson(data['ISBN-13'],data['Title'],data['Authors'],
                        synopsis.replace('\n',' '),img,data['Publisher'],data['Year'],data['Language']) #on écrit les données

        except isbnlib.dev._exceptions.NoDataForSelectorError: #problème pour récupérer les données
            print('Pas de données, veuillez écrire les données manuellement ou donner un autre ISBN')
        except isbnlib.dev._exceptions.ISBNLibURLError: #problème d'internet
            print('Veuillez vérifier votre connexion internet')
        except isbnlib._exceptions.NotValidISBNError: # ISBN invalide
            print('Veuillez rentrer un ISBN valide')
    return ajoute,data,img,synopsis
