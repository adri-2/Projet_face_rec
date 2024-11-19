import customtkinter as ctk
from subprocess import call
import tkinter.messagebox as tkmb


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x500")
root.title("Modern Login UI using Customtkinter")

def login():
        username = user_entry.get()
        password = user_pass.get()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM users WHERE username = ? AND password = ?
        ''', (username, password))

        user = cursor.fetchone()

        conn.close()

        if user: 
            tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")  
            messagebox.showinfo("", "Bienvenue à vous " + surnom)
            user_entry.delete("0", "end")
            user_pass.delete("0", "end")
            root.destroy()
            call(["python", "acceuil.py"])
        elif user==None: 
            tkmb.showerror("", "il faut rentrer les Données")
            user_entry.delete("0", "end")
            user_pass.delete("0", "end")
        else: 
            tkmb.showerror(title="Login Failed",message="Invalid Username and password") 



label = ctk.CTkLabel(root,text="This is the main UI page")

label.pack(pady=20)


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20,padx=40,fill='both',expand=True)

label = ctk.CTkLabel(master=frame,text='Modern Login System UI')
label.pack(pady=12,padx=10)


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)


button = ctk.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)


root.mainloop()
