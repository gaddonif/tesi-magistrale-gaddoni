import pprint
import time

# Funzione per enumerare i sottorettangoli di interesse
def enumerate_rect(matrice):
    n = len(matrice)        # numero di righe
    m = len(matrice[0])     # numero di colonne
    
    dizionario = {}
    counter = 0
    # scegli riga iniziale
    for r_start in range(n):
        # scegli riga finale
        for r_end in range(r_start, n):
            # scegli colonna iniziale
            for c_start in range(m):
                # scegli colonna finale
                for c_end in range(c_start, m):

                    valido = True

                    # controlla direttamente senza creare la sottomatrice
                    for i in range(r_start, r_end + 1):
                        for j in range(c_start, c_end + 1):
                            if matrice[i][j] == 0:
                                valido = False
                                break
                        if not valido:
                            break

                    if not valido:
                        continue

                    # estrai la sottomatrice
                    sottomatrice = []
                    for i in range(r_start, r_end + 1):
                        riga = matrice[i][c_start:c_end + 1]
                        sottomatrice.append(riga)
                  
                    counter += 1
                    nome = f"R{counter}"
                    dizionario[nome] = sottomatrice
    
    return counter, dizionario
    

# Esempio di utilizzo
matrice = [
    [4, 0, 5],
    [2, 0, 3],
    [0, 1, 0]
]

matrice2 = [
    [23, 24,  25, 26, 27,  28, 29],
    [18, 0, 19, 0, 20, 21, 22],
    [ 11, 12,  13, 14, 15,  16, 17],
    [ 7,  0, 8,  0, 9,  0,  10],
    [ 1,  2,  3,  4,  5,  0,  6]
]

startT = time.time()
n, diz = enumerate_rect(matrice2)
endT = time.time()
print(f"Totale rettangoli: {n}")
pprint.pprint(diz)
print(f"Tempo impiegato: {endT-startT} sec")
print()