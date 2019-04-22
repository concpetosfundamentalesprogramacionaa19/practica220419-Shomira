"""Ingreso de dos numeros de tipo string y convertirlos a e
nteros y mostarr la suma entre ellos y la multiplicacion
"""

print("Escriba el numero 1 : ")
numero1 =input()
print ("Escriba el numero 2 : ")
numero2= input()

suma = int(numero1) + int(numero2) #Suma de numeros convirtiendolos a enteros
multiplicacion = int (numero1) * int(numero2) #Multiplicacion de numeros convirtiendolos a enteros 

print("La suma es :  %d\t La Multiplicacion es: %d" % (suma , multiplicacion))

