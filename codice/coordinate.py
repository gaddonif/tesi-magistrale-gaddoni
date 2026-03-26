def coordinate(vect):
# prende in input un vettore e restituisce le somme cumulative
# nel nostro caso utilizzato per determinare il vettore delle coordinate
# su asse x e y della facciata

  res = [0]
  for i in vect:
    res.append(res[-1]+i)
  return res

W=[2,1,3]
res=coordinate(W)
print(res)