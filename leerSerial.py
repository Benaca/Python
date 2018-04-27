#!usr/bin/env/ python

#Lee la información recibida por el USB
#Se usa para leer el serial de un Arduino conectaodo a la Raspberry mediante USB


import serial

arduino = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1.0)


try:
	while True:
	    val = arduino.readline()

	    try:
	    	print(val)
	    except:
	    	pass
	    

except KeyboardInterrupt:
	print ("Programa interrumpido")
	arduino.close()