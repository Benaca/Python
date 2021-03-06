#Detector vehículo

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
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

print ("Sensor ultrasónico HC-SR04")

rojo = GPIO.PWM(16, 100)
verde = GPIO.PWM(18,100)

rojo.start(0)
verde.start(0)


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

		if distancia < 20 and distancia > 10:
			presencia_vehiculo = True
		else:
			presencia_vehiculo = False

		if presencia_vehiculo:
			rojo.ChangeDutyCycle(0)
			verde.ChangeDutyCycle(100)
		else:
			rojo.ChangeDutyCycle(100)
			verde.ChangeDutyCycle(0)


except KeyboardInterrupt:
	GPIO.cleanup()


