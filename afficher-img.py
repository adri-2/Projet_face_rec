from tkinter import *
from PIL import Image,ImageDraw,ImageTk

root = Tk()
root.title("window")
root.geometry("550x450")

# creer un bouton

# creer un objet image

load = Image.open("image/1.jpg")

 
# ceer une phote image
photo = ImageTk.PhotoImage(load)

# label sur le quel affiche l'image
lable_img = Label(root, image = photo)
lable_img.place(x=0,y=0)

# creer un bouton
bt_close = Button(root, text="EXIT",command=root.quit )
bt_close.pack()
bt_close.place(x=250,y=400)
root.mainloop()
 