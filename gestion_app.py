import tkinter as tk #module tkinter
from tkinter import font,messagebox,filedialog #sous-modules tkinter
import tools.web_json as web_json #module perso
from tools.data_isbn import deljson #module perso
from PIL import Image, ImageTk #module gestion d'image
from tools.reservation import reservation_del,reservation_data,reservation_state
import tools.book as book
#################################################
color='#B5BCF0'

root2=tk.Tk()
root2.resizable(False,False) #ne permet pas d'agrandir
root2.title("ISBN : Gestion")
root2.configure(background=color)
root2.geometry("575x300")
from tools.font import *
#################################################
title_font=font.Font(family='Calibri',size=25,underline=1)
title1_font=font.Font(family='Calibri',size=18)
title2_font=font.Font(family='Calibri',size=15,weight='bold')
title3_font=font.Font(family='Calibri',size=12,slant='italic')
#################################################
affichage_frame=tk.Frame(root2,bg=color)
information_frame=tk.Frame(affichage_frame,bg=color)
emprunt_isbnframe=None
image = ImageTk.PhotoImage(Image.open('img/no_img.jpg'))
#################################################
def valider_affichage():
    global affichage_frame
    affichage_frame.destroy()
    affichage_frame=tk.Frame(root2,bg=color)
    root2.geometry("575x300")
    main_frame.pack()
##################################################################################################
def affichage_resultats(ISBN,data,img,sypnosis):
    '''
    On modifie l'affichage pour montrer les données importées
    '''
    global image
    main_frame.pack_forget() #on masque la frame principale

    root2.geometry("500x475")   #redimensionnement de la fenêtre
    affichage_frame.pack(fill="both",expand=tk.YES) 
    information_frame.grid(row=0,column=0)
    ##################################
    if len(data['Title'])>=50: #on raccourci le titre si nombre caractères supérieur à 50
        data['Title']=data['Title'][0:50]+'...'
    text='{}\n Par {}'.format(data['Title'],str(data['Authors']).lstrip('[').rstrip(']'))
    ##################################
    tk.Label(information_frame,text=text,font=title2_font,fg ='black',bg=color).grid(row=0,column=0) #titre & auteurs
    tk.Label(information_frame,text='ISBN: '+ISBN,font=title2_font,fg ='black',bg=color).grid(row=2,column=0) #ISBN
    tk.Label(information_frame,text='{}, publié en {}, langue : {}'.format(data['Publisher'],data['Year'],data['Language']),
                    font=title2_font,fg ='black',bg=color).grid(row=3,column=0)#editeur & année
    ##################################
    image = ImageTk.PhotoImage(Image.open(img))
    tk.Label(affichage_frame,image=image).grid(row=1,column=0)
    ##################################
    if len(sypnosis)>=400:  #Si il y a plus de 400 caractères, on s'arrête à 400 caractères et on affiche des points de suspensions
        sypnosis=sypnosis[0:400]+'...'

    tk.Label(information_frame,text=sypnosis,font=title3_font,fg ='black',bg=color).grid(row=5,column=0)
    tk.Button(affichage_frame, text="Fermer",command=valider_affichage,font=title1_font,relief='ridge',borderwidth=5,bg='white').grid(row=2,column=0)
##################################################################################################
def filepath(): #ouvre une boîte de dialogue invitant l'utilisateur à donner le chemin du fichier
    return filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('jpg files','.jpg')])

def modif_manuelle(ISBN,data,img,sypnosis):
    '''
    Si la recherche automatique n'a pas aboutie et que le l'utilisateru choisit de modifier les données manuellement
    On modifie l'affichage pour montrer les données importées
    '''
    pass
    # global pic,image
    # entry_frame.pack_forget()
    # fenetre_connexion.geometry("500x375")
    # affichage_frame.pack(fill="both",expand=tk.YES) #"2020", "img": "img/Miroir_de_nos_peines_9782226449757.jpg", "taken": false}}}
    # information_frame.grid(row=0,column=0)
    # ##################################
    # value = tk.StringVar() 
    
    # tk.Label(information_frame,text='ISBN: '+ISBN,font=title2_font,fg ='black',bg=color).grid(row=0,column=0,pady=10)
    # tk.Label(information_frame,text='Titre:',font=title2_font,fg ='black',bg=color).grid(row=1,column=0)
    # ########
    # value.set(data['Title'])
    # entry_title=tk.Entry(information_frame,textvariable=value,width=25).grid(row=1,column=1)
    
    # ########
    # tk.Label(information_frame,text='Auteur(s):',font=title2_font,fg ='black',bg=color).grid(row=2,column=0,pady=10)
    # value.set(data['Authors'])
    # entry_authors=tk.Entry(information_frame,textvariable=value,width=25).grid(row=2,column=1)
    # ########
    # tk.Label(information_frame,text='Publieur/Editeur:',font=title2_font,fg ='black',bg=color).grid(row=3,column=0,pady=10)
    # value.set(data['Publisher'])
    # entry_publisher=tk.Entry(information_frame,textvariable=value,width=25).grid(row=3,column=1)

    # tk.Label(information_frame,text='Année:',font=title2_font,fg ='black',bg=color).grid(row=4,column=0,pady=10)
    # value.set(data['Year'])
    # entry_year=tk.Entry(information_frame,textvariable=value,width=25).grid(row=4,column=1)

    # tk.Label(information_frame,text='Sypnosis:',font=title2_font,fg ='black',bg=color).grid(row=5,column=0,pady=10)
    # value.set(sypnosis)
    # entry_sypnosis=tk.Entry(information_frame,textvariable=value,width=25).grid(row=5,column=1)
    
    # # pic = Image.open(img)
    # # image = ImageTk.PhotoImage(pic)

    # # affichage_img_l=tk.Label(affichage_frame,image=image).grid(row=1,column=0)
    # bouton_affichage.configure(text='Valider',command=valider_affichage)
    # bouton_affichage.grid(row=6,column=0)

################################################################################################## 
def add(ISBN):
    ajoute,data,img,sypnosis=web_json.search(ISBN) #on lance la recherche 
    if ajoute==True: #le livre a été rajouté
        print(data,img,sypnosis[0:30],ajoute)
        affichage_resultats(ISBN,data,img,sypnosis)

    elif ajoute=='existe': #le livre existe déja
        messagebox.showerror('Erreur','ISBN déja présent')

    elif ajoute==False: #le livre n'a pas été rajouté
        if messagebox.askokcancel('Erreur',
            'Erreur avec {}:\nVoulez vous inscrire les données manuellement ou annuler ?'.format(ISBN)):
            modif_manuelle(ISBN,data,img,sypnosis)
#################################################
def voir_reservation(ISBN):
    global image,emprunt_isbnframe
    emprunt_isbnframe=tk.Frame(root2,bg='white')
    emprunt_isbnframe.pack(expand=tk.YES)
    img_frame=tk.Frame(emprunt_isbnframe,bg='white')
    img_frame.grid(row=0,column=0)
    info_frame=tk.Frame(emprunt_isbnframe,bg='white')
    info_frame.grid(row=0,column=1,sticky='n',padx=15)
    #################################################
    image=ImageTk.PhotoImage(Image.open('img/{}.jpg'.format(ISBN)))
    data=reservation_data(ISBN)
    tk.Label(img_frame,image=image).pack()
    tk.Label(info_frame,text=book.titlefromISBN(ISBN),font=tt_font_title,bg='white').grid(row=0,column=0)
    tk.Label(info_frame,text='ISBN:{}'.format(ISBN),font=tt_font_title,bg='white').grid(row=1,column=0)
    tk.Label(info_frame,text='Emprunté par {},\ndu {} au {}'.format(data['Name'],data['from'],data['to']),font=tt_font,bg='white').grid(row=2,column=0,pady=5)
    tk.Button(info_frame,text='Marquer le livre\ncomme non-emprunté',command=lambda:valider('rendu')).grid(row=3,column=0,pady=15)
    tk.Button(info_frame,text='Annuler',command=lambda:valider('rendu_annule')).grid(row=4,column=0,pady=15)
def valider(types):
    ISBN=ISBN_entry.get()
    if ISBN!='':
        if types=='ajouter':
            add(ISBN)
        elif types=='supprimer':
            deljson(ISBN)
        elif types=='rendre':
            if reservation_state(ISBN)==True:
                main_frame.pack_forget()
                voir_reservation(ISBN)
            else:
                messagebox.showerror('ISBN',"Le livre n'a pas été emprunté")
        elif types=='rendu':
            if reservation_del(ISBN)==True:
                messagebox.showinfo('ISBN','Le livre a bien été retiré')
                emprunt_isbnframe.destroy()
                main_frame.pack()
            else:
                messagebox.showerror('Erreur',"Le livre n'a pas pu être retiré")
        elif types=='rendu_annule':
                emprunt_isbnframe.destroy()
                main_frame.pack()            
    else:
        messagebox.showwarning('Erreur',"Vous n'avez pas rentré de numéro d'ISBN")  
##################################################################################################
"""
Création de la frame principale
"""
##################################################################################################
def connection():
    global main_frame
    password=mdp_entry.get()
    if password=='ISNcabrini':
        messagebox.showinfo('Connection','Vous êtes connecté')
        mdp_frame.pack_forget()
        main_frame.pack(fill="both", expand="yes")
    else:
        messagebox.showwarning('Connection','Mot de passe eronné')
         
mdp_frame=tk.Frame(root2,bg=color)
tk.Label(mdp_frame,text="Mot de passe admin",font=title1_font,bg=color).pack(pady=25)
mdp_entry=tk.Entry(mdp_frame, width=40,justify='center',show='*')
mdp_entry.pack()
tk.Button(mdp_frame,text='Se connecter',command=connection,
                font=title1_font,relief='ridge',borderwidth=5,bg='white').pack(pady=15)
mdp_frame.pack(fill="both", expand="yes")       




        

main_frame=tk.Frame(root2,bg=color)
tk.Label(main_frame,text='ISBN : Gestion',font=title_font,bg=color).pack(pady=15)
tk.Label(main_frame,text="Renseignez l'ISBN",font=title1_font,bg=color).pack()
#################################################
ISBN_entry = tk.Entry(main_frame, width=40,justify='center')#champ de saisie pour l'ISBN
ISBN_entry.pack()
#création des deux boutons ajouter & supprimer
tk.Button(main_frame, text="Ajouter",command=lambda:valider('ajouter'),
                font=title1_font,relief='ridge',borderwidth=5,bg='white').pack(pady=10)
tk.Button(main_frame, text="Supprimer",command=lambda:valider('supprimer'),
                font=title1_font,relief='ridge',borderwidth=5,bg='white').pack(pady=10)
tk.Button(main_frame, text="Rendre le livre",command=lambda:valider('rendre'),
                font=title1_font,relief='ridge',borderwidth=5,bg='white').pack(pady=10)
#################################################

root2.mainloop()