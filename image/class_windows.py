from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
# import face_recognition

#------------------------------------------------------------------------------------------------------#
#                                 CREATION DE LA CLASSE FENETRE                                        # 
#------------------------------------------------------------------------------------------------------#

class MaFenetre(Tk):
    def __init__(self,nom,title,couleur):
        super().__init__()
        self.nom = nom
        self.title(title)
        self.geometry("1295x850")
        self.config(bg=couleur)
        self.attributes("-fullscreen",True)
        def fullscreen(event=None):
           self.attributes("-fullscreen",not self.attributes("-fullscreen"))
        self.bind("<Escape>",fullscreen)

        
        #self.grid_columnconfigure(0,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        

        
# Créer une instance de la classe MaFenetre
root = MaFenetre("wind","tkt","black")

# fonction pour recherche l'image
def browse():
    global img
    # pour ouvri le fenetre de selection
    filename = filedialog.askopenfilename(title = "Select a File")
    # recupere le chemin de l'image et pour l'ouvre 
    img = Image.open(filename) 

    img_r = img.resize((490,560))
    # transforme l'image pour quel soit utulisable sur tkinter
    img_tk = ImageTk.PhotoImage(img_r)
    
    # applique sur un label <label_img>
    label_img = Label(frame_w,image=img_tk)
    # positionne le label
    label_img.place(x=0,y=0)
    print("image affiche")
    # applique le label
    root.mainloop()


# boutton pour cherche l'image 
Button(root,text='Browse an Image',command=browse,fg='blue',font='arial 18').place(x=150,y=600)

# frame de droite
frame_w = Frame(root,width=500,height=570,bg="red",borderwidth=2,relief="solid",highlightthickness=3)
# frame_w.grid(row=0,column=0,padx=10,pady=10)
frame_w.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")  # sticky="nsew" pour permettre au cadre de se développer avec la fenêtre
frame_w.grid_rowconfigure(0, weight=1)  # Permet au cadre de s'étendre verticalement
frame_w.grid_columnconfigure(0, weight=1)  # Permet au cadre de s'étendre horizontalement


# frame de gauche
frame_h = Frame(root,width=500,height=570,bg="blue",borderwidth=2,relief="solid",highlightthickness=3)
# frame_h.grid(row=0,column=1,padx=10,pady=10)
frame_h.grid(row=0, column=1, padx=220, pady=10, sticky="nsew")
frame_h.grid_rowconfigure(0, weight=1)
frame_h.grid_columnconfigure(0, weight=1)

# Lancer la boucle principale de l'application
root.mainloop()






# # fonction pour recherche l'image
# def browse():
#     global image
#     # pour ouvri le fenetre de selection
#     filename = filedialog.askopenfilename(title = "Select a File")
#     # recupere le chemin de l'image et pour l'ouvre 
#     # img = Image.open(filename) 
#     image = face_recognition.load_image_file(filename) # Chargez l'image

#     loc = face_recognition.face_locations(image) # Détecter les visages
#     print(loc)

#     # Créer une nouvelle image
#     image_pil = Image.fromarray(image)
#     draw = ImageDraw.Draw(image_pil)

#     # Dessinez les carrés
#     for tete in loc:
#         y0, x0, y1, x1 = tete
#         #draw.rectangle(((x0,y0),(x1,y1)), outline=(0,0,255))
#         draw.rectangle(((x1, y0), (x0, y1)), outline=(0, 0, 255))
#         #print(x1," ",x0," ",y0," ",y1)
#     # Afficher la nouvelle image
#     # image_pil.show()
#     img_r = image_pil.resize((490,560))
#     photo = ImageTk.PhotoImage(img_r )
#     wondows = Label(frame_w, image=photo)
#     wondows.pack()
