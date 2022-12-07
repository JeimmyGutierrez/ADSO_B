'''Solicitar números al usuario hasta que ingrese el cero. 
Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).'''
def suma_digitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
num=int(input("Numero a procesar: "))
while num!=0:
    print('suma',(suma_digitos)(num))
    num=int(input("Numero a procesar: "))