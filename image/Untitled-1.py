from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.geometry("1270x750-1+0")

# label = ctk.CTkLabel(root,text="save user",bg_color="green")
# label.pack(padx=10,fill='both')

frame_p = ctk.CTkFrame(master=root)
frame_p.pack(pady=40,padx=40,expand=True,fill='both')

# lbltitre = ctk.CTkLabel(root,text="save user", )
# lbltitre.place(x=10,y=0)


label_name=ctk.CTkLabel(frame_p,text="NOM ",width=100,height=10)
label_name.place(x=0,y=50)
entry_name=ctk.CTkEntry(frame_p)
entry_name.place(x=200,y=50)





label_name=ctk.CTkLabel(frame_p,text="PRENOM ",width=100,height=10)
label_name.place(x=10,y=90)
entry_name=ctk.CTkEntry(frame_p)
entry_name.place(x=200,y=90)


label_name=ctk.CTkLabel(frame_p,text="DATE NAISSANCE ",width=100,height=10)
label_name.place(x=33,y=130)
entry_name=ctk.CTkEntry(frame_p)
entry_name.place(x=200,y=130)


label_name=ctk.CTkLabel(frame_p,text="VILLE DE NAISSANCE",width=100,height=10)
label_name.place(x=32,y=170)
entry_name=ctk.CTkEntry(frame_p)
entry_name.place(x=200,y=170)


label_name=ctk.CTkLabel(frame_p,text="SEXE",width=100,height=10)
label_name.place(x=1,y=210)
entry_name=ctk.CTkEntry(frame_p)
entry_name.place(x=200,y=210)

label_name=ctk.CTkLabel(frame_p,text="SEXE",width=100,height=10)
label_name.place(x=1,y=210)

root.mainloop()