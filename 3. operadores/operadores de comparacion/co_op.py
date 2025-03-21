# (==)
igual_que = 5 == 6

# (!=)
distinto_de = 5 != 6

# (>)
mayor_que = 5 > 6

# (<)
menor_que = 5 < 6

# (>=)
mayor_o_igual = 5 >= 6

# (<=)
menor_o_igual = 5 <= 6


# calculos combinados
a = 5
b = 10
c = 20
comparacion = a + b < c

print(igual_que)
print("---------")

print(distinto_de)
print("---------")

print(mayor_que)
print("---------")

print(menor_que)
print("---------")

print(mayor_o_igual)
print("---------")

print(menor_o_igual)
print("---------")

print(comparacion)

#comparar usuarios

# Usuario: Alfonsin

password_almacenada = "me_gustan_los_perros" # supongamos que es la contraseña almacenada en el servidor
password_escrita = "no_me_gustan_los_perros"

print("Su clave se esta procesando")
print(password_almacenada != password_almacenada) # va a tirar false
