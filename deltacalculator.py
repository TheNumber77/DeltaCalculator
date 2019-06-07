linha = '-' * 42
titulo = 'DELTA CALCULATOR'
print(linha)
print(titulo.center(42))
print(linha)
a = int(input('digite o valor de "a": '))
b = int(input('digite o valor de "b": '))
c = int(input('digite o valor de "c": '))
d = b ** 2 - 4 * a * c
print('o valor de delta é: {}'.format(d))
