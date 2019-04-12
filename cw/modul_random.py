'''
1. Rzuć kostką. Co? Nie masz kostki do gry pod ręką? W takim razie:

Zaimportuj moduł random

Zainicjiuj zmienne min =1 i max = 6

Do zmiennej dice zapisz wynik losowania liczby między min, a max. W ten sposób zasymulowaliśmy rzut kostką.

Napisz sekwencję poleceń if/elif/else, która w zależności od wylosowanej wartości wyświetli:



1:
   
 o 
   
 
2:
  o
   
o  
 
3:
  o
 o 
o  
 
4:
o o
   
o o
 
5:
o o
 o 
o o
 
6:
o o
o o
o o


2. Trochę zmieniamy temat. Rzuć pięcioma kostkami:



zadeklaruj zmienną dices jako pustą listę

pięć razy wylosuj liczbę z zakresu min do max i wynik dopisz do listy dices

posortuj listę dices

wyświetl zawartość zmienej dices
'''

import random
 
min = 1
max = 6
 
dice = random.randint(min,max)
 
if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')
 
print('----------------------')
 
dices = []
for i in range(5):
    dices.append(random.randint(min,max))
 
dices.sort()
print(dices)
