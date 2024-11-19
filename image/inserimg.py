import sqlite3
from tkinter import filedialog


# def convert_to_binary_data(filename):
#     with open(filename, 'rb') as file:
#         binary_data = file.read()
#     return binary_data




def convert_to_binary_data():
    # pour ouvri le fenetre de selection
    filename = filedialog.askopenfilename(title = "Select a File")
    # with open(filename, 'rb') as file:
    #     binary_data = file.read()
    return filename


def insert_image( description):
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        
        # Créer une table si elle n'existe pas déjà
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                image BLOB NOT NULL
            )
        ''')

        # Convertir l'image en binaire
        binary_data = convert_to_binary_data()

        # Insérer l'image
        cursor.execute('''
            INSERT INTO images (description, image) VALUES (?, ?)
        ''', (description, binary_data))

        # Commit les changements
        conn.commit()
        
        print("L'image a été insérée avec succès.")
    
    except sqlite3.Error as error:
        print(f"Erreur lors de l'insertion de l'image : {error}")
    
    finally:
        if conn:
            conn.close()





def views():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM images ;
    ''')
    print(cursor.fetchall())
    # Commit les changements
    conn.commit()
    
    print("L'image a été insérée avec succès.")

        
# Exemple d'utilisation

choix=input("choix>")
if choix == "1":
    d=input('description > ')
    convert_to_binary_data()
    
    insert_image(d)
elif choix=="2":
    views()

