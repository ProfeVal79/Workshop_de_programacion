def lista_pares_triplicados(lista):
    return [i * 3 for i in lista if i % 2 == 0]

mi_lista = [6, 5, 3, 4]
resultado = lista_triplicada(mi_lista)
print(resultado)