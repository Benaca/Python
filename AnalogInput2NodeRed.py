"""
Lee información de Arduino mediante USB

En un circuito con 3 potenciómetros R:A0 G:A1 B:A2, lee los valores analógicos de las entradas
y los almacena en el diccionario "colores"

Luego usa estos valores para controlar un led RGB conectado a los GPIO R:18 G:23 B:24

Además, envía la información a Node-Red

"""


#!usr/bin/env/ python
# -*- coding: UTF-8 -*-

import serial
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import sys

time.sleep(5) #Sleep to allow wireless to connect before starting MQTT

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1.0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT)  

username = "pi"
clientid = "RGB" 

# Arrancar cliente mqtt 
mqttc = mqtt.Client(client_id=clientid)
mqttc.connect("localhost")

# Arrancar pines GPIO
red = GPIO.PWM(18, 100)
green = GPIO.PWM(23,100)
blue = GPIO.PWM(24,100)

red.start(0)
green.start(0)
blue.start(0)

colores = {"R":0,"G":0,"B":0}

mqttc.loop_start()

# Create the route for the topics

topic_color_red = "v1/" + username + "/things/" + clientid + "/data/1"
topic_color_green = "v1/" + username + "/things/" + clientid + "/data/2"
topic_color_blue = "v1/" + username + "/things/" + clientid + "/data/3"

t0 = int(100*time.clock())

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

		#Publicar datos mediante mqtt
		t1=int(100*time.clock())

		if t0!=t1:
			t0=t1
			if colores["R"] is not None:
				mqttc.publish(topic_color_red, payload=colores["R"], retain=True)
			if colores["G"] is not None:
				mqttc.publish(topic_color_green, payload=colores["G"], retain=True)
			if colores["B"] is not None:
				mqttc.publish(topic_color_blue, payload=colores["B"], retain=True)

		

		#print("t0=",t0," t1=",t1)
		#print (10*time.clock())
		#time.sleep(1)



except KeyboardInterrupt:
	print ("\nPrograma interrumpido")
	arduino.close()
	GPIO.cleanup()
	mqttc.disconnect()
	sys.exit()



	