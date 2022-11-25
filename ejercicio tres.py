'''Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
exceda los límites emita un mensaje y finalice el programa'''
k=int(input("Digita tu numero: "))

if k<=9:
    print("El numero es de una cifra")
elif k<=99:
    print("El numero es de dos cifras")    
elif k<=999:
    print("El numero es de tres cifras")
elif k<=9999:
    print("El numero es de cuatro cifras")
else:
    print("No se encuentra")   