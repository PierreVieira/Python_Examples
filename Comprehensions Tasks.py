# Task: Find title movies released before 2000
movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattaca", 1997),
          ("No Country for Old Men", 2007), ("Rear Windoway", 1954),
          ("The Lord of the Rings: The Fellowship of the Ring"
           , 2001), ("Groundhog Day", 1993), ("Close Encouters of the Third Kind", 1977),
          ("The Royal Tenembaums", 2001),
          ("The Aviator", 2004), ("Raiders of the Los Ark", 1981)]
# Code
antes2000 = [titulo for (titulo, ano) in movies if ano < 2000]
print(antes2000)
# Task2: Make a cartesian Product with the sets
A = {1, 3}
B = {'x', 'y'}
# Code
AxB = {(first, second) for first in A for second in B}
print(AxB)
