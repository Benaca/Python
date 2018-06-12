#Medir distancia usando un sensor ultrasónico

import RPi.GPIO as GPIO
import time

#!usr/bin/env/ python
# -*- coding: UTF-8 -*-

#configuración de los pines

GPIO.setmode(GPIO.BOARD)

Trigger = 10
Echo = 12

GPIO.setup(Trigger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

print ("Sensor ultrasónico HC-SR04")

try:
	while True:
		#Establece el trigger en bajo y deja al módulo tiempo para resolver
		GPIO.output(Trigger, False)
		time.sleep(0.5)

		#manda pulso de ultrasonido y registra el tiempo
		GPIO.output(Trigger, True)
		time.sleep(0.00001)
		GPIO.output(Trigger, False)
		inicio=time.time()

		while GPIO.input(Echo)==0:
			inicio=time.time()

		while GPIO.input(Echo)==1:
			final=time.time()

		#calcula el tiempo transcurrido
		t_transcurrido = final - inicio

		#calcula distancia
		distancia = t_transcurrido*34000/2

		print ("Distancia = %.1f cm"%distancia)

except KeyboardInterrupt:
	GPIO.cleanup()


