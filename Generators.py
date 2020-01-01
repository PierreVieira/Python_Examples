"""
Generators seriam as tuple comprehension.
"""
print(all(nome[0] == 'C' for nome in ['Carlos', 'Camila', 'Cassiano']))
gen = (i for i in range(10))
for c in gen:
    print(c)
#Na segunda utilização já não tem mais nada disponível em gen
for c in gen:
    print(c)