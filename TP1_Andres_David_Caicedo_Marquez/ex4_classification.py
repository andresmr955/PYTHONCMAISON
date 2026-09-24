# ---------------------------------------------------------
# Titre : Clasification d'un nombre selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée : nombre_entier
# Variables de sortie : classification
# ---------------------------------------------------------

#On demande le nombre entier à l'utilisateur
nombre_entier = int(input("Entrez un nombre entier?  "))
#On déclare une variable pour stocker la clasification.

classification = ""

#On utilise une structure conditionnelle pour clasifiquer le nombre
# On utilise >, < pour vérifier si le nombre est positif ou négatif 
# L'operateur modulo nous aid à savoir si la chiffre est impair ou pair
if nombre_entier > 0 and nombre_entier % 2 == 0:
    classification = "positif et pair. "
elif nombre_entier > 0 and nombre_entier % 2 != 0:
    classification = "positif et impair. "
elif nombre_entier < 0 and nombre_entier % 2 == 0:
    classification = "négatif et pair"
elif nombre_entier < 0 and nombre_entier % 2 != 0:
    classification = "négatif et impair"
else:
    classification = "égal à zéro"

print(f"Le nombre {nombre_entier} est {classification}")
