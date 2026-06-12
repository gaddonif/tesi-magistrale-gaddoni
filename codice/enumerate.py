# algoritmo di enumerazione OK consegnato ai proff

import numpy as np

def enumerate(A):
    n, m = A.shape
    risultati = []
    

    for i in range(n):  # riga iniziale
        for j in range(m):  # colonna iniziale
            valide = np.ones(m, dtype=bool) # inizializzo vettore valide: a priori tutte le colonne valide
            
            # (i,j) cella iniziale
            for i2 in range(i, n): # espando verso il basso fino a riga i2
                valide &= (A[i2] != 0) # se ci sono zeri nella i2-esima riga, mette False nelle rispettive colonne di valide
                
                for j2 in range(j, m): # espando verso destra fino a colonna j2
                    if valide[j2]:
                        risultati.append((i, j, i2, j2)) # 'vertici sx alto - dx basso' del rettangolo                       
                    else:
                        break 
    return risultati, len(risultati)


# Esempio: istanza proposta dai proff

A = np.ones((4,6)) # definisco la matrice di uni
zero_pos = np.array([[1,1],
                    [1,5],
                    [3,3]])
A[zero_pos[:,0], zero_pos[:,1]] = 0 # metto zeri in posizione porte/finestre

rect, num = enumerate(A)

# visualizzazione verticale
for r in rect:
   print(r)

print("Totale rettangoli:", num)

# creo txt con output
with open("output.txt", "w") as f:
    for r in rect:
        f.write(str(r) + "\n")