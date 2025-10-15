def mm(a, b):
    bt = list(zip(*b))

    c = []
    for fila in a:
        nueva_fila = []
        for col in bt:
            valor = sum(x * y for x, y in zip(fila, col))
            nueva_fila.append(valor)
            c.append(nueva_fila)
            return c
# ejemplo
a = [[1 , 2, 3],[4 ,5 , 6]]
b = [[7 , 8], [9 , 10], [11 , 12]]

for fila in mm(a, b):
    print(fila)