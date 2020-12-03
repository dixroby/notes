
#de una lista devolver la lista sin repetir
arr = [1,2,2,2,3,4,5,6,7,7,8,8]

print (arr)
def arreglos(arr):
  return list(set(arr))

print(arreglos(arr))
