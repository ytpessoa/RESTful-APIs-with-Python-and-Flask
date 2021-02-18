

def listas():
	L = []
	L1 = [1,2,3]
	print(L1)
	L1[0]=2
	print(L1)
	


def fString():
	nome = "Pedro"
	idade = 54
	print(f"O nome dele eh {nome}. Ele tem {idade} anos")

def printPar(fim):
	print("func2")
	i=0
	while i <= fim :
		print(i)
		i+=2


def main():
	print("func1:main")
	x = int(input("Entre com um numero"))
	printPar(x)
	
		

if __name__ == '__main__':
	listas()
	#fString()
	#main()