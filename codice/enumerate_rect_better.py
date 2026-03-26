import pprint
import time

# Funzione per enumerare i sottorettangoli di interesse più efficiente
def enumerate_rect_better(matrice):
    n = len(matrice)
    m = len(matrice[0])

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

                            sottomatrice = []
                            for i in range(r_start, r_end + 1):
                                riga = matrice[i][c_start:c_end + 1]
                                sottomatrice.append(riga)

                            dizionario[nome] = sottomatrice
                else:
                    j += 1

    return contatore, dizionario

# prova 

matrice = [
    [6, 7, 8],
    [4, 0, 5],
    [1, 2, 3]
]

matrice3 = [
    [8, 9, 10, 11, 12],
    [5, 0, 6, 0, 7],
    [1, 2, 3, 0, 4]
]

matrice2 = [
    [23, 24,  25, 26, 27,  28, 29],
    [18, 0, 19, 0, 20, 21, 22],
    [ 11, 12,  13, 14, 15,  16, 17],
    [ 7,  0, 8,  0, 9,  0,  10],
    [ 1,  2,  3,  4,  5,  0,  6]
]

startT = time.time()
n, diz = enumerate_rect_better(matrice3)
endT = time.time()
print(f"Totale rettangoli: {n}")
pprint.pprint(diz)
print(f"Tempo impiegato: {endT-startT} sec")
print()