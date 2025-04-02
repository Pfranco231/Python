
# creando una lista con list
lista = list(["hola","dalto",40])

cadena = "hola"


## devuelve la cantidad de elementos de la lista
resultado = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJA")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "Toma Mamá")


#agregando varios elementos a la lista
lista.extend([False,2030])


#eliminando un elemento de la lista  (por su indice)
lista.pop(0)

#eliminando un elemento de la lista  (por su indice)
lista.pop(-1)#en este caso elimina el ultimo elemento de la lista y el -2 es el ante ultimo y asi  sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("dalto")

#elimando todos los elementos de la lista
# lista.clear()

#ordena los elementos de forma ascendente, considerancion no funciona con cadenas de texto
lista2 = list([99,55,77,22,11,43,65,2,12,6,4,23,44,2222,88])
lista2.sort() #forma ascendente

# como indica su nombre da vuelta el elemento (reverse=True)
lista2.sort(reverse=True) #forma desendente

#no importa como este ordenada la lista siempre como que lo da vuelta osea der pasar a un "hola",34 a 34,"hola"
lista3 = list([99,55,77,22,"hola",True,False,"holamaquinola"])
lista3.reverse()

# print(lista)
# print(lista2)


#aqui tambien tenemos index pero busca elemtos completos
index_funcion = lista3.index(99)
print(lista3)
print(index_funcion)


