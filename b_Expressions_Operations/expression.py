# Une expression est un combinasion d'opérateurs, de valeurs, de variables et d'appels de sousalgorithmes
print(1 + 2 + 3)
print(1 + 2 * 3)
print((1 + 2) * 3)

#Dans presque tous les langages de programation un réel et nul sont vus comme CONSTATNTE et sa valeur est équivalente au nombre lui-même
#LES ENTIERS (int)
print(5, 'Entier positif')
print( -42, 'Entier negarif')
print(0, 'zéro')

#LES FLOTTANTS
print(3.14159, 'nombre décimal (flottant)')
print(2.71828, 'Autre flottant')
print(-0.5)

#!!ON DOIT ÉCRIRE LES DÉCIMALS AVEC DES POINTS ET NON AVEC VERGULE

#NOTATION SCIENTIFIQUE
#Est un manière de représenter les nombres très grans ou très petits de manière compacte et lisible.


print(3.14e5, 'Équivalent à 314000')
print(3.5e-3, 'Équivalent à 0.0025')
print(6.022e23, 'Équilent à une mole')

#Pour les nombres >= 10e15, l'affichege se fait avec la représentation sicentifique.

#OPERATEURS ARITHMÉTIQUES
# | Symbole | Description |
# |   +     | Additionne  |
# |   -     | Soustrait   |
# |   *     | Multiplie   |
# |   /     | Divise      |
# |   ||    | Divise et garde seulment la partie entière|
# |   %     | Reste de la division|
# |   **    | Exponentiation(Puissance)|


#OPÉRATEURS BINAIRES (À DEUX EXPRESSIONS)
print( 1 + 2)
print((10 + 2))
#Dans ces exemples,  +  /  -  * sont des opérateurs binaires.
#Operateurs unaires
# Un operatuer unaire opère sur une seule expression. Il nécessite donc une seule entrée pour produire un résultat.
print(-1)
print(+10)

#PRIORITÉ DES OPÉRATEURS
# | NIVEAU | OPÉRATEURS            |
# |    1   |      ()
# |    2   |      **               |
# |    3   |      UNAIRES EX:(-10) |
# |    4   |      *, /, //, %      |
# |    5   |       +, - BINAIRES   |
#------------------------------------------
# |    6   |   <    |<, >>	5 << 1
# |    7   |   &    |	5 & 2
# |    8   |   ^    |	5 ^ 2
# |    9   |   |    |	5 | 2
# |   10   |comparaciones    |	5 > 2
# |   11   |   not	  |	not True
# |   12   |   and	  |	True and False
# |   13   |	or    |	True or False

#SI DEUX OPÉRATEURS ONT LA MÊME PRIORITÉ, LA PLUS À GAUCHE EST D'ABORD EXÉCUTÉ

print( 2 + 3 * 2, 'Égal 8')
print( 2 + -2 ** 2, 'Égal -2')

#Mettez des parenthèses partout
#Syntaxe définit la manière donc les instructions doivent être écrites pour que le compilateur et l'interpreteur puisse les comprendre et les éxecuter
# print("Hello World!") # Syntaxe valide!
# print('Hello World!') # Syntaxe valide!
# print("Hello World!') # Syntaxe invalide, les guillemets sont différents
# print "Hello World!"  # Syntaxe invalide, il manque les parenthèses
# PRINT("Hello World!") # Grammaire non respectée, print doit être en minuscules
# print("Hello World!"  # Syntaxe non respectée, il manque une parenthèse
# print(Hello World!)   # Syntaxe non respectée, il manque des ""
# prt("Hello World!")   # Grammaire non respectée, la commande prt n'existe pas
# print("BOnjoUR!")     # Syntaxe valide!

print(5^2)
print(5|3)

# 5 / 2 = 2  r1
# 2 / 2 = 1  r0
# 1 / 2 = 0  r1

# 2 / 2 = 1 r0
# 1 / 2 = 0 r1

# 101
# 001
# 100

# 0 = 2 ** 0 = 1
# 1 = 2 ** 1 = 2
# 1 = 2 ** 2 = 4

#OPÉRATEUR | compare les bits de deux valeurs, position par position. L'résultat est 1 si au moins un des deux bits vaut 1

# #par example 5 | 3
# 5 / 2 = 2  r1
# 2 / 2 = 1  r0
# 1 / 2 = 0  r1

# 3 / 2 = 1 r1
# 1/2  = 0 r1


# 101
# 011
# 111


# 1 = 2 ** 0 = 1
# 1 = 2 ** 1 = 2
# 1 = 2 ** 2 = 4

# 7
#OPÉRATEUR DEPLACE LES BITS << >>

5 = 101
5 << 1
#ON AJOUTE 0
1010

1 * 2 ** 3 = 8
0 * 2 ** 2 = 0
1 * 2 ** 1 = 2
0 * 2 ** 0 = 0

10
# Divides entre 2 y lees los residuos de abajo hacia arriba.
# Binario → decimal lees de izquierda a derecha, pero cada posicion tiene potencia de 2

