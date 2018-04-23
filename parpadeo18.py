#!usr/bin/env/ python
# -*- coding: UTF-8 -*-
#enciende.py
#importamos la libreria GPIO
import RPi.GPIO as GPIO
import time 
#Definimos el modo BCM 
GPIO.setmode(GPIO.BCM) 
#Ahora definimos el pin GPIO 18 como salida
GPIO.setup(18, GPIO.OUT) 
#Y le damos un valor logico alto para encender el LED
for i in range(0,3):
	print ("Encendido")
	GPIO.output(18, GPIO.HIGH)
	time.sleep(1)
	print ("Apagado")
	GPIO.output(18, GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()