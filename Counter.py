from collections import Counter
texto = 'Hope Sandoval juntou-se à banda Opal nos finais de 1980s com David Roback e sua amiga Kendra Smith, que viria a ' \
        'deixar a banda. Roback e Sandoval começam a compor juntos (sendo Sandoval autora da maioria das letras) e alteram ' \
        'o nome da banda para Mazzy Star. No inicio de 1992, a banda lançou o album So Tonight That I Might See'
lista_texto = texto.split()
print(lista_texto)
res = Counter(lista_texto)
print(res)
print(res.most_common(3))
mais_comum = res.most_common(1)
print(mais_comum)
print(f"A palavra que mais apareceu foi: '{mais_comum[0][0]}' aparecendo {mais_comum[0][1]} vezes")