"""
def es_primo(num):
	resultado = True

	for divisor in range(2,num):
		print(divisor)
		if (num % divisor) == 0:
			resultado = False
			break


	return resultado

es_primo(13)
"""
s = 0

for n in range(1,10):
	if n % 2 != 0:
		continue;

	s += n

else:
	s += 5



print(s)