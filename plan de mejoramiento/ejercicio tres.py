'''pedir un numero entre 0 y 9,999 y decir cuantas cifras tiene. 
cuando el numero exceda los limites emite un mensaje y finalice el programa'''
k=int(input("digite un numero: "))
if k<=9: 
    print("el numero es de una cifra")
elif k<=99:
    print("el numero es de dos cifras")
elif k<=999:
    print("el numero es de tres cifras")
elif k<=9999:
    print("el numero es de cuatro cifras")
elif k<=99999:
    print("ERROR")