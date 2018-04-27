#!usr/bin/env/ python

"""
Lee información de Arduino mediante USB

En un circuito con 3 potenciómetros R:A0 G:A1 B:A2, lee los valores analógicos de las entradas
y los almacena en el diccionario "colores"

"""

import serial

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1.0)
red = 0
green = 0
blue = 0
colores = {"R":0,"G":0,"B":0}

try:
	while True:
		val = arduino.readline()
		cadena = []
		texto=str("")
				
		for i in range(len(val)):
			cadena.append(chr(val[i]))
		
		try:
			cadena.pop(-1)
			cadena.pop(-1)
		except:
			pass
		
		for i in range(len(cadena)):
			texto = str(texto) + str(cadena[i])
		
		valor_entrada = texto.split(":")
		
		try:
			colores[valor_entrada[0]]=int(valor_entrada[1])
		except:
			pass

		print (colores)


	    

except KeyboardInterrupt:
	print ("Programa interrumpido")
	arduino.close()