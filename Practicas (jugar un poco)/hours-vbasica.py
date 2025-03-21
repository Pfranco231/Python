#vamos a replicar a hours+ de js a phyton(version basica)

# Variables
preciohr = 3078
horas = 20
gastos = 699000

#multiplica las horas por el precio hora
resultado = horas * preciohr
# automatico resta las deudas que tengas junto al resultado final
resultado_gastos_sumado = resultado - gastos


# imprime el valor exacto antes de pasar por el condicional(if)
print(resultado_gastos_sumado)


#este es un condicional if, elif, else. en este caso si el resultado de las deudas es 0 o menor
# te dice que gastas mucho
if resultado_gastos_sumado <= 0:
    print("-----------------------")
    print(f"Horas: {horas}")
    print(f"Precio/hr: ${preciohr}")
    print(f"Ganas: ${resultado}")
    print(f"Deudas: ${gastos}")
    print(f"Resultado: ${resultado_gastos_sumado}")
    print("-----------------------")
    print("Observaciones: Gastas una banda chavon")
    print("-----------------------")
    
    
#este elif dice de que si tus resultado final de mes es menor o igual que 4000
#te advierte que estas gastando mucho
elif resultado_gastos_sumado <= 4000:
    print("-----------------------")
    print(f"Horas: {horas}")
    print(f"Precio/hr: ${preciohr}")
    print(f"Ganas: ${resultado}")
    print(f"Deudas: ${gastos}")
    print(f"Resultado: ${resultado_gastos_sumado}")
    print("-----------------------")
    print("Observaciones: y tas cortina")
    print("-----------------------")
    
#y este otro elif dice que si tenes como resultado mas o igual de 5000
#dice que administras bien el dinero
elif resultado_gastos_sumado >= 5000:
    print("-----------------------")
    print(f"Horas: {horas}")
    print(f"Precio/hr: ${preciohr}")
    print(f"Ganas: ${resultado}")
    print(f"Deudas: ${gastos}")
    print(f"Resultado: ${resultado_gastos_sumado}")
    print("-----------------------")
    print("Observaciones: Administras bien el dinero")
    print("-----------------------")
    
# no se para que se puede usar este else entonces si te aparece es por que hay un error
else:
    print("Error")
    
    


### Programa basico pero rapido a comparacion con js(eso si la de js tiene mas funcionalidades)
# pero es rapido

## NOTAS: Python es muy facil de interpretar use creo la misma logica con js pero pareciera mas facil 
# Agilidad en python lo hice muy rapido (tener en cuenta que esto es una version basica pero igual)
# menos de 5 minutos lo hice