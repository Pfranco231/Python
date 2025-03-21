a = 2
b = 3
c = a + b

print(c)


nombre = "Franco Papeschi"

print(nombre)


numero = 10
numero += 5
# numero = 10 + 5

numero1 = 10
numero1 -= 5
# numero = 10 - 5
print(numero1)

nombre = "Franco"
bienvenida = "Hola, " + nombre + " ¿Como estas?"
print(bienvenida)

# Parecido a los backticks de js
nombre1 = "Franco"
# concatenar con +
bienvenida2 = f"Hola, {nombre1} ¿Como estas?"
del bienvenida2 # borrar variable
# print(bienvenida2)

#operadores de pertenencia (in /not in)

productos = "manzana, pera, durazno, banana"
print("manzana" in productos)

productos2 = "laptop"
print("manzana" not in productos2)


# la recomendacion oficial de python no es usar camelcase si no snake

pcGamer = "ryzen 9" # asi no es recomendado (buenas practicas)

pc_gamer = "ryzen thipperhidden" # asi es recomendado por python 