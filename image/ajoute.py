import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import sqlite3

# Connectez-vous à la base de données (ou créez-la)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Créez la table si elle n'existe pas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        image_path TEXT
    )
''')

conn.commit()
conn.close()


class ImageRegistrationApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Image Registration")
        self.geometry("1270x750-1+0")

        # Labels and entry fields
        self.first_name_label = ctk.CTkLabel(self, text="First Name")
        self.first_name_label.pack(pady=5)
        self.first_name_entry = ctk.CTkEntry(self)
        self.first_name_entry.pack(pady=5)

        self.last_name_label = ctk.CTkLabel(self, text="Last Name")
        self.last_name_label.pack(pady=5)
        self.last_name_entry = ctk.CTkEntry(self)
        self.last_name_entry.pack(pady=5)

        self.age_label = ctk.CTkLabel(self, text="Age")
        self.age_label.pack(pady=5)
        self.age_entry = ctk.CTkEntry(self)
        self.age_entry.pack(pady=5)

        self.image_label = ctk.CTkLabel(self, text="No image selected")
        self.image_label.pack(pady=5)
        
        self.select_image_button = ctk.CTkButton(self, text="Select Image", command=self.select_image)
        self.select_image_button.pack(pady=5)

        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_data)
        self.save_button.pack(pady=20)

        self.image_path = None

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path = file_path
            self.image_label.configure(text=file_path)

    def save_data(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = int(self.age_entry.get())
        image_path = self.image_path

        if not image_path:
            ctk.CTkMessagebox.show_warning("Warning", "Please select an image")
            return

        # Save image to the specified folder (e.g., "images/")
        image = Image.open(image_path)
        save_path = f"images/{first_name}_{last_name}.png"
        image.save(save_path)

        # Save data to the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (first_name, last_name, age, image_path)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, age, save_path))

        conn.commit()
        conn.close()

        ctk.CTkMessagebox.show_info("Info", "Data saved successfully")

if __name__ == "__main__":
    app = ImageRegistrationApp()
    app.mainloop()



# import customtkinter as ctk
# from tkinter import filedialog
# # from PIL import Image
# import sqlite3


# def select_image():
#     file_path = filedialog.askopenfilename(title = "Select a File")
#     if file_path:
#         image_path = file_path
#         image_label.configure(text=file_path)

# def save_data():
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     age = int(age_entry.get())
#     image_path = image_path

#     if not image_path:
#         ctk.CTkMessagebox.show_warning("Warning", "Please select an image")
#         return

#     # Save image to the specified folder (e.g., "images/")
#     image = Image.open(image_path)
    
#     save_path = f"images/{first_name}_{last_name}.png"
#     image.save(save_path)

#     # Save data to the database
#     conn = sqlite3.connect('tusers.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO users (first_name, last_name, age, image_path)
#         VALUES (?, ?, ?, ?)
#     ''', (first_name, last_name, age, save_path))

#     conn.commit()
#     conn.close()

#     ctk.CTkMessagebox.show_info("Info", "Data saved successfully")
# def c():
#     # Connectez-vous à la base de données (ou créez-la)
#     conn = sqlite3.connect('tusers.db')
#     cursor = conn.cursor()

#     # Créez la table si elle n'existe pas
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT,
#             last_name TEXT,
#             age INTEGER,
#             image_path TEXT
#         )
#     ''')

#     conn.commit()
#     conn.close()







# root=ctk.CTk

# root.title("Image Registration")
# root.geometry("400x700")
# ctk.set_appearance_mode("dark")

# ctk.set_default_color_theme("blue")

# # Labels and entry fields
# first_name_label = ctk.CTkLabel(master=root, text="First Name")
# first_name_label.pack(pady=5)
# first_name_entry = ctk.CTkEntry()
# first_name_entry.pack(pady=5)

# last_name_label = ctk.CTkLabel(master=root, text="Last Name")
# last_name_label.pack(pady=5)
# last_name_entry = ctk.CTkEntry()
# last_name_entry.pack(pady=5)

# age_label = ctk.CTkLabel(master=root, text="Age")
# age_label.pack(pady=5)
# age_entry = ctk.CTkEntry()
# age_entry.pack(pady=5)

# image_label = ctk.CTkLabel(master=root, text="No image selected")
# image_label.pack(pady=5)

# select_image_button = ctk.CTkButton(master=root, text="Select Image", command=select_image)
# select_image_button.pack(pady=5)

# save_button = ctk.CTkButton(master=root, text="Save", command=save_data)
# save_button.pack(pady=20)

# save_bd = ctk.CTkButton(master=root, text="bd", command=c)
# save_bd.pack(pady=20)

        

       

    

# root.mainloop()
