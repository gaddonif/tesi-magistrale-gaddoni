def genera_matrice(m,n,zero_pos):
    matrice = [[0 for _ in range(n)] for _ in range(m)] #creo matrice di zeri
    set_zero=set(zero_pos)
    val = 1
    for i in range(m-1,-1,-1): #percorro le righe da alto a basso
        for j in range(n): #percorro colonne da sx a dx
            if (i,j) in set_zero:
              continue
            else: 
              matrice[i][j]=val
              val += 1
    return matrice

#prova
m=5
n=5
zero_pos=[(1,1),(1,3),(3,1),(3,3),(4,3)] #ricorda di leggere indici partendo da 0,0 e da nord-ovest
risultato=genera_matrice(m,n,zero_pos)
print(risultato)
