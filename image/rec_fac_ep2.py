from PIL import Image, ImageDraw, ImageFont,ImageTk
import face_recognition
import numpy as np
import tkinter as tk

root = tk.Tk()
root.title("recognition")
root.geometry("1000x800")
# Chargez un exemple d'image et apprenez a la reconnaitre
image_bieber = face_recognition.load_image_file("image/bieber.jpg")
encodage_visage_bieber = face_recognition.face_encodings(image_bieber)[0]
image_guetta = face_recognition.load_image_file("image/guetta.jpg")
encodage_visage_guetta = face_recognition.face_encodings(image_guetta)[0]

# Creer une liste d'encodages de visage connus et leurs noms
encodage_visage_connu = [
    encodage_visage_guetta,
    encodage_visage_bieber
]
nom_visage_connu = [
    "David Guetta",
    "Justin Bieber"
]

# Charger une image avec un visage inconnu
image_inconnu = face_recognition.load_image_file("image/Bieber_0.jpg")

# Trouver tous les visages et encodages de visage dans l'image inconnue
emp_visage_inconnu = face_recognition.face_locations(image_inconnu)
encodage_visage_inconnu = face_recognition.face_encodings(image_inconnu, emp_visage_inconnu)

image_pil = Image.fromarray(image_inconnu)
draw = ImageDraw.Draw(image_pil)

# Traverser chaque visage trouve dans l'image inconnue
for (haut, droite, bas, gauche), encodage_visage in zip(emp_visage_inconnu, encodage_visage_inconnu):
    # Voir si le visage correspond au visage connu
    corresp = face_recognition.compare_faces(encodage_visage_connu, encodage_visage)
    # [True, False]
    
    nom = "Inconnu"

    # Ou a la place, utilisez le visage connu avec la plus petite distance par rapport au nouveau visage
    distances_visages = face_recognition.face_distance(encodage_visage_connu, encodage_visage)
    meilleur_indice = np.argmin(distances_visages)
    if corresp[meilleur_indice]:
        nom = nom_visage_connu[meilleur_indice]

    # Dessinez une boite autour du visage a l'aide du module Pillow
    draw.rectangle(((gauche, haut), (droite, bas)), outline=(0, 0, 255))

    # Dessinez une etiquette avec un nom sous le visage
    #largeur_texte, hauteur_texte = (234,344)
    # choisir la police de caractere du texte
    ft=ImageFont.truetype("arial.ttf",25)
    draw.text((gauche + 6, bas + 15), nom, fill=(255, 255, 255, 255),font=ft)


# Afficher l'image resultante
#plt.show(image_pil)
#image_pil.show()
photo = ImageTk.PhotoImage(image_pil)
wondows = tk.Label(root, image=photo)
wondows.place(x=0,y=0)
root.mainloop()
#image_pil.save("im2.jpg") #- Enregistrer l'image
