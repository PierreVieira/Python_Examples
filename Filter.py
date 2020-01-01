#Using filter function to find all data above the average
from statistics import mean
#Exemplo 1: Pegando os valores acima da média
print('EXEMPLO 1')
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = mean(data)
lista_acima_media = list(filter(lambda x: x > avg, data))
lista_abaixo_media = list(filter(lambda x: x < avg, data))
print(f'Valores: {data}')
print(f'Média = {avg:.2f}')
print(f'Valores acima da média: {lista_acima_media}')
print(f'Valores abaixo da média: {lista_abaixo_media}')
print('EXEMPLO 2')
#Exemplo 2: Removendo dados ausentes
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(list(filter(None, countries)))
