valores = list(map(int, input("Digite seis valores inteiros!\n").split()))
valoresPositivos = int()

for i in valores:
	
	if i > 0:		
		valoresPositivos += 1
		
print ("Existem {} valores positivos.\n" .format( valoresPositivos))	