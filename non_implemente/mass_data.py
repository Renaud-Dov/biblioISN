import web_json as w
import isbnlib
def test():
    while True:
        ajoute,data,img,sypnosis=w.launch(input('ISBN :'))
        print(ajoute,data,img,sypnosis[0:30])
        del ajoute
        del data 
        del img
        del sypnosis

test()