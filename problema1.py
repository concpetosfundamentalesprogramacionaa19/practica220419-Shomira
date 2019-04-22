"""Realizar un problema que permita calcular el 
salario de un trabajador tomando en cuenta las 
horas trabajadas el valor d ecada una y descontandoi el 10% del seguro 
"""
#Ingreso de datos nombre, hotras trabahjadaas y el valor por hora 
print("CALCULO DEL SALARIO DE UN TRABAJADOR")
print("Ingrese el  nombre del trabajador o trabajadora ")
nombre=input()
print ("Ingrese el numero de horas trabajadas por:  " + nombre )
horast = input()
print("Ingrese el valor de pago por cada hora : ")
valorh = input()
#Calculo del sueldo descontando el seguro
sueldo = float(horast) * float (valorh)
seguro = float (sueldo)*0.10
sueldo = float (sueldo) - float (seguro)

#print ("El Sueldo de " + nombre + "Con una cantidad de " + horast+ "pagandole " + valorh +"por hora "+ 
	#+"El total de su sueldo descontado el seguro es de: " + sueldo )
print("EL Sueldo de  %s es: %.1f" % (nombre,sueldo))