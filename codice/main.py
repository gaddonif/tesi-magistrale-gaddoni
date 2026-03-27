import pprint
import time
from functions import coordinate, genera_matrice, enum_rect

# algoritmo di enumerazione rettangoli
# esempio 1
m=3
n=5
w = [1,1,2,1,1]
h = [1.5,1,1.5]

zero_pos=[(1,1),(1,3),(2,3)] #ricorda di leggere indici partendo da 0,0 e da nord-ovest
M = genera_matrice(m,n,zero_pos)
print(M)

startT = time.time()
n, diz = enum_rect(M,w,h)
endT = time.time()
print(f"Totale rettangoli: {n}")
pprint.pprint(diz)
print(f"Tempo impiegato: {endT-startT} sec")
print()

# esempio 2

m2=5
n2=7
w2 = [1,1,1,1,3,1,1]
h2 = [1,1,2,1,1]

zero_pos2=[(1,1),(1,3),(3,1),(3,3),(3,5),(4,5)] #ricorda di leggere indici partendo da 0,0 e da nord-ovest
M2 = genera_matrice(m2,n2,zero_pos2)
print(M2)

startT2 = time.time()
n2, diz2 = enum_rect(M2,w2,h2)
endT2 = time.time()
print(f"Totale rettangoli: {n2}")
pprint.pprint(diz2)
print(f"Tempo impiegato: {endT2-startT2} sec")
print()
