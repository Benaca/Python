#! /usr/bin/python
# -*- coding: UTF-8 -*-

#Recibe un valor en número romanos y devuelve un entero o viceversa

from colorama import init, Fore, Back, Style

init()

claves = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}

#Función romanizar devuelve un número romano a partir de un valor decimal
def romanizar (valor):

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

#Función arabizar devuelve el valor decimal del número romano introducido
def arabizar (valor):   
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

print (Fore.YELLOW+Style.BRIGHT+Back.GREEN+"Números Romanos v1.0 - (c) Antonio de la Rosa 2018"+Fore.RESET+Back.RESET+Style.DIM)
print ("Este software convierte los números decimales en romanos y viceversa")
print ("Para salir, pulse "+Fore.GREEN+Style.BRIGHT+"Enter"+Fore.RESET+Style.DIM+" sin introducir ningún valor")

num_rom=0

while True:
	print (Fore.YELLOW)
	numero=input("Por favor introduzca un número romano o decimal: ")
	print (Fore.RESET, end="")
	if numero == "":
			break

	try:
		if 0 < int(numero) < 4000:
			print (Fore.BLUE + numero + Fore.RESET + " en números romanos es " + Fore.RED + romanizar(int(numero))+ Fore.RESET)
			
		elif 0 >= int(numero) or int(numero) >= 4000:
			print ("Los valores decimales deber estar comprendidos entre 1 y 3999")
	
	except:
		if es_romano(numero):
			print (Fore.RED + numero + Fore.RESET + " en números decimales es " + Fore.BLUE + str(arabizar(numero))+ Fore.RESET)
		elif es_romano(numero.upper()):
			print ("Los números romanos deben introducirse en mayúsculas")
		else:
			print ("El valor introducido no es correcto")


