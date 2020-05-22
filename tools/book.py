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


    # print(liste)
def edit_files(ISBN,data):
    with open("data/livres/{}.json".format(ISBN),'r') as outfile:
        var=json.load(outfile)
        outfile.close()
    var['Book']['Titre']=data[0]
    var['Book']['Auteur']=data[1]
    var['Book']['Synopsis']=data[2]
    var['Book']['publisher']=data[3]
    var['Book']['year']=data[4]
    var['Book']['language']=data[5]
    with open('data/livres/{}.json'.format(ISBN), 'w') as outfile:
        json.dump(var, outfile)
        outfile.close()

# edit_files('9791034732968',['test les lumières mon amour', ['Annie Lerrnaux'], 'Pendant unen effed rendez-voard.', 'Raconter la vie', '2015', 'fr'])