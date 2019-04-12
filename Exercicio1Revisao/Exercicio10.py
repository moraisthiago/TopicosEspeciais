diario = int(input("Quantos cigarros em média você fuma por dia?\n")) * 10
anual = int(input("Há quantos anos você tem esse hábito?\n")) * 365
diasPerdidos = (diario * anual) / (60 * 24)
horasPerdidas = ((diario * anual) % (60 * 24)) / 60
minutosPerdidos = ((diario * anual) % (60 * 24)) % 60


print ("Você perdeu {} dia(s), {}  hora(s) e {} minuto(s) da sua vida!" .format(int(diasPerdidos), int(horasPerdidas), int(minutosPerdidos)))