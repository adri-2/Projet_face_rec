from tkinter import *
import customtkinter as ctk
from subprocess import call

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")


def view_liste():
    root.destroy()
    call(["python","liste.py"])
def view_ajoute():
    root.destroy()
    call(["python","ajoute.py"])
def view_search():
    root.destroy()
    call(["python","search.py"])



root = ctk.CTk()
root.geometry("700x600")
root.title("Acceuil")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20,padx=40,fill='both',expand=True)

btn_liste=ctk.CTkButton(master=frame,text="liste",command=view_liste).pack(padx=30,pady=70)
btn_reach=ctk.CTkButton(master=frame,text="reach",command=view_search).pack(padx=30,pady=70)
btn_save=ctk.CTkButton(master=frame,text="save",command=view_ajoute).pack(padx=30,pady=70)



root.mainloop()