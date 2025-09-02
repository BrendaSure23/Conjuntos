
conjunto_a = {1, 2, 3, 5, 9}

conjunto_b = {1, 4, 6, 7, 5}

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
#elementos que se encuentran en A o en B, o en ambos.

print(conjunto_a | conjunto_b)

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
#elementos que se encuentran en A y en B

print(conjunto_a & conjunto_b)

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
#conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

print(conjunto_b - conjunto_a)

#Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
#un subconjunto de otro conjunto, B

print(conjunto_b.issubset(conjunto_a)) #False

#otro ejemplo con True
conjunto_c = {"Leo", "Gonzalo", "Juan", "Gastón"}
conjunto_d = {"Gonzalo", "Leo"}

print(conjunto_d.issubset(conjunto_c))

#Dados un conjunto, A, escribe un programa en Python que imprima el número de
#elementos del conjunto.

print(len(conjunto_a))
