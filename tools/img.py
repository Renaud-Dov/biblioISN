from PIL import Image

def rezise(img,title,ISBN):
    '''
    Cette méthode a pour but de recadrer une image,
    importée par l'utilisateur qui souhaite rajouter un livre manuellement.
    '''
    img = Image.open(img) #on ouvre l'image
    # width, height = img.size
    new=img.resize((128,200)) #on la recadre
    new.save('img/{}.jpg'.format(ISBN)) #et on l'enregistre


# def open_img(img): #ouvrir une image
#     img=Image.open(img)
#     new=img.resize((480,800))
#     img.show()
# open_img('img/no_img.jpg')
# rezise('img/no_img.jpg','Titre','251662489523')