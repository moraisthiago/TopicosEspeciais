valores = list(map(int, input("Digite 15 valores inteiros!\n").split()))
maior = valores[0]; posicao = int()

for i in range(1, 15):
	if valores[i] > maior:
		maior = valores[i]
		posicao = i
		
print ("O maior valor é {} na posição {}." .format(maior, posicao + 1))