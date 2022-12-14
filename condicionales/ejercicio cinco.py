'''En un juego de preguntas a las que se responde “Si” o “No” gana quien
responda correctamente las tres preguntas. Si se responde mal a cualquiera de
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de Colombia fue en el año 1810?
3. The Doors fue un grupo de rock Americano?'''

si="correcto"
no="incorrecto" 
pregunta1=(input("¿colon descubrio America?: "))
if pregunta1!= si:
    print("respuesta correcto")
else:
    print("respuesta incorrecta") 
pregunta2=(input("La independencia de Colombia fue en el año 1810?: "))
if pregunta2!= si:
    print("la respuesta es correcta")
else:
    print("la respuesta es incorrecta")
pregunta3:(input("The Doors fue un grupo de rock Americano?: "))
if pregunta3!= no:
    print("la respuesta es correcta")
else:
    print("la respuesta es incorrecta")

