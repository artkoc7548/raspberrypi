for i in range(32,127):
    print(i, chr(i)) 

import random

ints = range(33,127)
haslo = ''
for i in range(10): 
    haslo += chr(random.choice(ints))
print(haslo)
