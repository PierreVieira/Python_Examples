earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)
print(earth_metals)
"""
--> Isso aqui gera AttributeError
conjunto = {1, 2, 3, 4, 5, 6}
conjunto.sort()
"""
#Outro exemplo:
"""
format := (name, radius, density, distance from Sun)
Radius: Radius at equator in kilometers
Density: Average density in g/cm³
Distance from Sun: Avg. distance to sun in AUs

1 Astronomical unit aprx: Average distance of Earth to Sun
"""
planets = [('Mercury', 2440, 5.43, 0.395), ('Venus', 6052, 5.24, 0.723), ('Earth', 6738, 5.52, 1),
           ('Mars', 3396, 3.93, 1.33, 1.53), ('Jupiter', 71492, 1.33, 5.21), ('Saturn', 60268, 0.69, 9.551),
           ('Uranus', 25559, 1.27, 19.213), ('Nepturne', 24764, 1.64, 30.07)]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True) #Ordena os planetas do maior para o menor
print(planets)
desinty = lambda planet: planet[2]
planets.sort(key=desinty) #Ordena os planetas pela densidade (da maior para a menor)
"""
O sorted não irá ordenar por referência, irá apenas retornar a coleção passada como parâmetro ordenada 
"""
from random import sample
numeros = tuple(sample(range(10), 5))
# numeros = (1, 4, 2, 5, 3)
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))