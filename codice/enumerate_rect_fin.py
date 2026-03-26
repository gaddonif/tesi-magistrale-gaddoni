import pprint
import time
from coordinate import coordinate

# Funzione per enumerare i sottorettangoli di interesse più efficiente
def enumerate_rect_fin(matrice, w, h):
    n = len(matrice)
    m = len(matrice[0])

    # definisco le coordinate della griglia
    X = coordinate(w)
    Y = coordinate(h)
    #htot = Y[-1] # l'ultimo elemento corrisponde ad altezza facciata

    contatore = 0
    dizionario = {}

    for r_start in range(n):

        valido_colonne = [1] * m  # tutte valide all'inizio

        for r_end in range(r_start, n):

            # aggiorna colonne valide
            for j in range(m):
                if matrice[r_end][j] == 0:
                    valido_colonne[j] = 0

            # ora trova segmenti continui di colonne valide
            j = 0
            while j < m:
                if valido_colonne[j] == 1:
                    start = j

                    while j < m and valido_colonne[j] == 1:
                        j += 1

                    end = j - 1

                    # genera tutti i sottorettangoli orizzontali
                    for c_start in range(start, end + 1):
                        for c_end in range(c_start, end + 1):

                            contatore += 1
                            nome = f"R{contatore}"
                            
                            x = X[c_start]
                            width = X[c_end + 1] - X[c_start]

                            y = Y[n-1-r_end] 
                            height = Y[n-r_start] - Y[n-1-r_end] 

                            sottomatrice = []
                            for i in range(r_start, r_end + 1):
                                riga = matrice[i][c_start:c_end + 1]
                                sottomatrice.append(riga)

                            dizionario[nome] = {"coords": (x,y,width,height), 
                                                "griglia": sottomatrice}
                else:
                    j += 1

    return contatore, dizionario

#prova
matrice = [
    [6, 7, 8],
    [4, 0, 5],
    [1, 2, 3]
]

w=[2,1,2]
h=[3,1,1]

startT = time.time()
n, diz = enumerate_rect_fin(matrice,w,h)
endT = time.time()
print(f"Totale rettangoli: {n}")
pprint.pprint(diz)
print(f"Tempo impiegato: {endT-startT} sec")
print()