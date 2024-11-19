import sqlite3
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

create_database()

def insert_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password))
    
    conn.commit()
    conn.close()

# Exemple d'ajout d'utilisateurs
insert_user('user1', 'password1')
insert_user('user2', 'password2')

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    
    user = cursor.fetchone()
    
    conn.close()
    
    if user:
        print("Connexion réussie !")
        return True
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")
        return False

# Exemple d'utilisation
username = input("Entrez votre nom d'utilisateur : ")
password = input("Entrez votre mot de passe : ")
login(username, password)
