import json
from os import remove,path
from tkinter import messagebox
from tools.date import date_today
from tools.write_data import title_data, author_data,data_del
def writefile(variable,ISBN):
    '''
    On enregistre les données du fichier
    '''
    with open('data/livres/{}.json'.format(ISBN), 'w') as outfile:
        json.dump(variable, outfile)
        outfile.close()

def newjson(ISBN,title,authors,sypnosis,img,publisher,year,language):
    '''
    On vient lire le ficher json en local et on le transforme en dictionnaire python...
    Nous intégrons alors les nouvelles informations dans dict(), puis lancons le programme writefile()
    afin de modifier le fichier.
    '''
    data ={"Book":{
            "Titre": title,
            "Auteur": authors,
            "Synopsis":sypnosis,
            "publisher":publisher,
            "year":year,
            "language":language,
            "img":img,
            "added":date_today(),
            "taken":False
            },
        "Notes":{"1": 0,"2": 0,"3": 0,"4": 0,"5": 0},
            
        }
    writefile(data,ISBN)
    title_data(ISBN,title)
    author_data(ISBN,authors)
    return True

def deljson(ISBN):
    '''
    On vient supprimer le livre à l'ISBN correspondant
    '''
    if not path.isfile('data/livres/{}.json'.format(ISBN)):
        messagebox.showerror('Erreur',"Vous n'avez pas rentré d'ISBN")
    else:
        data_del(ISBN) #on supprime l'ISBN des datas title & authors
        try:
            remove('img/{}.jpg'.format(ISBN)) #on supprime l'image
        except FileNotFoundError:
            pass
        remove('data/livres/{}.json'.format(ISBN)) #on supprime le fichier json
        messagebox.showinfo('Terminé','Le livre a été correctement supprimé de la bibliothèque')


'''
La partie ci dessous en commentaire correspond à l'ancien code de ce fichier
'''
################################################################################################################################
################################################################################################################################
################################################################################################################################
# import json
# from tkinter import messagebox
# from tools.date import date_today
# from write_data import title_data, author_data
# from os import remove

# def writefile(variable):
#     '''
#     On enregistre les données du fichier
#     '''
#     with open('data/base.json', 'w') as outfile:
#         json.dump(variable, outfile)
#         outfile.close()
#     title_data()
#     author_data()
    

# def newjson(ISBN,title,Authors,sypnosis,img,publisher,year,language):
#     '''
#     On vient lire le ficher json en local et on le transforme en dictionnaire python...
#     Nous intégrons alors les nouvelles informations dans dict(), puis lancons le programme writefile()
#     afin de modifier le fichier.
#     '''
#     data ={
#                     "Titre": title,
#                     "Auteur": Authors,
#                     "Synopsis":sypnosis,
#                     "publisher":publisher,
#                     "year":year,
#                     "language":language,
#                     "img":img,
#                     "added":date_today(),
#                     "taken":False
#                 }
                
#     with open('data/base.json', 'r') as outfile:
#         var=json.load(outfile)

#         if ISBN in var['livre']: #si l'ISBN est déja présent dans la liste
#             return 'existe'
#         else: #L'ISBN n'est pas présent dans la liste
#             var['livre'][ISBN]=data #on rajoute en ISBN (key) la data (value)
#             outfile.close() #on ferme le fichier
#             writefile(var) #on lance la méthode d'écriture de fichier
#             return True


# def deljson(ISBN):
#     '''
#     On vient supprimer le livre à l'ISBN correspondant
#     '''
#     with open('data/base.json', 'r') as outfile:
#         var=json.load(outfile)
#         name=str()
#         if ISBN in var['livre']: #si l'ISBN est présent dans la liste
#             name=var['livre'][ISBN]['Titre']
#             del var['livre'][ISBN] # on le supprime
#             outfile.close() #on ferme le fichier
#             writefile(var) #on lance la méthode d'écriture de fichier
#             remove('img/{}_{}.jpg'.format(name.replace(' ','_'),ISBN)) #on supprime l'image
#             return True

#         else: #L'ISBN n'est pas présent dans la liste
#             messagebox.showerror('Erreur','ISBN non présent')
#             return False

