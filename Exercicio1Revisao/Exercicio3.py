N = int(input())

for i in range(1, N + 1):
	
	valores = list(map(float, input().split()))
	
	print ("Média {}: {}\n" .format (i, ((valores[0] * 2) + (valores[1] * 3) + (valores[2] * 5) / 10)))