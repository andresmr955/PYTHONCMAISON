# ---------------------------------------------------------
# Titre : Resultat d'un étudiant selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée : nom_etudiant, note_examen
# Variables de sortie : echec, reussite
# ---------------------------------------------------------

#Ici, on demande le nom en type string
nom_etudiant = str(input("Comment vous appelez vous? "))
#Ici, on demande la note en float
note_examen = float(input("Quelle est la note obtenue dans votre examen? "))
#On initialise un variable pour pouvoir la modifier
resultat = ""

#On utilise une structure conditionnelle pour vérifier si la note est superieur
if note_examen >= 60:
    #Si la note est suffisante ou supérieur, on garde le châine de caractères de réussite dans la variable resultat
    resultat = f"{nom_etudiant}, vous avez réussi l'examen"
else:
    #Si la note est inferieur, on garde la châine de caracters  de échec dans la variable resultat
    resultat = f"{nom_etudiant}, vous avez échoué l'examen"

#On affiche le resultat et la note
print(resultat)
print(f"Votre note est: {note_examen}")