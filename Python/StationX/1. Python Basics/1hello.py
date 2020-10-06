double = "She said, \"That's a great tasting apple!\""
single = 'She said, "That\'s a great tasting apple!"'
print(double, single)

print(double[0])
print(len(double))
print(single.lower())
print(single.upper())
print('I ' + 'love '+ 'Python')
print('!' * 10)
version = 3.7

print('I love Python ' + str(version))

# Formatting Strings

print('I {}Python {}'.format('love ', version))

print('I {0} {1}. {1} {0}s me'.format('love', 'Python'))

print('{0:8} | {1:8}'.format('Fruit', 'Quantity')) # :8 indica 8 caracteres como mínimo
print('{0:8} | {1:8}'.format('Orange', 3))

# < Left > Right ^ Center (Default Left)
print('{0:8} | {1:>8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:>8}'.format('Orange', 3))
print('{0:8} | {1:>8.2f}'.format('Orange', 3.45546464)) # 2 decimal places (float) 
#input() entrada del usuario
#everything in python is an object
#objects can have methods
#methods are functions that operate on an object
