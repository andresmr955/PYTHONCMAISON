# ---------------------------------------------------------
# Titre : Système de notation selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée :  nom_employee, nombre_annees, evalu_annuelle
# Variables de sortie :  note_evaluation, prime
# ---------------------------------------------------------

nom_employee = str(input("Comment vous appelez-vous? "))
nombre_annees = int(input("Combien d'années d'experience avez vous? "))
evalu_annuelle = int(input("Quelle est votre note d'évaluation annuelle? "))
note_evaluation = ""
prime = ""

#On verifie en premier si l'evaluation annuelle est superier à 60, sinon il passe à else
if evalu_annuelle >= 60:
    note_evaluation = "Réussie"
    #On don
    if nombre_annees >= 5:
        prime = "10 %"
    else:
        prime = "5 %"
else:
    note_evaluation = "Échoué"
    prime = "Vous n'êtes pas admissible à une prime"


print(f"Évaluation: {note_evaluation}")
print(f"Experience: {nombre_annees} ans.")
print(f"Prime: {prime}")

## Porquoi dans l'exercise 5 on donne accès s'il n'y a pas carte d'accès
## Porquoi on doit montre deux fois l'experience dans l'exercise 6