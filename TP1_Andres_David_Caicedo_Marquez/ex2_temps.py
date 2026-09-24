# ---------------------------------------------------------
# Titre : Conversion de temps selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée : nombre_sec
# Variables de sortie : heures, minutes, secondes
# ---------------------------------------------------------

nombre_sec = int( input("Donnez moi un nombre de sec: => "))

heures = nombre_sec // 3600
rest_sec = nombre_sec % 3600
minutes = rest_sec // 60
secondes = rest_sec % 60

print(heures)
print(minutes)
print(secondes)