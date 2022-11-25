'''Pida un numero al usuario que representa días del año. Diga a que mes del año
corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días'''
dias=int(input("Ingrese un numero para calcular el mes: "))

if dias<=31:
    print("Enero")
elif dias >31 and dias<= 60:
    print("Febrero")
elif dias >60 and dias <= 91:
    print("Marzo")
elif dias > 91 and dias <= 121:
    print("Abril")
elif dias > 121 and dias <= 152:
    print("Mayo")
elif dias > 152 and dias <= 182:
    print("Junio")
elif dias > 182 and dias <= 213:
    print("Julio")     
elif dias > 213 and dias <= 244:
    print("Agosto")
elif dias > 244 and dias <= 270:
    print("Septiembre")
elif dias > 270 and dias <= 301:
    print("Octubre")
elif dias > 301 and dias <=  331:
    print("Noviembre")
elif dias > 331 and dias <= 365:
    print("Diciembre")          
