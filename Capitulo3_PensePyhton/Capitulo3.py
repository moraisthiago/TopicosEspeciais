print ("3.1 - Chamada de Função\n")

print (type(42), "\n")

print (int('32'), "\n")

#print (int('Hello'), "\n")

print (int(3.99999), "\n")

print (int(-2.3), "\n")

print (float(32), "\n")

print (float('3.14159'), "\n")

print (str(32), "\n")

print (str(3.14159), "\n")

print ("3.2 - Funções Maremáticas\n")

import math

print (math, "\n")

signal_power = 10.0
noise_power = 15.5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
heigth = math.sin(radians)
degress = 45

print (heigth, "\n")

degrees = 45
radians = degrees / 180.0 * math.pi

print (math.sin(radians), "\n")

print (math.sqrt(2) / 2.0, "\n")

print ("3.3 - Composição\n")

x = math.sin(degrees / 360.0 * 2 * math.pi)

print (x, "\n")

x = math.exp(math.log(x+1))

print (x, "\n")

hours = 3
minutes = hours * 60

print (minutes, "\n")

#hours * 60 = minutes

print (minutes, "\n")

print ("Como Acrescentar Novas Funções\n")

def print_lyrics():
	print ("I'm a lumberjack, and I'm okay.")
	print ("I sleep all night and I work all day.")

print (print_lyrics, "\n")

print (type(print_lyrics), "\n")

print (print_lyrics(), "\n")

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

print (repeat_lyrics(), "\n")

print ("3.7 - Parâmetros e Argumentos\n")

def print_twice(bruce):	
	print (bruce)
	print (bruce)

print (print_twice('Spam'), "\n")

print (print_twice(42), "\n")

print (print_twice(math.pi), "\n")

print (print_twice('Spam' * 4), "\n")

print (print_twice(math.cos(math.pi)), "\n")

michael = "Eric, the half a bee."

print (print_twice(michael), "\n")

print ("3.8 - As Variáveis e os Parâmetros São Locais\n")

def cat_twice(part1, part2):
	cat = part1 + part2
	print_twice(cat)

line1 = "Bing tiddle "
line2 = "tiddle bang."

print (cat_twice(line1, line2), "\n")

#print (cat, "\n")

print ("3.10 - Funções com Resultado e Funções Nulas\n")

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

print (x, "\n")
print (golden, "\n")
print (math.sqrt(5), "\n")

result = print_twice("Bing")

print ("\n")

print (result, "\n")

print (type(None), "\n")
