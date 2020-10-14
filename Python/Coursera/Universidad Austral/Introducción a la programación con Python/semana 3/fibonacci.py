# fib(n) = fib(n-1) + fib(n-2)

def fib(num):
	"""Resuelve la sucesión de Fibonacci"""
	anterior,actual=0,1

	for x in range(0,num//2):
		aux = anterior + actual
		print(anterior, actual)
		anterior = aux
		actual += anterior

	return anterior,actual

print(fib(35), sep='-', end='')