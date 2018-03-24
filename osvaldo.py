#!/usr/bin/env python
def sumar(x, y):
	print "El resultado de sumar "+str(x)+ " y "+str(y)+ " es: "+str((x+y))

def restar(x, y):
        print "El resultado de restar "+str(x)+ " y "+str(y)+ " es: "+str((x-y))

def multiplicar(x, y):
        print "El resultado de multiplicar "+str(x)+ " y "+str(y)+ " es: "+str((x*y))

def dividir(x, y):
        print "El resultado de dividir "+str(x)+ " y "+str(y)+ " es: "+str((x/y))


def menu():
	print "***La calculadora de ODMA***"
	print " "
	print "escoja una opcion"
	print "1-Sumar"
	print "2-Restar"
	print "3-Multiplicar"
	print "4-Dividir"
	print "0-Salir"
	return int(input("introduce tu opcion: "))
while(True):
	opcion = menu()
	if (opcion==0):
		break
	else:
		num1 = int(input("ingrese el primer numero: "))
		num2 = int(input("ingrese el segundo numero: "))
		if(opcion==1):
			sumar(num1, num2)
		elif(opcion==2):
			restar(num1, num2)
		elif(opcion==3):
			multiplicar(num1, num2)
		elif(opcion==4):
			dividir(num1, num2)
		else:
			print "Opcion incorrecta."
print "ADIOS!"
