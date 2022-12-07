'''Crea una funcion que contenga cierta cantidad de materias, pueda ingresar la nota de cada
una de ellas e imprima la materia con su respectiva nota'''
def materias():
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    nota1= []
    for materia in materias:
        nota = input("¿Qué nota has sacado en " + materia + "? ")
        nota1.append(nota)
    for i in range(len(materias)):
        print("En " + materias[i] + " has sacado " + nota1[i])
materias()