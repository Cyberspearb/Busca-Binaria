def pesquisa_binaria_recursiva(A, esquerda, direita, item):
  
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
   
    if A[meio] == item:
        return meio
 
    elif A[meio] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)

A = [0,17,25,32,58,70,100,250]
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 25))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 0))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 70))
print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 250))