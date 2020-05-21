import json
from tools.date import date_today,date_add
# from tools.connection import read_emprunt
#################################################
def writefile(variable,name):
    '''
    On enregistre les données du fichier
    '''
    with open('data/{}.json'.format(name), 'w') as outfile:
        json.dump(variable, outfile)
#################################################
def reservation_read(ISBN):
    with open('data/reservation.json','r') as outfile:
        var=json.load(outfile)
    date=var[ISBN]['to']
    return date
    
#################################################
def reservation_add(ISBN,time,name):
    """Méthode de réservation  via l'ISBN d'un livre, qui nécéssite le nom, le prénom de l'utilisateur
    time -> Temps en jours de réservation du livre
    """
    reserve=False

    data={
            "from":date_today(),
            "to":date_add(time),
            "Name":name
        }
    with open('data/reservation.json','r') as outfile:
        var=json.load(outfile)
        var[ISBN]=data
        outfile.close()
        writefile(var,'reservation')
    with open('data/livres/{}.json'.format(ISBN),'r') as outfile:
        var2=json.load(outfile)
        var2['Book']['taken']=True
        outfile.close()
        writefile(var2,'livres/{}'.format(ISBN))
        reserve=True
    return reserve

# def reservation_add_user(ISBN,time,username):
#     reserve=False
#     if read_emprunt(username)<=3:
#         data={
#                 "from":date_today(),
#                 "to":date_add(time),
#                 "Name":username
#             }
#         with open('data/reservation.json','r') as outfile:
#             var=json.load(outfile)
#             var[ISBN]=data
#             outfile.close()
#             writefile(var,'reservation')
#         with open('data/user.json','r') as outfile:
#             var=json.load(outfile)
#             var[username]['emprunts_actuels']+=1
#             writefile(var,'user')
#         with open('data/livres/{}.json'.format(ISBN),'r') as outfile:
#             var2=json.load(outfile)
#             var2['Book']['taken']=True
#             outfile.close()
#             writefile(var2,'livres/{}'.format(ISBN))
#             reserve=True
#     return reserve
#################################################
def reservation_del(ISBN):
    '''
    Retire le livre. Retourne True si le livre a été retiré
    '''
    with open('data/reservation.json','r') as outfile:
        var=json.load(outfile)
    if ISBN in var:
        del var[ISBN]
        outfile.close()
        writefile(var,'reservation')
        with open('data/livres/{}.json'.format(ISBN),'r') as outfile:
            var2=json.load(outfile)
            var2['Book']['taken']=False
            outfile.close()
            writefile(var2,'livres/{}'.format(ISBN))
        return True # le livre a été retiré
    else:
        return False #le livre n'a pas été retiré

def reservation_data(ISBN):
    '''
    Retourne toutes les réservations (Dictionnaire)
    '''
    with open('data/reservation.json','r') as outfile:
        var=json.load(outfile)
    return var[ISBN]
def reservation_state(ISBN):
    '''
    Cette méthode checke si le livre est emprunté
    '''
    with open('data/reservation.json','r') as outfile:
        var=json.load(outfile)
    return ISBN in var