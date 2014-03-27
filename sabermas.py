#!/usr/bin/python
#!encoding: UTF-8
import modulo
import sys

print "Introduzca el nombre del fichero donde se encuentran los resultados:"
nombre_fichero = raw_input ()
  

#NOTA:
#UNA FORMA DE AVERIGUAR SI UN FICHERO EXISTE O NO PUEDE SER LA SIGUIENTE
#DEBEMOS INCLUIR EL PAQUETE OS.PATH
#		IF OS.PATH.ISFILE(NOMBRE_FICHERO):
#			FICHERO = OPEN(NOMBRE_FICHERO, "A")
#		ELSE:
#			FICHERO = OPEN (NOMBRE_FICHERO, "W")
#LA OTRA FORMA PUEDE SER MEDIANTE EXCEPCIONES, ES DECIR:
try:
   fichero = open (nombre_fichero)
except:
    print "El nombre del fichero intreoducido es incorrecto"


linea = fichero.readline()
while (linea != ""):
	aproximaciones = int (linea.split()[3])
	print ("Nº de intervalos: %d" % (aproximaciones))
	for i in range (5):
		linea = fichero.readline()
		porcentaje = linea.split()[0]
		umbral = float (linea.split()[6])
		print ("%s de fallos para el umbral %2.5f" % (porcentaje, umbral))
	linea = fichero.readline()
    
    
    
    
