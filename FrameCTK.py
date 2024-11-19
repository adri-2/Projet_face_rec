import Class_interface
from PIL import Image, ImageTk
root = Class_interface.App()

root.geometry('1400x900')
#45pp._set_appearance_mode


def browse():
    global img
    # pour ouvri le fenetre de selection
    filename = Class_interface.ctk.filedialog.askopenfilename(title = "Select a File")
    # recupere le chemin de l'image et pour l'ouvre 
    img = Image.open(filename) 
    # img_r = img.resize((480,500))
    img_r = img.resize((490,560))
    # transforme l'image pour quel soit utulisable sur tkinter
    img_tk = ImageTk.PhotoImage(img_r)
    # applique sur un label <label_img>
    label_img = Class_interface.ctk.CTkLabel(frame_w,image=img_tk)
    # positionne le label
    label_img.pack()
    print("image affiche")
  



# frame_w = Frame(root,width=480,height=500,bg="red")
frame_w = Class_interface.ctk.CTkFrame(root,width=400,height=450,border_width=3)
frame_w.place(x=20,y=20)
# frame_w.grid(row=0, column=0, padx=10, pady=30)  # sticky="nsew" pour permettre au cadre de se développer avec la fenêtre
frame_w.grid_rowconfigure(0, weight=1)  # Permet au cadre de s'étendre verticalement
frame_w.grid_columnconfigure(0, weight=1)  # Permet au cadre de s'étendre horizontalement


# frame_h = Frame(root,width=480,height=500)
frame_h = Class_interface.ctk.CTkFrame(root,width=600,height=600,border_width=3)
frame_h.place(x=650,y=20)
# frame_h.grid(row=0, column=1, padx=10, pady=30)
frame_h.grid_rowconfigure(0, weight=1)
frame_h.grid_columnconfigure(0, weight=1)




# boutton pour cherche l'image 
Class_interface.ctk.CTkButton(root,text='Browse an Image',command=browse).place(x=150,y=600)

# root.grid_rowconfigure(0, weight=1)  # Permet à la ligne de se développer verticalement
root.grid_columnconfigure(0, weight=1)  # Permet à la colonne de se développer horizontalement
root.grid_columnconfigure(1, weight=1)


root.mainloop()



