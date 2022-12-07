'''Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando
si la dirección es válida o no, valiéndose de una función para decidirlo.
Una dirección se considerará válida si contiene el símbolo "@".'''
def validacion (email):
    direccion="@"
    for c in email:
        if c == direccion:
            return True
        else:
            return False
email=input('Ingresa tu email: ')
if validacion(email):
    print('direccion valida')
else:
    print('direccion invalida')
print(validacion(email))