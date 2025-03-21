ingreso_mensual = 81000
gasto_mensual = 80000

# ejemplo de elif 

if ingreso_mensual > 10000:
    # con if anidado
    
    print("estas bien en cualquier parte del mundo pero cuanto gastas???--- hay que ver dejame revisar")
    
    if ingreso_mensual - gasto_mensual < 0:
        
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual >= 3000:
        
        print("tas bastante bien")
    else:
        
        print("y estas gastando una banda")
        
elif ingreso_mensual > 1000: # else if es elif en python
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en argentina")
elif ingreso_mensual > 200:
    print("estas bien en venezuela")
else:
    print("sos pobre")