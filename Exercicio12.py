def valorPagamento(prestacao, atraso):
	valor = int()
	if atraso == 0:
		valor = prestacao
	elif atraso > 0:
		valor = prestacao + (prestacao * 0.03) + ((prestacao * 0.001) * atraso)
	return (valor)
	
prestacao = float(input("Por favor, nos informe o valor da sua prestação.\nR$ "))

while prestacao > 0:
	atraso = int(input("Nos informe o período de atraso em dias.\n"))
	print ("Valor final a ser pago: R$ {:.2f}\n" .format (valorPagamento(prestacao, atraso)))
	prestacao = float(input("Por favor, nos informe o valor da sua prestação.\nR$ "))	