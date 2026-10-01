# ---------------------------------------------------------
# Titre : Conversion de temps selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée : nombre_sec
# Variables de sortie : heures, minutes, secondes
# ---------------------------------------------------------
'''
On demande à l'utilisateur le nombre de secondes à convertir
'''
nombre_sec = int( input("Donnez moi un nombre de sec: => "))

#On prends l'entrée de l'utilisateur et on la divise entre le nombre de seconds qu'il y a 
# dans un heure. On utilise // pour avoir la partie entière.
heures = nombre_sec // 3600
#On prend le reste de la même division précédente pour savoir, combien minutes et 
# seconds restent.
rest_sec = nombre_sec % 3600
#On prend le rest des secondes et on le divise pour 60 pour obtenir les minutes exacts.
minutes = rest_sec // 60
#On prend le rest pour savoir avec module combien de secondes ils restent.
secondes = rest_sec % 60

#On affiche les heures, les minutes et les secondes.
print(f"Les nombres de seconds données: {nombre_sec}")
print(f"Heures: {heures}")
print(f"Minutes: {minutes}")
print(f"Secondes: {secondes}")