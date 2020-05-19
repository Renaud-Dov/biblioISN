import tkinter as tk
from tkinter import font,messagebox
from PIL import Image, ImageTk
from tools.book import readinfo
from tools.note import moy_note

root=tk.Tk()
root.configure(bg='red')
root.geometry('1000x1000')
root.resizable(False,False)

import tools.font as Font_perso

Panel=tk.Frame(root,bd=5,bg='white')
Panel.pack(expand=tk.YES)
info1=tk.Frame(Panel,bg='white')
info2=tk.Frame(Panel,bg='white')
info1.grid(row=0,column=0,sticky='n')
info2.grid(row=0,column=1,sticky='n')

def fermer():
    pass

###################################################
ISBN="9780140446456"
book,avis=readinfo(ISBN)
note,note_img=moy_note(avis['Notes'])
###################################################
photo=ImageTk.PhotoImage(Image.open('img/{}.jpg'.format(ISBN)))
star=ImageTk.PhotoImage(Image.open('img/stars/{}.jpg'.format(str(note_img).replace('.',','))))
author=str()
for o in book["Auteur"]:
    author+=o+', '  
author=author[0:-2]
for i in range(len(book['Synopsis'])):
        if i%100==0 and i!=0: #si multiple de 45 caractères
            book['Synopsis']=book['Synopsis'][0:i]+'\n'+book['Synopsis'][i:len(book['Synopsis'])]
###################################################
tk.Label(info1,text=book['Titre'],font=Font_perso.title2_font,bg='white').grid(row=0,column=0,pady=5)
tk.Label(info1,text='Par : {}'.format(author),font=Font_perso.tt_font2,bg='white').grid(row=1,column=0)
tk.Label(info1,text=book['Synopsis'],font=Font_perso.tt_font1,justify='left',bg='white').grid(row=2,column=0,pady=15,padx=15)
###################################################
tk.Button(info2,command=fermer,text='Fermer',font=Font_perso.tt_font,relief='ridge',borderwidth=5,bg='white',width=12).grid(row=0,column=0,pady=15)
tk.Label(info2,image=photo).grid(row=1,column=0,pady=10)
tk.Label(info2,text='ISBN: {}\nAnnée: {}\nLangue: {}\nNote:{}/5'.format(ISBN,book['year'],book['language'],round(note,2))
                        ,justify='left',fg='grey',bg='white').grid(row=2,column=0,pady=5,padx=10)
tk.Label(info2,image=star,bd=0).grid(row=3,column=0,pady=5)




root.mainloop()