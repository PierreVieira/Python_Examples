temps_celcius = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
         ("London", 22), ("Beijing", 32)]
temps_fahrenheit = list(map(lambda tupla_cidade: (tupla_cidade[0], (9/5)*tupla_cidade[1] + 32), temps_celcius))
#Aplica a operação da função lambda para cada elemento (tupla) da lista temp_celcius
print(temps_fahrenheit)
