import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import tools.research as research
from tools.book import readinfo
from tools.note import moy_note
import tools.date as date
from tools.reservation import reservation_read,reservation_add
root=tk.Tk()
root.geometry('1400x900')
root.resizable(False,False)
root.title('BIBLIO-ISN')
root.configure(bg='#809c7c')

from tools.font import *



##################################################################################################################
##################################################################################################################
##################################################################################################################
"""
Panneau de gauche :

Menu de recherche
"""
##################################################################################################################
##################################################################################################################
##################################################################################################################
left_panel=tk.Frame(root,bg='#aec9ab',relief='raised')
left_panel.pack(fill=tk.Y,side=tk.LEFT)
right_panel=tk.Frame(root,relief='raised',bg='#809c7c')
welcome_label=tk.Label(root,text='Bienvenue dans BIBLIO-ISN',bg='#809c7c',fg='white',font=title_font)
#########################################################
liste_decoupe=[]
value_entry = tk.StringVar()
pages_max=int()
#########################################################
def add_button():
    messagebox.showinfo('Erreur','Lancez le programme isbn_ui.py')
#########################################################
def valider():
    global nb_resultats,liste_decoupe,pages_max
    ###########################################
    data=entry.get()
    if data!='':
        resultats,liste_decoupe=research.recherche(data,6)

        if resultats!=[]:
            nb_resultats.configure(text='Nombre de résultats: {}'.format(len(resultats)))
            welcome_label.forget()
            right_panel.pack(fill=tk.BOTH,expand=tk.YES) 
            pages_max=len(liste_decoupe) # nombre de pages nécéssaire pour afficher tous les résultats
            reinitialiser_recherche()
            affichage_resultats()
        else:
            messagebox.showerror('Erreur','Aucun résultat')
    else:
        messagebox.showerror('Erreur','Aucun terme rentré')
#########################################################
tk.Label(left_panel,text='BIBLIO-ISN',bg='#aec9ab',font=title1_font).pack(pady=25,padx=80)
welcome_label.pack(expand=tk.YES)
#########################################################
tk.Label(left_panel,text='Rechercher un livre',bg='#aec9ab',font=research_font).pack(padx=80)
entry=tk.Entry(left_panel,bg='white',relief='raised',width=30,exportselection=0,justify='center',textvariable=value_entry)
entry.pack()
nb_resultats=tk.Label(left_panel,bg='#aec9ab',font=research_font)
#########################################################
loupe=Image.open('tools/icons/search.png')
loupe=ImageTk.PhotoImage(loupe)

tk.Button(left_panel,text="Rechercher",image=loupe,command=valider,font=title1_font,relief='ridge',borderwidth=5,bg='white',width=12,cursor="hand1").pack(pady=10)

nb_resultats.pack()
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
research_frame=tk.Frame(right_panel,bg='#809c7c') #5f8ade
images=[0]*6
clock_img=ImageTk.PhotoImage(Image.open('tools/icons/clock.jpg')) #clock
research_panels=[tk.Frame(research_frame,bg='white')]*6

###############################################################
def reinitialiser_recherche():
    '''
    On se remet à la première page
    '''
    global page_num,pages_max
    page_num=1
    numberpage.configure(text=str(page_num)+'/'+str(pages_max))
    previous_page.configure(state='disable')
    next_page.configure(state='normal')

def clic_auteur(authors):
    '''
    Lance une recherche d'un auteur
    '''
    value_entry.set(' '.join(authors)) #on écrit dans l'encadré le nom de(s) auteurs
    valider() #on lance la recherche() avec le nom de l'auteur
###############################################################
def frame_valider(ISBN):
    affichage_fiche(ISBN)
###############################################################
def afficher(panel,infos,number):
    # global clock_img
    print(number,infos[0:3])
    # print(infos)
    # ISBN=infos[0]
    # title=infos[1]
    # authors=infos[2]
    # synopsis=infos[3]
    # disponible=infos[4]
    images[number] = ImageTk.PhotoImage(Image.open(infos[4]))
    author=str()
    for o in infos[2]:
        author+=o+', '  
    author=author[0:-2]
 
    ###########################################################
    if len(infos[1])>40: #si titre + de 40 caractères
        infos[1]=infos[1][0:37]+'...'
    for i in range(len(infos[3])):
        if i%45==0 and i!=0: #si multiple de 45 caractères
            infos[3]=infos[3][0:i]+'\n'+infos[3][i:len(infos[3])]
        if i>=400:
            infos[3]=infos[3][0:i]+'...' #si plus de 400 caractères
            break
    ###########################################################
    panel_info=tk.Frame(panel,bg='white',cursor="hand1")
    panel_info.grid(row=0,column=1,sticky='n')
    ###########################################################
    title=tk.Label(panel_info,text=infos[1],font=tt_font_title,bg='white')
    title.grid(row=0,column=0,pady=5,padx=10)
    ###########################################################
    auteur_label=tk.Label(panel_info,text=author,bg='white',font=tt_font3)#auteurs
    auteur_label.grid(row=1,column=0)
    auteur_label.bind("<Button-1>",lambda e:clic_auteur(infos[2]))
    ###########################################################
    image=tk.Label(panel,image=images[number])
    image.grid(row=0,column=0,sticky='n') #image

    if infos[5]==True:
        clock=tk.Label(panel,image=clock_img)
        clock.grid(row=0,column=0,sticky='nw')
        clock.bind('<Button-1>',lambda e:frame_valider(infos[0]))
    ###########################################################
    desc=tk.Label(panel_info,text=infos[3],font=tt_font1,bg='white',justify='left')
    desc.grid(row=2,column=0,padx=5) #synopsis
    ###########################################################
    for i in [panel,panel_info,desc,title,image]:
        i.bind('<Button-1>',lambda e:frame_valider(infos[0])) #Clic gauche

photo_fiche=ImageTk.PhotoImage(Image.open('img/{}.jpg'.format('9780525555353')))
star_fiche=ImageTk.PhotoImage(Image.open('tools/icons/stars/5,0.jpg'))
fiche_panel=None
def emprunt(ISBN,time,name,title):
    if name!='':
        if messagebox.askyesno('Emprunt',"Confirmer l'emprunt de \"{}\"".format(title)):
            if reservation_add(ISBN,time,name):
                messagebox.showinfo('Emprunt','Votre emprunt a été enregistré au nom de {} pour une durée de {} jours'.format(name,time))
                fiche_panel.destroy()
                affichage_resultats()
            else:
                messagebox.showwarning('Erreur',"Le livre n'a pas pu été enregistré. Demandez conseil auprès de votre bibliothécaire")
    else:
        messagebox.showwarning('Erreur',"Vous n'avez pas mis votre nom prénom")
def affichage_fiche(ISBN):
    global right_panel,photo_fiche,star_fiche,fiche_panel
    fiche_panel=tk.Frame(right_panel,bg='#aec9ab',bd=8)
    info1=tk.Frame(fiche_panel,bg='white')
    info2=tk.Frame(fiche_panel,bg='white')
    emprunt_panel=tk.Frame(info1,bg='white')
    desc_panel=tk.Frame(info1,bg='white')
    fiche_panel.grid(row=0,column=0,sticky='s')
    info1.grid(row=0,column=0,sticky='ns')
    info2.grid(row=0,column=1,sticky='ns')
    desc_panel.grid(row=2,column=0,pady=15,padx=15)
    emprunt_panel.grid(row=3,column=0)
    ###################################################
    book,notes_data=readinfo(ISBN)
    note,note_img=moy_note(notes_data)
    try:
        photo_fiche=ImageTk.PhotoImage(Image.open('img/{}.jpg'.format(ISBN)))
    except FileNotFoundError:
        photo_fiche=ImageTk.PhotoImage(Image.open('img/no_img.jpg'))
    star_fiche=ImageTk.PhotoImage(Image.open('tools/icons/stars/{}.jpg'.format(str(note_img).replace('.',','))))
    ###################################################
    author=str()
    for o in book["Auteur"]:
        author+=o+', '  
    author=author[0:-2]
    # for i in range(len(book['Synopsis'])):
    #         if i%100==0 and i!=0: #si multiple de 45 caractères
    #             book['Synopsis']=book['Synopsis'][0:i]+'\n'+book['Synopsis'][i:len(book['Synopsis'])]
    ###################################################
    tk.Label(info1,text=book['Titre'],font=title2_font,bg='white').grid(row=0,column=0,pady=5)
    tk.Label(info1,text='Par : {}'.format(author),font=tt_font2,bg='white').grid(row=1,column=0)
    ###################################################
    text = tk.Text(desc_panel, wrap=tk.WORD,bd=0,font=tt_font1,height=18,exportselection=0)
    text.insert(tk.END,book['Synopsis'])
    text.configure(state='disabled')
    text.pack(side=tk.LEFT)
    if len(book['Synopsis'])>=1410: #rajout d'une barre de défilement si le texte est trop long
        scrollbar = tk.Scrollbar(desc_panel)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=text.yview)

    
    ###################################################
    tk.Label(info2,image=photo_fiche).grid(row=0,column=0,pady=10)
    tk.Label(info2,text='ISBN: {}\nAnnée: {}\nLangue: {}\nNote:{}/5'.format(ISBN,book['year'],book['language'],round(note,2))
                            ,justify='left',fg='grey',bg='white').grid(row=1,column=0,pady=5,padx=10)
    tk.Label(info2,image=star_fiche,bd=0).grid(row=2,column=0,pady=5)
    tk.Button(info2,command=lambda:fiche_panel.destroy(),text='Fermer',font=tt_font,relief='ridge',borderwidth=5,bg='white',width=12).grid(row=3,column=0,pady=15)
    ###################################################
    if book['taken']==False:
        tk.Label(emprunt_panel,bg='white',font=tt_font3,
                text='Réservation disponible:\nVous pouvez réserver le livre du {} au {} (2 semaines) ?'.format(date.date_today(),date.date_add(14))).grid(row=0,column=0)
        tk.Label(emprunt_panel,text='Nom & Prénom',bg='white').grid(row=1,column=0)
        name_entry=tk.Entry(emprunt_panel,bg='white',relief='raised',width=30,exportselection=0,justify='center')
        name_entry.grid(row=2,column=0)
        ##################
        tk.Button(emprunt_panel,text='Réserver',command=lambda:emprunt(ISBN,14,name_entry.get(),book['Titre']),font=tt_font,relief='ridge',borderwidth=5,bg='white',width=12).grid(row=3,column=0,pady=10)
    elif book['taken']==True:
        tk.Label(emprunt_panel,bg='white',text='Réservation indisponible:\nLe livre sera disponible le {}'.format(reservation_read(ISBN))).grid(row=0,column=0,pady=5)
    
#########################################################

def affichage_resultats():
    '''
    On lance l'affichage de chaque rectangle
    '''
    global images,liste_decoupe,research_panels
    #####################################################
    research_frame.pack_forget() #on masque le frame le temps de récupérer les données
    for o in research_panels:
        o.destroy() #on supprime tous les rectangles
    #####################################################
    list_ISBN=liste_decoupe[page_num-1] #on prend les nb ISBN correspondant au numero de page

    for o in range(len(list_ISBN)):
        research_panels[o]=tk.Frame(research_frame,bg='white',cursor="hand1",height=200,width=490)
        if o==0:row=0;column=0
        elif o==1:row=0;column=1
        elif o==2:row=1
        elif o==3:row=1
        elif o==4:row=2
        elif o==5:row=2
        if o%2==0:column=0
        else:column=1
        research_panels[o].grid(row=row,column=column,padx=15,pady=15)
        research_panels[o].grid_propagate(0)
        afficher(research_panels[o],research.data(list_ISBN[o]),o)

    research_frame.grid(row=0,column=0,sticky='n') #on réaffiche le frame
#####################################################
numpage_panel=tk.Frame(right_panel,bg='#809c7c') #809c7c
numpage_panel.grid(row=1,column=0,sticky='s')
page_num=1 #numero de page

def change_page(num):
    global page_num,pages_max

    if page_num+num<=pages_max:
        previous_page.configure(state='normal') #Le bouton refonctionne
        next_page.configure(state='normal')     #Le bouton refonctionne
        page_num+=num
        numberpage.configure(text='{}/{}'.format(page_num,pages_max))
        affichage_resultats()
        if page_num==1:
            previous_page.configure(state='disable')    #Le bouton désactivé
        if page_num==pages_max:#on est à la dernière page
            next_page.configure(state='disable')        #Le bouton est désactivé

#########################################################
'''
Création des boutons page précédente & suivante, et du numero de la page
'''
previous_page=tk.Button(numpage_panel,text='Page précédente',font=tt_font,relief='ridge',borderwidth=5,bg='white',width=12,command=lambda:change_page(-1),state='disable')
previous_page.grid(column=0,row=0,pady=65,padx=50)
numberpage=tk.Label(numpage_panel,text=page_num,font=title1_font,bg='#809c7c',fg='white')
numberpage.grid(column=1,row=0)
next_page=tk.Button(numpage_panel,text='Page suivante',font=tt_font,relief='ridge',borderwidth=5,bg='white',width=12,command=lambda:change_page(1))
next_page.grid(column=2,row=0,padx=50)
#########################################################







root.mainloop()