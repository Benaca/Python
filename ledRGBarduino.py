#!usr/bin/env/ python

"""
Lee información de Arduino mediante USB

En un circuito con 3 potenciómetros R:A0 G:A1 B:A2, lee los valores analógicos de las entradas
y los almacena en el diccionario "colores"

Luego usa estos valores para controlar un led RGB conectado a los GPIO R:18 G:23 B:24

"""

import serial
import RPi.GPIO as GPIO 

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1.0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT)  

red = GPIO.PWM(18, 100)
green = GPIO.PWM(23,100)
blue = GPIO.PWM(24,100)

red.start(0)
green.start(0)
blue.start(0)

colores = {"R":0,"G":0,"B":0}

try:
	while True:
		val = arduino.readline()
		cadena = []
		texto=str("")
		
		#Convierte los valores ASCII en caracteres y los almacena en "cadenas"		
		for i in range(len(val)):
			cadena.append(chr(val[i]))
		
		#Elimina los 2 últimos caracteres leidos "Retorno de carro" y "Salto de línea"
		try:
			cadena.pop(-1) 
			cadena.pop(-1)
		except:
			pass
		
		#Convierte la cadena en un string
		for i in range(len(cadena)):
			texto = str(texto) + str(cadena[i])
		
		#Separa el nombre de la variable de su valor y lo almacena en una lista
		valor_entrada = texto.split(":")
		
		#Almacena cada valor en su lugar correspondiente del diccionario "colores"
		try:
			colores[valor_entrada[0]]=int(valor_entrada[1])*100//1023
		except:
			pass

		#print (colores)

		#Controla el led RGB con los valores almacenados en "colores"
		red.ChangeDutyCycle(int(colores["R"]))
		green.ChangeDutyCycle(int(colores["G"]))
		blue.ChangeDutyCycle(int(colores["B"]))



except KeyboardInterrupt:
	print ("\nPrograma interrumpido")
	arduino.close()
	GPIO.cleanup()



	