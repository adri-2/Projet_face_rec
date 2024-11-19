from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk

root = Tk()

# Obtenir les dimensions de l'écran
# largeur_ecran = root.winfo_screenwidth()
# hauteur_ecran = root.winfo_screenheight()

# Définir la taille de la fenêtre en plein écran
root.geometry("1300x850")
# root.geometry("{}x{}".format(largeur_ecran, hauteur_ecran))
# print((largeur_ecran, hauteur_ecran))
# root.geometry("1000x900")
root.title("root")
root.attributes("-fullscreen",True)
root.config(background="black")
#root.resizable(width=False,height=False)

def fullscreen(event=None):
    root.attributes("-fullscreen",not root.attributes("-fullscreen"))
root.bind("<Escape>",fullscreen)

def browse():
    global img
    # pour ouvri le fenetre de selection
    filename = filedialog.askopenfilename(title = "Select a File")
    # recupere le chemin de l'image et pour l'ouvre 
    img = Image.open(filename) 
    # img_r = img.resize((480,500))
    img_r = img.resize((490,560))
    # transforme l'image pour quel soit utulisable sur tkinter
    img_tk = ImageTk.PhotoImage(img_r)
    # applique sur un label <label_img>
    label_img = Label(frame_w,image=img_tk)
    # positionne le label
    label_img.pack()
    print("image affiche")
    # applique le label
    root.mainloop()




# frame_w = Frame(root,width=480,height=500,bg="red")
frame_w = Frame(root,width=500,height=570,bg="red",borderwidth=2,relief="solid",highlightthickness=3)
# frame_w.grid(row=0,column=0,padx=10,pady=10)
frame_w.grid(row=0, column=0, padx=10, pady=10)  # sticky="nsew" pour permettre au cadre de se développer avec la fenêtre
frame_w.grid_rowconfigure(0, weight=1)  # Permet au cadre de s'étendre verticalement
frame_w.grid_columnconfigure(0, weight=1)  # Permet au cadre de s'étendre horizontalement


# frame_h = Frame(root,width=480,height=500)
frame_h = Frame(root,width=500,height=570,bg="blue",borderwidth=2,relief="solid",highlightthickness=3)
# frame_h.grid(row=0,column=1,padx=10,pady=10)
frame_h.grid(row=0, column=1, padx=10, pady=10)
frame_h.grid_rowconfigure(0, weight=1)
frame_h.grid_columnconfigure(0, weight=1)




# boutton pour cherche l'image 
Button(root,text='Browse an Image',command=browse,fg='blue',font='arial 18').place(x=150,y=600)

# root.grid_rowconfigure(0, weight=1)  # Permet à la ligne de se développer verticalement
root.grid_columnconfigure(0, weight=1)  # Permet à la colonne de se développer horizontalement
root.grid_columnconfigure(1, weight=1)


root.mainloop()
