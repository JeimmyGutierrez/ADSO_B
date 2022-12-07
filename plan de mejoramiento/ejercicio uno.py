'''pedir tres numeros e indicar cual de ellos es el valor del medio'''
w=int(input("ingrese el primer numero: "))
e=int(input("ingrese el segundo numero: "))
r=int(input("ingrese el tercer numero: "))
if w>e and w>r:
    print(e)
elif r>e and e>w:
    print(e)
elif r>w and w>e:
    print(w)
elif e>w and w>r:
    print(w)
elif w>r and r>e:
    print(r)
elif e>r and r>w:
    print(r)
    