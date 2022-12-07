'''Escribir una función que reciba un número entero positivo y devuelva su factorial'''
def factorial (n):
    f=1
    for i in range (n):
        f*=i+1
    return f
numero=int(input('¿Cual es el numero al que le quieres hallar su factorial?'))
print(factorial(numero))