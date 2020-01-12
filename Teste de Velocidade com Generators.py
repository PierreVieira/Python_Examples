from time import time

# Generator Expression
gen_inicio = time()
print(sum(i for i in range(50_000_000)))  # 50 milhões
gen_tempo = time() - gen_inicio
print(f'Generator expression levou {gen_tempo} segundos.')
# List Comprehension
list_inicio = time()
print(sum([i for i in range(50_000_000)]))  # 50 milhões
list_tempo = time() - list_inicio
print(f'List Comprehension levou {list_tempo} segundos.')
