# ---------------------------------------------------------
# Titre : Admissibilité à un programme selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée :  moyenne_general, resultat_entrevue, nombre_dabsencess
# Variables de sortie :   resultat
# ---------------------------------------------------------


moyenne_general = int(input("Quelle est votre moyenne général? "))
resultat_entrevue = input("Entrevue réussi?  (OUI,oui/ NON,non) ")
nombre_dabsencess = int(input("Combien absences avez vous? "))

resultat = ""
resultat_entrevue = resultat_entrevue.lower()
print(resultat_entrevue)
if moyenne_general >= 70:
    if resultat_entrevue == "oui":
        if nombre_dabsencess < 10:
            resultat = "Vous respectez les critères d'admission"
        else:
            resultat = "Vous ne respectez le critère d'absences"
    else:
        resultat = "Vous ne respectez le critère de resultat de l'entrevue"
else:
    resultat = "Vous ne respectez le critères d'admission."

print('*' * 100)
print('Moyenne: ', moyenne_general)
print('Entrevue réussie: ', resultat_entrevue)
print("Nombre d'absence: ", nombre_dabsencess)
print("Résultat", resultat)