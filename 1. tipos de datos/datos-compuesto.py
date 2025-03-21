lista = ["Franco papeschi","Franqx35",True,1.85]
print(lista)

lista[3] = 1.95

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])




# tupla (no se puede modificar) como el const

tupla = ("Franco papeschi","Franqx35",True,1.85)

print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])


# usando (set) se puede modificar todo pero no por elemento por que es desordenado (no funciona como 0,1,2,3)
# es interesante por que no se puede repetir valores por ejemplo "Franco Papeschi"
conjunto = {"Franco papeschi","Franqx35",True,1.85}

#print(conjunto) > no se puede 
#

print(conjunto)



# creando un diccionario parecido a un json o un array

# a diferencia de list este no se define por 0 : "Franco papeschi" si no por el nombre asociado
diccionario = {
    'nombre' : "Franco Papeschi",
    'edad' : 32,
    'es_el_mejorxd' : True,
    'dato_duplicado' : "Franco Papeschi"
}

print(diccionario)
print(diccionario['nombre'])