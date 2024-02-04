from tkinter import *
from PIL import Image, ImageDraw, ImageTk



root = Tk()
root.geometry("750x500")
root.title("menu_windows")

mon_menu = Menu(root)
def affiche():
    img = Image.open("image/1.jpg")
    img_tk = ImageTk.PhotoImage(img)
    label_img = Label(root,image=img_tk)
    label_img.pack()
    print("image affiche")
    root.mainloop()



# sous onglet fichier
fichier = Menu(mon_menu,tearoff=0)
fichier.add_command(label="affiche",command=affiche)


# les 2  principaux onglets
mon_menu.add_cascade(label="Fichier",menu=fichier)
mon_menu.add_cascade(label="Option")

root.config(menu=mon_menu)


root.mainloop()