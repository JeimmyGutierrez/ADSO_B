'''Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores'''
nota=int(input("Ingresa la nota: "))
if nota <= 2:
    print("Insuficiente")
elif nota<= 6:
    print("Bajo")     
elif nota<= 7.5:
    print("Basico")
elif nota <= 8.9:
    print("Alto")
elif nota <= 10:
    print("Superior")   