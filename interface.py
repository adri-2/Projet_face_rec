from tkinter import *

# creer notre fenetre
root = Tk()
# donne un titre a notre fenetre
root.title("windows")
# donne les dimention notre fenetre
root.geometry("750x550")
# donne un bg a la fenetre
root["bg"] = "red"
label = Label(root,text='bonjour')
#label.pack(side=RIGHT,padx=50)
label.place(x=57,y=67)
root.mainloop()