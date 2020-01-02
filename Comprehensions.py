"""
List Comprehensions examples
"""
# Gerando uma lista simples de dados números que vão de 0 a 9
lista_dados = [i for i in range(10)]
print(lista_dados)
"""[expr for val in collection]"""
comprehension1 = [x ** 2 for x in lista_dados]  # Eleva todos os números da lista ao quadrado
print(f'Comprehension 1: {comprehension1}')
"""[expr for val in collection if <test>]"""
comprehension2 = [x ** 2 for x in lista_dados if x % 2 == 0]  # Eleva apenas ao quadrado apenas os números pares.
#  Nesse caso apenas os pares estarão inclusos na lista
print(f'Comprehension 2: {comprehension2}')
"""[expr for val in collection if <test1> and <test2>]"""
comprehension3 = [x/3 for x in lista_dados if x % 2 == 1 and x % 3 == 0]
#  Aqui todos os números que sejam ímpares sendo múltiplos de 3 serão divididos por 3 e adicionados à lista.
print(f'Comprehension 3: {comprehension3}')

