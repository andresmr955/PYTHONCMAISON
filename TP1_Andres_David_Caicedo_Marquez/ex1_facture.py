# ---------------------------------------------------------
# Titre : Calcul d'une facture selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée : nom_produit, prix_unitaire, quantite_achete
# Variables de sortie : sous_total, tps, tvq, total
# ---------------------------------------------------------

#On fait un message de bienvenue
print("Bienvenue apprecie client")

#On demande les entrées au client
#on utilise float, str and int just pour être sûr que le client ne va pas mettre d'autres caractères.
nom_produit = str(input("Quel article avez vous acheté? "))
prix_unitaire = float(input("Combien coûtez votre produit? "))
quantite_achete = int(input("Combien produits avez vous acheté? "))

#Je declare deux constantes qui ne vont pas changer
TPS = 5
TVQ  = 9.75

# Je multiplie la quantité pour le prix unitaire avec le sous_total, je pourrait travailler
sous_total = prix_unitaire * quantite_achete
# Je utilise la règle de 3 pour savoir les imptôts 
tps_produit = (sous_total * TPS) / 100
tvq_produit = (sous_total * TVQ) / 100
# Je fait le total avec le sous-total plus les impôts
total = sous_total + tps_produit + tvq_produit


#J'affiche les sorties
print(f"Produit: {nom_produit} ")
print(f"Sous-total: {sous_total} $")
print(f"TPS: {tps_produit} $" )
print(f"TVQ: {tvq_produit} $")
print(f"tOTAL: {total} $")


