'''Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña 
y te devuelve Verdadero si el nombre de usuario es “yura” 
y la contraseña es “tom”. Además recibe el número de intentos 
que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.'''
def login (usuario,contrasena):
    if usuario == "yura" and contrasena =="tom":
        print(f'El usuario {usuario} es correcto y la contraseña {contrasena} tambien es correcta')
    else:
        print("El usuario o la contraseña son incorrectos")

h=input("¿Cual es tu nombre de usuario? ")
j=input("¿Cual es tu contraseña? ")
login(h,j)