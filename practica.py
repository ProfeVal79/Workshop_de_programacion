nums = [1, 2, 3, 4]
nueva_lista = []

for i in nums:
    if i % 2 == 0:
        i = i * 2
        nueva_lista.append(i)
    else:
     nueva_lista.append(i)
    
print(nueva_lista)      