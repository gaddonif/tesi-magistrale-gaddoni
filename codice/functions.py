# funzioni per l'algoritmo di enumerazione dei rettangoli di una facciata

def genera_matrice(m,n,zero_pos):
    # crea la matrice dei rettangoli singoli numerandoli (0 per rettangoli su porte e finestre)
    
    matrice = [[0 for _ in range(n)] for _ in range(m)] #creo matrice di zeri
    set_zero=set(zero_pos)
    val = 1
    for i in range(m-1,-1,-1): #voglio numerare le righe dal basso
        for j in range(n): #percorro colonne da sx a dx
            if (i,j) in set_zero:
              continue
            else: 
              matrice[i][j]=val
              val += 1
    return matrice

###

def coordinate(vect):
# prende in input un vettore di lunghezza m e restituisce le somme cumulative 
# partendo da 0
# nel nostro caso utilizzato per determinare il vettore delle coordinate
# su asse x e y della facciata

  res = [0]
  for i in vect:
    res.append(res[-1]+i)
  return res

###
 
def enum_rect(matrice, w, h):
    # Funzione per enumerare i sottorettangoli

    n = len(matrice)
    m = len(matrice[0])

    # definisco le coordinate della griglia
    X = coordinate(w)
    Y = coordinate(h)

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
                                                "celle": sottomatrice}
                else:
                    j += 1

    return contatore, dizionario