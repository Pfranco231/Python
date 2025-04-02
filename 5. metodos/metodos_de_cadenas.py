cadena1 = "Hola"
cadena2 = "Bienvenido Maquinola"

#muestra todos los atributos disponibles

# print(dir(["lista de objetos"]))

# resultado = dir(cadena1)

#convierte todo a mayus
mayusc = cadena1.upper()
# resultado2 = "hola gente como estas todo bien".upper()

#de este modo convierte todo a minus
minusc = "HOLA GENTE COMO ESTAN".lower()

#Primero convierte todo a minus y depues la primera letra en mayus
primer_letra_mayusc = "hola".capitalize()

#busquemos un caracter en una cadena, si no hay concidencia nos devuelve -1
busqueda_find = cadena1.find("F")

#busquemos un caracter en una cadena, si no hay concidencia nos lanza una excepcion
######## busqueda_index = cadena1.index("4")

# si es numerico, devuelve true, si no vuelve flase
es_numerico = cadena1.isnumeric()

# esto devuelve si es alfa numerico(numeros con letras) 
######## es_alfa_numerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("a")


#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("2")


#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("Hola", "Hola mi gente como esta")

### Pequeño Programa
### String con todas la letras empezando con mayus y con coma en vez de espacio
cadenas = "Hola,Maquina,Como,Estas"
## se modifica la cadena para remplazar el coma por espacios
cadena_modificada = cadenas.replace(","," ")
## y la ultima manera corrige todas las letra para que solo la primera se la mayus en este caso Hola maquina como estas
cadena_mejorada = cadena_modificada.capitalize()

## Imprimimos resultados
# print(cadena_mejorada) 


##El Split separa todo en listas ej:
cadena_separada = cadenas.split(",")


# incluso podemos elegir que nos muestre que hay en el 1 o 0 o cualquiera
print(cadena_separada[0])
##  aqui podemos observar que tipo covierte el split en este caso lista
print(type(cadena_separada))