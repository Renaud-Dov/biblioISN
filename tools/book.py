import json
def readinfo(ISBN):
    '''
    Retourne les informations d'un livre à partir de son ISBN
    '''
    with open('data/livres/{}.json'.format(ISBN),'r') as outfile:
        var=json.load(outfile)
        return var['Book'],var['Notes']
def titlefromISBN(ISBN):
    '''
    Retourne le titre d'un livre grâce à l'ISBN
    '''
    with open('data/title.json'.format(ISBN),'r') as outfile:
        var=json.load(outfile)
        return var[ISBN]
# print(read('9780140446456'))