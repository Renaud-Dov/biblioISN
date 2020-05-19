import tkinter as tk
from tkinter import messagebox,font
from PIL import Image, ImageTk
import isbnlib,requests
import tools.web_json as web_json
from io import BytesIO
root=tk.Tk()

root.geometry('1400x900')
root.resizable(False,False)
root.title('Titre')
root.configure(bg='#8F98E2')
#########################################################
title1_font=font.Font(family='Calibri',size=25)
research_font=font.Font(family='Calibri',size=18)
tt_font=font.Font(family='Calibri',size=14,weight='bold')
tt_font1=font.Font(family='Calibri',size=12,slant='italic')

##################################################################################################################
left_panel=tk.Frame(root,bg='#B5BCF0',relief='raised')
left_panel.pack(fill=tk.Y,side=tk.LEFT)
right_panel=tk.Frame(root,bg='#8F98E2',relief='raised')
#########################################################
liste_decoupe=[]
value_entry = tk.StringVar()
pages_max=int()
#########################################################
def return_img(ISBN):
    try :
        img=isbnlib.cover(ISBN)['smallThumbnail']
    except:
        img='http://google.com/favicon.ico'
    print(img)
    return img
def return_data(ISBN):
    try:
        data=isbnlib.meta(ISBN)
        print('data')
    except:
        data={'ISBN-13':'Vide','Title':'Vide','Authors':['Vide'],'Language':'Vide','Publisher':'Vide','Year':'Vide'}
    try:
        data['synopsis']=isbnlib.desc(ISBN)
        print('synopsis')
    except:
        data['synopsis']='Vide'
    return data
#########################################################
def research(txt,types):
    global nb_resultats,liste_decoupe
    liste=[];liste_decoupe=[]

    if types=='goom':
        data=isbnlib.goom(txt)
        for o in data:
            liste.append(o['ISBN-13'])

    elif types=='editions':
        liste=isbnlib.editions(txt) #9782092543085

    nb_resultats.configure(text='Nombre de résultats: {}'.format(len(liste)))
    for i in range(0,len(liste),4):
        liste_decoupe.append(liste[i:i+4])

#########################################################
def valider(types):
    global nb_resultats,liste_decoupe,pages_max
    ############################
    txt=entry.get()
    if txt!=str():
        chargement_label.configure(text='Chargement')
        research(txt,types)
        if liste_decoupe!=[]:
            right_panel.pack(fill=tk.BOTH)
            pages_max=len(liste_decoupe) #nombre de pages nécéssaire pour afficher tous les résultats
            reinitialiser_recherche()
            affichage_resultats()
        else:
            chargement_label.configure(text='')
            messagebox.showerror('Erreur','Aucun résultat')
    else:
        messagebox.showerror('Erreur','Aucun terme rentré')
#########################################################
tk.Label(left_panel,text='Rechercher',bg='#B5BCF0',font=research_font).pack(padx=80,pady=40)
entry=tk.Entry(left_panel,bg='white',relief='raised',width=30,exportselection=0,justify='center',textvariable=value_entry)
entry.pack()
nb_resultats=tk.Label(left_panel,bg='#B5BCF0',font=research_font)
chargement_label=tk.Label(left_panel,bg='#B5BCF0',font=research_font)


#########################################################
tk.Button(left_panel,text="Par Titre",command=lambda:valider('goom'),font=title1_font,relief='ridge',borderwidth=5,bg='white',width=12,cursor="hand1").pack(pady=10)
tk.Button(left_panel,text="Par ISBN",command=lambda:valider('editions'),font=title1_font,relief='ridge',borderwidth=5,bg='white',width=12,cursor="hand1").pack(pady=10)

nb_resultats.pack()
chargement_label.pack()
#########################################################





##################################################################################################################
##################################################################################################################
##################################################################################################################
"""
Panneau de droite :

Interface de recherche
"""
##################################################################################################################
##################################################################################################################
##################################################################################################################
research_frame=tk.Frame(right_panel,bg='#8F98E2') #5f8ade
images=[ImageTk.PhotoImage(Image.open("img/no_img.jpg"))]*4
###############################################################
panel1=tk.Frame(research_frame,bg='white')
panel2=tk.Frame(research_frame,bg='white')
panel3=tk.Frame(research_frame,bg='white')
panel4=tk.Frame(research_frame,bg='white')
###############################################################
def reinitialiser_recherche():
    global page_num,pages_max
    page_num=1
    numberpage.configure(text=str(page_num)+'/'+str(pages_max))
    previous_page.configure(state='disable')
    next_page.configure(state='normal')
###############################################################
def clic_ISBN(ISBN):
    value_entry.set(ISBN)
    valider('editions')
def frame_valider(ISBN): #9782322172290
    ajoute,data,img,synopsis=web_json.launch(ISBN)
    print(ajoute)
    if ajoute==True:
        messagebox.showinfo('Réussi','Livre ajouté')
    elif ajoute==False:
        messagebox.showerror('Erreur','Livre non rajouté')
    elif ajoute=='existe':
        messagebox.showerror('Erreur','Le livre est déja dans la bibliothèque')
###############################################################
def afficher(panel,infos,image):
    ISBN=infos['ISBN-13']
    title=infos['Title']
    authors=infos['Authors']
    synopsis=infos['synopsis']
    ##########################""""
    Language=infos['Language']
    year=infos['Year']
    publisher=infos['Publisher']
    
    
    author=str()
    for o in authors:
        author+=o+' & '
    authors=author[0:-3]
    ############################
    if len(title)>40:
        title=title[0:32]+'...'
    if synopsis==None:
        synopsis='Vide'
    else:
        for i in range(len(synopsis)):
            if i%45==0 and i!=0:
                synopsis=synopsis[0:i]+'\n'+synopsis[i:len(synopsis)]
            if i>=400:
                synopsis=synopsis[0:i]+'...'
                break

    ###########################################################
    label=tk.Label(panel,text=title+' '+ISBN,font=tt_font,bg='white')
    label.grid(row=0,column=0,pady=5,padx=10) #titre du livre
    label.bind("<Button-1>",lambda e:clic_ISBN(ISBN))
    ###########################################################
    auteur_label=tk.Label(panel,text=authors[0:30],bg='white',font=tt_font).grid(row=1,column=0)

    ###########################################################
    tk.Label(panel,image=image).grid(row=2,column=1,padx=5) #image
    tk.Label(panel,text=synopsis,font=tt_font1,bg='white',justify='left').grid(row=2,column=0,padx=5) #synopsis
    tk.Label(panel,text='Langue: {}, editeur:{}, \nannée : {}'.format(Language,publisher,year),font=tt_font1,bg='white',justify='left').grid(row=3,column=0,padx=5) #synopsis

    ###########################################################
    tk.Button(panel,text='Ajouter',font=tt_font,relief='ridge',borderwidth=5,bg='white',cursor="hand1",command=lambda:frame_valider(ISBN)).grid(row=3,column=1,pady=15)
########################################################

def affichage_resultats():
    global panel1,panel2,panel3,panel4,images,liste_decoupe
    #####################################################
    research_frame.pack_forget()
    panel1.destroy()
    panel2.destroy()
    panel3.destroy()
    panel4.destroy()
    #####################################################
    list_ISBN=liste_decoupe[page_num-1]
    print(liste_decoupe)

    num_isbn=len(list_ISBN)
    if num_isbn>=1:
        panel1=tk.Frame(research_frame,bg='white',relief='raised')
        panel1.grid(row=0,column=0,padx=15,pady=15)
        # data[list_ISBN[0]]['img']
        images[0] = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(return_img(list_ISBN[0])).content)))
        ###################################################
        afficher(panel1,return_data(list_ISBN[0]),images[0],)
    if num_isbn>=2:
        panel2=tk.Frame(research_frame,bg='white',relief='raised')
        panel2.grid(row=1,column=0,padx=15,pady=15)
        images[1] = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(return_img(list_ISBN[1])).content)))
        ###################################################
        afficher(panel2,return_data(list_ISBN[1]),images[1])
    if num_isbn>=3:
        panel3=tk.Frame(research_frame,bg='white',relief='raised')
        panel3.grid(row=0,column=1,padx=15,pady=15)
        images[2] = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(return_img(list_ISBN[2])).content)))
        ###################################################
        afficher(panel3,return_data(list_ISBN[2]),images[2])
    if num_isbn>=4:
        panel4=tk.Frame(research_frame,bg='white',relief='raised')
        panel4.grid(row=1,column=1,padx=15,pady=15)
        images[3] = ImageTk.PhotoImage(Image.open(BytesIO(requests.get(return_img(list_ISBN[3])).content)))
        ###################################################
        afficher(panel4,return_data(list_ISBN[3]),images[3])

    research_frame.pack(side=tk.TOP)
    chargement_label.configure(text='')
#####################################################
page_panel=tk.Frame(right_panel,bg='#8F98E2') #8F98E2
page_panel.pack(side=tk.BOTTOM)

page_num=1 #numero de page

def change_page(num):
    global page_num,pages_max
    
    if page_num==1 and num==-1:
        page_num=1
        previous_page.configure(state='disable')
        next_page.configure(state='disable')
        
    elif page_num+num<=pages_max:
        previous_page.configure(state='normal')
        next_page.configure(state='normal')
        page_num+=num
        numberpage.configure(text=str(page_num)+'/'+str(pages_max))
        affichage_resultats()
        if page_num==1:
            previous_page.configure(state='disable')
        if page_num==pages_max:
            next_page.configure(state='disable')

#########################################################
previous_page=tk.Button(page_panel,text='Page précédente',font=tt_font,relief='ridge',borderwidth=5,bg='white',width=12,command=lambda:change_page(-1),state='disable')
previous_page.grid(column=0,row=0,pady=65,padx=50)
numberpage=tk.Label(page_panel,text=page_num,font=title1_font,bg='#8F98E2',fg='white')
numberpage.grid(column=1,row=0)
next_page=tk.Button(page_panel,text='Page suivante',font=tt_font,relief='ridge',borderwidth=5,bg='white',width=12,command=lambda:change_page(1))
next_page.grid(column=2,row=0,padx=50)
#########################################################
root.mainloop()