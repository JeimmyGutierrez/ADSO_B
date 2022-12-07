'''Escribir una función que calcule el máximo común divisor de dos números.'''
def maximo_comun_divisor(num1,num2):
    rest = 0
    while (num2 > 0):
        rest = num2
        num2 = num1 % num2
        num1 = rest
    return num1
num1=int(input('Ingresa el primer numero: '))
num2=int(input('Ingresa segundo numero: '))
print(maximo_comun_divisor(num1,num2))