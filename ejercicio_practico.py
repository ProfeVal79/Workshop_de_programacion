def lista_triplicada(lista):
    nueva_lista = []
    for i in lista:
        i = i * 3
        nueva_lista.append(i)
    return nueva_lista

mi_lista = [1, 2, 3, 4]
resultado = lista_triplicada(mi_lista)
print(resultado) 
