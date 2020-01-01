# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria', 'Carol', 'Karine']
# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha mais de 5 caracteres
instrutoras_selecionadas = list(
    filter(lambda nome: len(nome) > 5, nomes))  # Seleciona apenas os nomes cujo número de caracters seja > 5
instrutoras_mapeadas = list(
    map(lambda nome: 'Sua instrutora é ' + nome, instrutoras_selecionadas))  # Concatena para cada nome selecionado
print(instrutoras_mapeadas)
