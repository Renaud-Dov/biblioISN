import json
########################################################################################
def data_del(ISBN):
    '''
    Supprime l'ISBN des datas title et authors
    '''
    with open('data/title.json', 'r') as outfile:
        var=json.load(outfile)
        del var[ISBN]
    with open('data/title.json','w') as outfile:
        json.dump(var, outfile)
    ############################################
    with open('data/authors.json', 'r') as outfile:
        var=json.load(outfile)
        del var[ISBN]
    with open('data/authors.json','w') as outfile:
        json.dump(var, outfile)
########################################################################################
def title_data(ISBN,title):
    '''
    Ajoute l'ISBN avec le titre dans title.json
    '''
    with open('data/title.json', 'r') as outfile:
        var=json.load(outfile)
        var[ISBN]=title
    with open('data/title.json','w') as outfile:
        json.dump(var, outfile)

def author_data(ISBN,authors):
    '''
    Ajoute l'ISBN avec le nom de l'auteur dans authors.json
    '''
    with open('data/authors.json', 'r') as outfile:
        var=json.load(outfile)
        var[ISBN]=authors
    with open('data/authors.json','w') as outfile:
        json.dump(var, outfile)

# import json
# def title_data():
#     data={}
#     with open('data/base.json', 'r') as outfile:
#         var=json.load(outfile)
#         for value in var['livre']:
#             # print(var['livre'][value]['Titre'],':',value)
#             data[var['livre'][value]['Titre']]=value
                
            
#     with open('data/title.json','w') as outfile:
#         json.dump(data, outfile)

# def author_data():
#     data={}
#     with open('data/base.json', 'r') as outfile:
#         var=json.load(outfile)
#         for key,value in var['livre'].items():
#             # print(key,value['Auteur'])
#             data[key]=value['Auteur']

#     with open('data/authors.json','w') as outfile:
#         json.dump(data, outfile)