# ---------------------------------------------------------
# Titre : Minicalculatrice selon Andres
# Auteur : Andres David Caicedo Marquez
# Date : 2026-10-01
# Variables d'entrée :   premier_nombre, deuxieme_nombre, operation_choisi
# Variables de sortie :  resultat_operation
# ---------------------------------------------------------

premier_nombre = int(input("Saisiez un premier nombre: "))
deuxieme_nombre = int(input("Saisiez un deuxieme nombre: "))
operation_choisi = str(input("Choisisiez une operation: (+,-,*,/)"))

match operation_choisi:
    case '+':
        resultat_operation = premier_nombre + deuxieme_nombre
    case '-':
        resultat_operation = premier_nombre - deuxieme_nombre
    case '*':
        resultat_operation = premier_nombre * deuxieme_nombre
    case '/':
        if deuxieme_nombre != 0:            
            resultat_operation = premier_nombre / deuxieme_nombre
        else:
            resultat_operation =  "Erreur: Division par zéro impossible"
    case _:
        resultat_operation= "Operation Invalide"

print(f"Votre premier nombre : {premier_nombre} {operation_choisi} deuxième nombre {deuxieme_nombre} = {resultat_operation}" )
