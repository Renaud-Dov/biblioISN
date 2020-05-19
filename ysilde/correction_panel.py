import tkinter as tk
from PIL import Image, ImageTk

fenetre=tk.Tk()

from tools.font import *

def valider(ISBN):
    print(True,ISBN)


fenetre.title('Test rectangle')

fenetre.configure(bg='red')

###################################################################
#Infos test
info=[{'ISBN':'025846231548623','Title':"Titre sqsderfgtyde l'oeuvre",'Author':"auteur",'Synopsis':"description description description description description description description"},
        {'ISBN':'1154752154','Title':"sdcfvgbhy",'Author':"auteur",'Synopsis':"description description description description description description description"},
        {'ISBN':'4152','Title':"fgthyjukhngbv ce",'Author':"auteur",'Synopsis':"description description description description description description description"},
        {'ISBN':'52145862','Title':"Titre de l'oeuvre",'Author':"auteur",'Synopsis':"description description description description description description description"}]
image=ImageTk.PhotoImage(Image.open('9780525555353.jpg'))
###################################################################
panels=[0]*4

panels[0]=tk.Frame(fenetre,cursor='hand1')
panels[0].pack(pady=15)
panels[1]=tk.Frame(fenetre,cursor='hand1')
panels[1].pack(pady=15)
panels[2]=tk.Frame(fenetre,cursor='hand1')
panels[2].pack(pady=15)
panels[3]=tk.Frame(fenetre,cursor='hand1')
panels[3].pack(pady=15)

# print(panels)
###################################################################
def affichage(panel,information):
    infos=tk.Frame(panel)
    infos.grid(row=0,column=1,sticky='n')

    tk.Label(panel,image=image).grid(row=0,column=0)

    tk.Label(infos,text= information['Title'],font=research_font).grid(row=0,column=0,padx=5,pady=10)
    tk.Label(infos,text= information['Author']).grid(row=1,column=0)
    tk.Label(infos,text=information['Synopsis']).grid(row=2,column=0)

    for i in [panel,infos]:
        i.bind('<Button-1>',lambda e:valider(information['ISBN'])) #Clic gauche


for o in range(4):
    affichage(panels[o],info[o])
    panels[o].pack(pady=15)

fenetre.mainloop()