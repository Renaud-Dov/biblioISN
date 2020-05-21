from math import floor
def moy_note(liste):
    #{"1": 0,"2": 0,"3": 0,"4": 0,"5": 0}
    try:
        note=(liste["1"]+liste["2"]*2+liste["3"]*3+liste["4"]*4+liste["5"]*5)/(liste["1"]+liste["2"]+liste["3"]+liste["4"]+liste["5"])
    except ZeroDivisionError:note=0
    return note,note_img(note)
# print(moy_note({"1": 5,"2": 1,"3": 4,"4": 5,"5": 14}))

def note_img(note):
    '''
    Cette méthode permet d'arrondir la note
    afin de choisir la bonne image dans les fiches
    '''
    if note-float(floor(note))>0.5:note=float(floor(note))+0.5
    else:note=float(floor(note))
    return note