#AND

# And las dos tienen que ser verdaderas(true) si no tira false
Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver False
Resultado3 = True & False #Devolver False
Resultado4 = False & False #Devolver False
#OR

#OR nos va a devolver falso si las dos condiciones no se cumplen, de lo contrario de AND
Resultado5 = True | True #Devolver true
Resultado6 = False | True #Devolver true
Resultado7 = True | False #Devolver true
Resultado8 = False | False #Devolver False
#NOT

#Convierte de un valor a otro por ejemplo si es true con not es false(sencillo todo)
# Caso sencillo si 2 == 2 me va a dar falso por mas que sea verdadero
# pero si le doy 2 > 20 me va a dar true por que es falso
Resultado9 = not True #Devolver False
Resultado10 = not False #Devolver True


print(Resultado10)