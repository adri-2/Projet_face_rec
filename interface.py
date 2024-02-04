from tkinter import *

# creer notre fenetre
root = Tk()

# donne un titre a notre fenetre
root.title("windows")
# donne les dimention notre fenetre
root.geometry("750x550")
# donne un bg a la fenetre
root["bg"] = "red"
# creation du label objet sur le quelle ont vas afficher des images texte...
label = Label(root,text='bonjour',font=("Verdana",20,"italic bold"),fg="white",bg="red")
#label.pack(side=RIGHT,padx=50)
label.place(x=57,y=67)

def actionbtt():
    if textevar.get() == "py":
        #print('')
        label['text']='bienvenur'
    else:
        label['text']='dsl'
        #print("")

textevar = StringVar()
entre = Entry(root,textvariable=textevar)
entre.place(x=120,y=210) 
bouton = Button(root,text='clik !',command=actionbtt)
bouton.place(x=120,y=239)

# boucle pres à l'emploie pour afficher en permamence le fenetre
root.mainloop()