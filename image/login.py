import customtkinter as ctk
import tkinter.messagebox as tkmb


# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x500-1+0")
app.title("Modern Login UI using Customtkinter")


def login():
	conn = sqlite3.connect('users.db')
	cursor = conn.cursor()

	cursor.execute('''
	       SELECT * FROM users WHERE username = ? AND password = ?
	   ''', (username, password))

	user = cursor.fetchone()

	conn.close()
	new_window = ctk.CTkToplevel(app)

	new_window.title("New Window")

	new_window.geometry("350x150")

	if user_entry.get() == username and user_pass.get() == password:
		tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
		ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack()
	elif user_entry.get() == username and user_pass.get() != password:
		tkmb.showwarning(title='Wrong password',message='Please check your password')
	elif user_entry.get() != username and user_pass.get() == password:
		tkmb.showwarning(title='Wrong username',message='Please check your username')
	else:
		tkmb.showerror(title="Login Failed",message="Invalid Username and password")



label = ctk.CTkLabel(app,text="This is the main UI page")

label.pack(pady=20)


frame = ctk.CTkFrame(master=app)
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


app.mainloop()
