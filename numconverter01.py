#Recibe un valor en número romanos y devuelve un entero o viceversa

#! /usr/bin/python
# -*- coding: UTF-8 -*-

from colorama import init, Fore, Back, Style

init()

claves = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}

car_dec2hex = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

car_hex2dec = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

#Función romanizar devuelve un número romano a partir de un valor decimal
def dec2rom (valor):

	def rom_uds_millar (valor):
		rom = ""
		repeticiones = int(valor/1000)
		while repeticiones > 0:
			rom = rom + "M"
			repeticiones = repeticiones -1
		return rom

	def rom_centenas (valor):
		rom = ""
		while valor >= 1000:
			valor = valor - 1000
		if valor >= 900:
			rom = "CM"
			valor = valor - 900
		if valor >= 500:
			rom = "D"
			valor = valor - 500
		if valor >= 400:
			rom = rom + "CD"
		else:
			repeticiones = int(valor/100)
			while repeticiones > 0:
				rom = rom + "C"
				repeticiones = repeticiones -1
		return rom

	def rom_decenas (valor):
		rom = ""
		while valor >= 1000:
			valor = valor - 1000
		while valor >= 100:
			valor = valor - 100
		if valor >= 90:
			rom = "XC"
			valor = valor - 90
		if valor >= 50:
			rom = "L"
			valor = valor - 50
		if valor >= 40:
			rom = rom + "XL"
		else:
			repeticiones = int(valor/10)
			while repeticiones > 0:
				rom = rom + "X"
				repeticiones = repeticiones -1
		return rom

	def rom_uds (valor):
		rom = ""
		while valor >= 1000:
			valor = valor - 1000
		while valor >= 100:
			valor = valor - 100
		while valor >= 10:
			valor = valor - 10
		if valor == 9:
			rom = "IX"
			valor = valor - 9
		if valor >= 5:
			rom = "V"
			valor = valor - 5
		
		if valor == 4:
			rom = rom + "IV"
		else:
			repeticiones = int(valor)
			while repeticiones > 0:
				rom = rom + "I"
				repeticiones = repeticiones -1
		return rom

	num_rom = str(rom_uds_millar(valor))+str(rom_centenas(valor))+str(rom_decenas(valor))+str(rom_uds(valor))

	return num_rom


# Función es_romano comprueba si el número romano introducido es correcto. Número correcto = True. Incorrecto = False
def es_romano(valor):  
	cifras=[]
	contador = 0

	# 1. Comprobar que no haya caracterer distintos a los usados en los números romanos. Si encuentra caracteres no permitidos devuelve False
	for i in valor:				
		if i in claves:
			pass
		else:
			return False

	# 2. Crear una lista que contenga las "cifras" del número, ya sean simples (M, C, D,...) o dobles (CM, IX,...)
	for i in range(len(valor)):
		if i == 0:
			cifras.append(valor[i])
		else:
			if (str(str(valor[i-1])+str(valor[i])) in claves):
				cifras.pop()
				cifras.append(str(str(valor[i-1])+str(valor[i])))
			else:
				cifras.append(valor[i])

    # 3. Comprobar las restricciones en cuanto al órden de las cifras en los números romanos. Si encuentra alguna combinación no permitida devuelve False
	for i in range(len(cifras)):
		if i>0:
			if cifras[i]=="M":
				if cifras[i-1] in ["M"]:
					pass
				else:
					return False
			elif cifras[i]=="D":
				if cifras[i-1] in ["M"]:
					pass
				else:
					return False
			elif cifras[i]=="C":
				if cifras[i-1] in ["M","D","C"]:
					pass
				else:
					return False
			elif cifras[i]=="L":
				if cifras[i-1] in ["M","D","C","CM","CD"]:
					pass
				else:
					return False
			elif cifras[i]=="X":
				if cifras[i-1] in ["M","D","C","L","X","CM","CD"]:
					pass
				else:
					return False
			elif cifras[i]=="V":
				if cifras[i-1] in ["M","D","C","L","X","CM","CD","XC","XL"]:
					pass
				else:
					return False
			elif cifras[i]=="I":
				if cifras[i-1] in ["M","D","C","L","X","V","I","CM","CD","XC","XL"]:
					pass
				else:
					return False
			elif cifras[i]=="CM":
				if cifras[i-1] in ["M"]:
					pass
				else:
					return False
			elif cifras[i]=="CD":
				if cifras[i-1] in ["M"]:
					pass
				else:
					return False
			elif cifras[i]=="XC":
				if cifras[i-1] in ["M","D","C","CM","CD"]:
					pass
				else:
					return False
			elif cifras[i]=="XL":
				if cifras[i-1] in ["M","D","C","CM","CD"]:
					pass
				else:
					return False
			elif cifras[i]=="IX":
				if cifras[i-1] in ["M","D","C","L","X","CM","CD","XC","XL"]:
					pass
				else:
					return False
			elif cifras[i]=="IV":
				if cifras[i-1] in ["M","D","C","L","X","CM","CD","XC","XL"]:
					pass
				else:
					return False
			# 4. Comprobar que ninguna cifra se repita más de 3 veces. En caso contrario devuelve False
			if cifras[i]==cifras[i-1]:
				contador=contador + 1
				if contador >= 3:
					return False
			else:
				contador = 0
			
	# 5. Si no ha encontrado ningún problema en las comprobaciones anteriores, devuelve True
	return True

#Devuelve el valor decimal del número romano introducido
def rom2dec (valor):   
	# Para que funcione correctamente, se debe haber comprobado que el número romano es correcto mediante la función es_romano	

	# 1. Inicia las variables
	cifras=[]
	suma = 0
	
	# 2. Crear una lista que contenga las "cifras" del número, ya sean simples (M, C, D,...) o dobles (CM, IX,...)
	for i in range(len(valor)):
		if i == 0:
			cifras.append(valor[i])
		else:
			if (str(str(valor[i-1])+str(valor[i])) in claves):
				cifras.pop()
				cifras.append(str(str(valor[i-1])+str(valor[i])))
			else:
				cifras.append(valor[i])

	# 3. Suma las cifras según su valor en el diccionario Claves
	for i in cifras:
		suma = suma + claves[i]

	return suma


#Convierte un valor decimal a binario
def dec2bin(decimal):
	digitosbin=[]
	dividendo = int(decimal)
	numbin=""

	while dividendo >= 1:
		digitosbin.append(dividendo%2)
		dividendo=dividendo//2
	
	for i in range(len(digitosbin)-1, -1, -1):
		numbin= numbin + str(digitosbin[i])

	return numbin

#Convierte un valor binario a decimal
def bin2dec(valor):
	numdec=0
	digitosbin=[]
	exp=0

	for i in range(len(valor)):
		digitosbin.append(valor[i])


	for i in range(len(digitosbin)-1, -1, -1):
		numdec=numdec+(int(digitosbin[i])*(2**exp))
		exp=exp+1
		
	return numdec

#Comprueba si un valor es binario
def esbinario(valor):

	for i in range(len(valor)):
		if int(valor[i]) == 0 or int(valor[i]) == 1:
			pass
		else:
			return False

	return True

#Convierte un valor decimal a hexadecimal
def dec2hex(decimal):
	digitoshex=[]
	dividendo = int(decimal)
	numhex=""

	while dividendo >= 1:
		digitoshex.append(car_hex2dec[dividendo%16])
		dividendo=dividendo//16
	
	for i in range(len(digitoshex)-1, -1, -1):
		numhex= numhex + str(digitoshex[i])

	return numhex

#Convierte un valor hexadecimal a decimal
def hex2dec(valor):
	numdec=0
	digitoshex=[]
	exp=0

	for i in range(len(valor)):
		digitoshex.append(valor[i])


	for i in range(len(digitoshex)-1, -1, -1):
		numdec=numdec+(int(car_dec2hex[digitoshex[i]])*(16**exp))
		exp=exp+1
		
	return numdec

#Comprueba si un valor es hexadecimal
def eshexadecimal(valor):

	for i in valor:
		if i in car_dec2hex:
			pass
		else:
			return False

	return True

#Comprueba si un valor es decimal
def esdecimal(valor):

	try:
		decimal = int (valor)
		if decimal < 0:
			print ("Debe introducir un número positivo.")
			return False

	except:
		return False

	return True


tipovalor = {"DEC":0,"ROM":0,"HEX":0,"BIN":0}
valores = {"DEC":0,"ROM":0,"HEX":0,"BIN":0}
tipodato = {"DEC":"decimal","HEX":"hexadecimal","ROM":"romano","BIN":"binaro"}

print (Fore.YELLOW+Style.BRIGHT+Back.GREEN+"NumConverter v1.0 - (c) Antonio de la Rosa 2018"+Fore.RESET+Back.RESET+Style.DIM)
print ("Este software convierte un valor introducido a decimal, romano, binario y hexadecimal")
print ("Para salir, pulse "+Fore.GREEN+Style.BRIGHT+"Enter"+Fore.RESET+Style.DIM+" sin introducir ningún valor")

num_rom=0

while True:

	for i in tipovalor:
		tipovalor[i]=0
		valores[i]=0
	
	print (Fore.YELLOW)
	numero=input("Por favor introduzca un valor: ")
	print (Fore.RESET, end="")
	if numero == "":
			print ("El programa se cerrará")
			break

	#Determindar el tipo de dato introducido
	try:
		if esdecimal(numero):
			tipovalor["DEC"]=1
	except:
		pass

	try:
		if esbinario(numero):
			tipovalor["BIN"]=1
	except:
		pass

	try:
		if es_romano(numero):
			tipovalor["ROM"]=1
	except:
		pass

	try:
		if eshexadecimal(numero):
			tipovalor["HEX"]=1
	except:
		pass

	
	nvalores=0

	for i in tipovalor:
		nvalores = nvalores + tipovalor[i]
	
	if nvalores == 0:
		print ("El valor introducido es incorrecto.")

	elif nvalores > 1:

		print ("El valor introducido puede ser", end=" ")

		j = 0

		for i in tipovalor:

			if tipovalor[i]:
				if j < (nvalores-1):
					print (tipodato[i], end=", ")
				elif j < nvalores:
					print (tipodato[i], end=" o ")
				else:
					print (tipodato[i], end=".\n")

			j = j +1	

	#Si el dato intoducido se corresponde con más de un tipo de datos, solicitar especificación
		while True:

			print ("Especifique el tipo de valor introducido (", end="")

			j = 0

			for i in tipovalor:

				if tipovalor[i]:
					if j < (nvalores):
						print (i+":"+tipodato[i], end=", ")
					
					else:
						print (i+":"+tipodato[i], end="): ")

				j = j +1

			t_dato = input().upper()

			if t_dato in tipovalor:
				if tipovalor[t_dato]:
					for i in tipovalor:
						tipovalor[i]=0
					tipovalor[t_dato]=1
					break
	
	# No aseguramos de que el tipo de dato ha sido bien determinado
	nvalores=0

	for i in tipovalor:
		nvalores = nvalores + tipovalor[i]

	# Calculamos los valores en los diferentes tipos de datos
	if nvalores:
		if tipovalor["DEC"]==0:
			if tipovalor["ROM"]==1:
				valores["DEC"]=rom2dec(numero)
			elif tipovalor["HEX"]==1:
				valores["DEC"]=hex2dec(numero)
			elif tipovalor["BIN"]==1:
				valores["DEC"]=bin2dec(numero)
		else:
			valores["DEC"]=int(numero)

		valores["HEX"]=dec2hex(valores["DEC"])
		valores["BIN"]=dec2bin(valores["DEC"])
		if valores["DEC"]<4000:
			valores["ROM"]=dec2rom(valores["DEC"])
		else:
			valores["ROM"]=""
 		
	#Imprimimos los valores calculados
	
		print ("")
		for i in valores:
			print (i + ": ", end=" ")
			if tipovalor[i]:
				print(Fore.RED + str(valores[i]) + Fore.RESET)
			else:
				print(Fore.BLUE + str(valores[i]) + Fore.RESET)


