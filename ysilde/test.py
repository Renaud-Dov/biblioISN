import tkinter as tk

fenetre = tk.Tk()

def valider():
    pass

fenetre.geometry('500x500') #taille de la fenêtre
fenetre.resizable(False,False) #on peut pas redimensionner
fenetre.title('Test rectangle')
fenetre.configure(bg='red')

panel = tk.Frame(fenetre)
panel.pack(expand=tk.YES)


title="titre de l'oeuvre"
auteur="auteur"
desc="description description description description description description description"
annee = "0000"
editeur = "editeur"

titre_label =tk.Label(panel, text = title) #et t'écris le reste
auteur_label = tk.Label (panel, text = auteur)
description_label = tk.Label (panel, text =desc)
annee_label = tk.Label (panel, text = annee)
editeur_label = tk.Label (panel, text = editeur)

bouton = tk.Button(panel, text = "Réserver", command = valider)
bouton.grid(row = 8,column=0)

titre_label.grid(row=3, column = 1,padx=5,pady=10)
auteur_label.grid(row = 4, column = 1)
description_label.grid (row = 3, column = 2)
annee_label.grid(row = 3, column = 2)
editeur_label.grid(row = 4, column = 2)

fenetre.mainloop()
