import pprint
import time
from functions import coordinate, genera_matrice, enum_rect

m=5
n=5
w = [1,1,2,1,1]
h = [1,1,1,1,1]

zero_pos=[(1,1),(1,3),(3,1),(3,3),(4,3)] #ricorda di leggere indici partendo da 0,0 e da nord-ovest
M = genera_matrice(m,n,zero_pos)
print(M)

startT = time.time()
n, diz = enum_rect(M,w,h)
endT = time.time()
print(f"Totale rettangoli: {n}")
pprint.pprint(diz)
print(f"Tempo impiegato: {endT-startT} sec")
print()

