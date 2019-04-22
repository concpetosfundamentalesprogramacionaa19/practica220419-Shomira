"""
Ingresar por teclado 3 variables x, y , z  y mediante una formula realizar una operacion para determinar el resultado de m

"""
#Ingreso de datos
print("Ingrese el valor de la variable X :")
x=input()
print("Ingrese el valor d ela variable Y : ")
y=input()
print("Ingrese el valor de Z")
z=input()

"""
Resolucion de la operacion para determinar el resultado de m 
conversion de string a float 
"""
numerador = float (x) + (float(y) /float(z))
denominador = float (x)- (float(y) /float(z))
m=numerador / denominador 
#Salida de datos 
print ("El resultado de la operacion es %.1f " % float(m))
