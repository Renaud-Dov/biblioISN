import tkinter as tk #module tkinter
from tkinter import font,messagebox,filedialog #sous-modules tkinter
import tools.web_json as web_json #module perso
from tools.data_isbn import deljson #module perso
from PIL import Image, ImageTk #module gestion d'image
from tools.reservation import reservation_del,reservation_data,reservation_state
import tools.book as book
import json

import tools.research as research
from tools.book import readinfo
from tools.note import moy_note
import tools.date as date
from tools.reservation import reservation_read,reservation_add

root=tk.Tk()
root.geometry('1400x900')
root.resizable(False,False)
root.title('Gestion BIBLIO-ISN')
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
left_panel.pack(side=tk.LEFT,fill=tk.Y)
right_panel=tk.Frame(root,relief='raised',bg='#809c7c')
image_add=ImageTk.PhotoImage(Image.open('tools/icons/no_img.jpg'))
right_panel.pack(side=tk.RIGHT,fill=tk.Y,expand=1)
emprunt_isbnframe=None
affichage_frame=None
information_frame=None
#########################################################
liste_decoupe=[]
liste_emprunts=[]
pages_max=int()
#########################################################
def valider(types):
    print(types)
    if types=='show':
        show_reservations()
    else:
        ISBN=entry.get()
        if types=='add':
            add(ISBN)
        elif types=='del':
            deljson(ISBN)
        elif types=='edit':
            messagebox.showinfo('Erreur','Fonctionnalité non implémentée')         

#########################################################
# tk.Label(left_panel,text='Rechercher un livre',bg='#aec9ab',font=research_font).pack(padx=80)
tk.Label(left_panel,text='Gestionnaire\nBIBLIO-ISN',bg='#aec9ab',font=title1_font).pack(pady=25,padx=80)
ISBN_frame=tk.Frame(left_panel,bg='#a1ba9e',relief='raised',bd=5)
tk.Label(ISBN_frame,text="Gestion ISBN",font=tt_font2,bg='#a1ba9e').pack(pady=5)
entry=tk.Entry(ISBN_frame,bg='white',relief='raised',width=15,exportselection=0,justify='center',font=tt_font2)
entry.pack(padx=25)
nb_resultats=tk.Label(left_panel,bg='#aec9ab',font=research_font)
#########################################################
tk.Button(left_panel,text="Rafraîchir",command=lambda:valider('show'),font=tt_font2,relief='ridge',borderwidth=5,bg='white',width=8,cursor="hand1").pack(pady=15)
tk.Button(ISBN_frame,text="Ajouter",command=lambda:valider('add'),font=tt_font2,relief='ridge',borderwidth=5,bg='white',width=6,cursor="hand1").pack(pady=10)
tk.Button(ISBN_frame,text="Retirer",command=lambda:valider('del'),font=tt_font2,relief='ridge',borderwidth=5,bg='white',width=6,cursor="hand1").pack(pady=10)
tk.Button(ISBN_frame,text="Modifier",command=lambda:valider('edit'),font=tt_font2,relief='ridge',borderwidth=5,bg='white',width=6,cursor="hand1").pack(pady=10)
ISBN_frame.pack()
tk.Button(left_panel, text="Quitter",command=root.quit,font=tt_font2,relief='ridge',borderwidth=5,bg='white',width=6,cursor="hand1").pack(pady=15,side=tk.BOTTOM)

nb_resultats.pack()

images=[0]*6
page_num=1
research_frame=tk.Frame(right_panel,bg='#809c7c') #5f8ade
research_frame.grid(row=1,column=0,sticky='n')
research_panels=[tk.Frame(research_frame,bg='white')]*6
numpage_panel=tk.Frame(right_panel,bg='#809c7c') #809c7c
numpage_panel.grid(row=2,column=0,sticky='s')
#########################################################
def close_affichage_resultats():
    global affichage_frame,information_frame
    affichage_frame.destroy()
    information_frame.destroy()
def affichage_resultats_add(ISBN,data,img,sypnosis):
    '''
    On modifie l'affichage pour montrer les données importées
    '''
    global image_add,affichage_frame,information_frame
    color='#aec9ab'
    affichage_frame=tk.Frame(right_panel,bg='#aec9ab',relief='raised',bd=5)
    affichage_frame.grid(row=0,column=0)
    information_frame=tk.Frame(affichage_frame,bg='#aec9ab')
    information_frame.grid(row=0,column=0)
    ##################################
    if len(data['Title'])>=50: #on raccourci le titre si nombre caractères supérieur à 50
        data['Title']=data['Title'][0:50]+'...'
    text='{}\n Par {}'.format(data['Title'],str(data['Authors']).lstrip('[').rstrip(']'))
    ##################################
    tk.Label(information_frame,text=text,font=tt_font3,fg ='black',bg=color).grid(row=0,column=0) #titre & auteurs
    tk.Label(information_frame,text='ISBN: '+ISBN,font=tt_font3,fg ='black',bg=color).grid(row=2,column=0) #ISBN
    tk.Label(information_frame,text='{}, publié en {}, langue : {}'.format(data['Publisher'],data['Year'],data['Language']),
                    font=tt_font3,fg ='black',bg=color).grid(row=3,column=0)#editeur & année
    ##################################
    image_add = ImageTk.PhotoImage(Image.open(img))
    tk.Label(affichage_frame,image=image_add).grid(row=1,column=0)
    ##################################
    if len(sypnosis)>=400:  #Si il y a plus de 400 caractères, on s'arrête à 400 caractères et on affiche des points de suspensions
        sypnosis=sypnosis[0:400]+'...'

    tk.Label(information_frame,text=sypnosis,font=tt_font3,fg ='black',bg=color).grid(row=5,column=0)
    tk.Button(affichage_frame, text="Fermer",command=close_affichage_resultats,font=title1_font,relief='ridge',borderwidth=5,bg='white').grid(row=2,column=0,pady=5)


def add(ISBN):
    if ISBN!='':
        ajoute,data,img,sypnosis=web_json.search(ISBN) #on lance la recherche 
        if ajoute==True: #le livre a été rajouté
            print(data,img,sypnosis[0:30],ajoute)
            affichage_resultats_add(ISBN,data,img,sypnosis)

        elif ajoute=='existe': #le livre existe déja
            messagebox.showerror('Erreur','ISBN déja présent')

        elif ajoute==False: #le livre n'a pas été rajouté
            if messagebox.askokcancel('Erreur',
                'Erreur avec {}:\nVoulez vous inscrire les données manuellement ou annuler ?'.format(ISBN)):
                # modif_manuelle(ISBN,data,img,sypnosis)
                pass
    else:
        messagebox.showwarning('Erreur',"Vous n'avez pas rentré d'ISBN")
        


def show_reservations():
    global liste_emprunts,liste_decoupe,pages_max,page_num
    with open('data/reservation.json','r') as outfile:
        liste_emprunts=json.load(outfile)
    liste_ISBN=list(liste_emprunts.keys())
    liste_decoupe=[]
    page_num=1
    for i in range(0,len(liste_ISBN),6):
        liste_decoupe.append(liste_ISBN[i:i+6])
    print(liste_decoupe)

    pages_max=len(liste_decoupe)

    numberpage.configure(text='{}/{}'.format(page_num,pages_max))
    previous_page.configure(state='disable')

    if pages_max==1:
        next_page.configure(state='disable')
    else:
        next_page.configure(state='normal')
    affichage_resultats()


def retirer(ISBN):
    if reservation_del(ISBN)==True:
        messagebox.showinfo('ISBN','Le livre a bien été retiré des emprunts')
        show_reservations()
    else:
        messagebox.showerror('Erreur',"Le livre n'a pas été retiré")
    

def voir_reservation(panel,ISBN,num):
    global images
    img_frame=tk.Frame(panel,bg='white')
    img_frame.grid(row=0,column=0)
    info_frame=tk.Frame(panel,bg='white')
    info_frame.grid(row=0,column=1,sticky='n',padx=15)
    ################################################
    images[num]=ImageTk.PhotoImage(Image.open('img/{}.jpg'.format(ISBN)))
    data=reservation_data(ISBN)
    tk.Label(img_frame,image=images[num]).pack()
    tk.Label(info_frame,text=book.titlefromISBN(ISBN),font=tt_font_title,bg='white').grid(row=0,column=0)
    tk.Label(info_frame,text='ISBN:{}'.format(ISBN),font=tt_font_title,bg='white').grid(row=1,column=0)
    tk.Label(info_frame,text='Emprunté par {},\ndu {} au {}'.format(data['Name'],data['from'],data['to']),font=tt_font,bg='white').grid(row=2,column=0,pady=5)
    tk.Button(info_frame,text='Marquer le livre\ncomme non-emprunté',command=lambda:retirer(ISBN)).grid(row=3,column=0,pady=15)


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
        if o==0 or o==1:row=0
        elif o==2 or o==3:row=1
        elif o==4 or o==5:row=2
        column=o%2

        research_panels[o].grid(row=row,column=column,padx=15,pady=15)
        research_panels[o].grid_propagate(0)
        voir_reservation(research_panels[o],list_ISBN[o],o)
    research_frame.grid(row=0,column=0,sticky='n')


def change_page(num):
    global page_num,pages_max

    print(num,pages_max)
    if page_num+num<=pages_max:
        previous_page.configure(state='normal') #Le bouton refonctionne
        next_page.configure(state='normal')     #Le bouton refonctionne
        page_num+=num
        numberpage.configure(text='{}/{}'.format(page_num,pages_max))
        affichage_resultats()
        if page_num==1:
            previous_page.configure(state='disable')    #Le bouton est désactivé
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

show_reservations()
root.mainloop()