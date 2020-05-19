import tkinter as tk
from reservation import reservation_read
from tkinter import messagebox
def valider():
    numero = entree.get()
    ok = reservation_read(numero)
    if ok:
        pass
    else :
        messagebox.showerror('Erreur','Livre emprunté')

fenetre = tk.Tk()
fenetre.geometry('200x60')

frame1 = tk.Frame(fenetre)
frame1.pack(fill='both', expand = 'yes')

isbn = tk.Label(fenetre, text = "ISBN" )
isbn.pack()

entree = tk.Entry(fenetre, width = 30)
entree.pack()

fenetre.mainloop()