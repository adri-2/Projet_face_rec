import customtkinter as ctk

root = ctk.CTk()

root.title("MENUE PRINCIPALE")
# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("light")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

root.geometry("1850x900-1+0")

ctk.CTkFrame(root).pack()

#titre
ctk.CTkLabel(root,)


root.mainloop()