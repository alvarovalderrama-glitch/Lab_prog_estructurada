def solve_n_queens(n):
    solutions = []
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(r, path):
        if r == n:
            solutions.append(path.copy())
            return
        for c in range(n):
            if c in cols or (r + c) in diag1 or (r - c) in diag2:
                continue
            cols.add(c); diag1.add(r + c); diag2.add(r - c)
            path.append(c)
            backtrack(r + 1, path)
            path.pop()
            cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)

    backtrack(0, [])
    return solutions


def board_to_text(solution):
    n = len(solution)
    text = ""
    for r in range(n):
        line = ""
        for c in range(n):
            if solution[r] == c:
                line += "X "
            else:
                line += ". "
        text += line + "\n"
    return text

n = int(input("Ingrese N: "))

solutions = solve_n_queens(n)

archivo = open("soluciones.txt", "w")
archivo.write("Total de soluciones para N=" + str(n) + "\n\n")

contador = 1
for sol in solutions:
    archivo.write("Solucion " + str(contador) + "\n")
    archivo.write(board_to_text(sol))
    archivo.write("\n")
    contador += 1

archivo.close()

print("Archivo generado: soluciones.txt")
