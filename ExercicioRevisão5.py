valores = list(map(int, input("Digite seis valores inteiros!\n").split()))
valoresPositivos = int()
media = int()

for i in valores:
	
	if i > 0:		
		valoresPositivos += 1
		media += i
		
print ("Existem {} valores positivos.\nMédia: {:.1f}" .format( valoresPositivos, media / valoresPositivos))	