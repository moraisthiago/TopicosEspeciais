pedido = int(input("Por favor, nos informe quantas pizzas serão pedidas.\n"))
valor = float(input("Agora nos informe o valor da pizza que está no cardápio.\nR$ "))
custo = pedido * valor; imposto = custo * 0.08

print ("Valor total do pedido: R$ {:.2f}." .format (custo + imposto))