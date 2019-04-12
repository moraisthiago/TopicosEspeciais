N = int(input())
f = 1

for i in range(1, N + 1):
	f = f * i
	
print ("O fatorial de {} é {}." .format (N, f))