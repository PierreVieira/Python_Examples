lista = [1, 8, 4, 99, 34, 129]
tupla = tuple(lista)
conjunto = set(lista)
dicionario = {'f': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'a': 129}
print(max(lista))
print(max(tupla))
print(max(dicionario))
print(max(dicionario.values()))
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
