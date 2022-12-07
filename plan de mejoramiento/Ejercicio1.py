def vocales (i):
    vocales= ['a','e','i','o','u','k','l','y','j']
    if i in vocales:
        print ('La letra ingresada se encuentra en la lista')
    elif i not in vocales:
        print('La letra ingresada no coincide con ningun elemento de la lista')
i=input('Ingresa una letra: ')
vocales(i)