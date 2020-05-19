import tkinter as tk
from PIL import Image,ImageTk
def showimg(img):
    root2=tk.Toplevel(root)
    root2.resizable(False,False)

    img=Image.open(img)
    w, h = img.size
    img=img.resize((w*2,h*2))

    logo=ImageTk.PhotoImage(img)

    canvas=tk.Canvas(root2,width=logo.width(),height=logo.height())
    canvas.create_image(logo.width()/2,logo.height()/2,image=logo)

    canvas.pack()

    # root2.mainloop()