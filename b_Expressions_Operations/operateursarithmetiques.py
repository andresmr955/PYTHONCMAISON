# La biblithèque math de Python est une collection intégrée de fonctions mathématiques.
# Module: Una pieza de codigo reutilizable 
#Una coleccion de modulos/herramientas
# Framework Una estructura compleata para construir la aplicacion

#ARRONDISSMENT
import math 
print(math.floor(1.2), '1m goes down')
print(math.ceil(2.8), '3 goes up')

#RACIINE ET PUISSANCE

import math
print(math.sqrt(64))
print(math.pow(4, 5))

#Exponentielle et logarithmique
import math
print(math.exp(2))
print(math.log(2))
print(math.log10(2))
print(math.log(8, 2))

#Géométrique
import math

# Conversion entre degrés et radians
degrees = 90
radians = math.radians(degrees)
print(f"{degrees} degrés = {radians} radians")

rad_to_deg = math.degrees(radians)
print(f"{radians} radians = {rad_to_deg} degrés")

# Fonctions trigonométriques
print(f"sin({radians} radians) = {math.sin(radians)}")
print(f"cos({radians} radians) = {math.cos(radians)}")
print(f"tan({radians} radians) = {math.tan(radians)}")

# Arcs (fonctions inverses des trigonométriques)
print(f"asin(1) = {math.asin(1)} radians")
print(f"acos(0) = {math.acos(0)} radians")
print(f"atan(1) = {math.atan(1)} radians")

# Fonctions hyperboliques
x = 1  # Exemples pour les fonctions hyperboliques
print(f"sinh({x}) = {math.sinh(x)}")
print(f"cosh({x}) = {math.cosh(x)}")
print(f"tanh({x}) = {math.tanh(x)}")

# #Constantes
# math.pi →   la constante pi.
# math.e →   la constante d'euler.

#opérateurs arithmétiques d'affectation 

# | Op. |  Description


# | +=  |  Addition et affectation

# | -=  |  Soustraction et affectation

# | *=  |  Multiplication et affectation

# | /=  |  Division et affectation

# | //= |  Division entière et affectation

# | **= |  Puissance et affectation

# | %=  |  Modulo et affectation

y = 2
x = 7
x += y # Équivalent à x = x + y
print(x)

x = 7
x -= y # Équivalent à x = x - y
print(x)

x = 7
x *= y # Équivalent à x = x * y
print(x)

x = 7
x /= y # Équivalent à x = x / y
print(x)

x = 7
x //= y # Équivalent à x = x // y
print(x)

x = 7
x **= y # Équivalent à x = x ** y
print(x)

x = 7
x %= y # Équivalent à x = x % y
print(x)