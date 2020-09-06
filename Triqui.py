import os

def clear():
	if os.name == "posix":
		os.system ("clear")
	else:
	  	os.system ("cls")

def imprimirMatriz():
	print()
	for i in range(3):
		for j in range(3):
			print(base[i][j], end="\t")
		print()
	print()

def modificarMatriz(x):
	for i in range(3):
		for j in range(3):
			if(base[i][j]==x):
				base[i][j]="X"
				break
def turnoSystem():
	for i in range(3):
		for j in range(3):
			if(type(base[i][j])== int):
				base[i][j]="O"
				return "Salgo de la Funcion"

def verificarTriqui(x):
	if(base[2][0]==x and base[2][1]==x and base[2][2]==x):
		return True
	elif(base[1][0]==x and base[1][1]==x and base[1][2]==x):
		return True
	elif(base[0][0]==x and base[0][1]==x and base[0][2]==x):
		return True
	elif(base[0][0]==x and base[1][1]==x and base[2][2]==x):
		return True
	elif(base[2][0]==x and base[1][1]==x and base[0][2]==x):
		return True
	elif(base[0][0]==x and base[1][0]==x and base[2][0]==x):
		return True
	elif(base[0][1]==x and base[1][1]==x and base[2][1]==x):
		return True
	elif(base[0][2]==x and base[1][2]==x and base[2][2]==x):
		return True

def turnoUser():
	x = int(input("Ingrese Numero: "))
	clear()
	modificarMatriz(x)
	imprimirMatriz()
	if(verificarTriqui("X")==True):
		return 1
	h=turnoSystem()
	clear()
	imprimirMatriz()
	if(verificarTriqui("O")==True):
		return 2

def verificarMatriz():
	for i in range(3):
		for j in range(3):
			if(type(base[i][j])== int):
				return True

base=[[1,2,3],[4,5,6],[7,8,9]]

imprimirMatriz()

while(verificarMatriz()):
	x = turnoUser()
	if(x == 2):
		print("Gano System")
		print()
		break
	if(x == 1):
		print("Gano Usuario")
		print()
		break
