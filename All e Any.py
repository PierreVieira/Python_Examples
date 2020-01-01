"""
all() -> Retorna True se todos os eleemntos do iterável são verdadeiros ou ainda se o iterável está vazio
"""
all([0, 1, 2, 3, 4])  # False
all([1, 2, 3, 4])  # True
# Exemplo prático
nomes = ['Carlos', 'Camila', 'Cassiano']
print(all([nome[0] == 'C' for nome in nomes]))  # True
"""
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna false
"""
any([0, 1, 2, 3, 4])  # True
any([])  # False
