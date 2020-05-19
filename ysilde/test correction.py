import tkinter as tk
from PIL import Image, ImageTk

fenetre=tk.Tk()

from tools.font import *

def valider(event):
    print(True)


fenetre.geometry('800x400') #taille de la fenêtre
fenetre.resizable(False,False) #on peut pas redimensionner
fenetre.title('Test rectangle')
fenetre.configure(bg='red')

panel=tk.Frame(fenetre,cursor='hand1')
panel.pack(expand=tk.YES)
###################################################################
#Infos test
ISBN='025846231548623'
title="Titre de l'oeuvre"
author="auteur"
desc="description description description description description description description"
image=ImageTk.PhotoImage(Image.open('9780525555353.jpg'))
###################################################################

'''
Pas besoin de mettre toutes les infos sur l'aperçu, il faut que ce soit compact.
Donc pas d'éditeur, ni d'année de publication

J'ai retiré les boutons réserver et fiche. Cliquer sur le frame suffira.

'''
def affichage():
    pass

infos=tk.Frame(panel)
infos.grid(row=0,column=1,sticky='n')

tk.Label(panel,image=image).grid(row=0,column=0)

tk.Label(infos,text= title,font=research_font).grid(row=0,column=0,padx=5,pady=10)
tk.Label(infos,text= author).grid(row=1,column=0)
tk.Label(infos,text=desc).grid(row=2,column=0)

for i in [panel,infos]:
    i.bind('<Button-1>',valider) #Clic gauche

fenetre.mainloop()
