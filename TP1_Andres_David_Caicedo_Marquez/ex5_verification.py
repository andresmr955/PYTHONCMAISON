# ---------------------------------------------------------
# Titre : Vérification d'un accès selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée : age_utilisateur, carte_acces
# Variables de sortie : resultat_acces
# ---------------------------------------------------------

#On demande à l'utilisateur l'âge sous forme d'un entier
age_utilisateur = int(input("Quelle âge avez vous? "))

#On demande à l'utilisateur s'il possède une carte d'accès
carte_acces = str(input("Avez vous une carte d'acces? ( OUI / NON )"))
#On déclare une variable pour pouvoir la modifier  selon la condition
resultat_acces = ""

#On fait un structure contidionnelle pour pouvoir confirmer avec operateurs de comparaison.
if age_utilisateur >= 18:
    resultat_acces = "Accès autorisé."
elif carte_acces == 'OUI':
    resultat_acces = "Accès autorisé."
else:
    resultat_acces = "Accès refusé."

#"On affiche le résultat"
print(f"Âge: {age_utilisateur}")
print(f"Carte d'accès: {carte_acces}")
print(resultat_acces)
