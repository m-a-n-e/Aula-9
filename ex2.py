numerosLista = [1, 2, 3, 4, 5]
somaTotal = 0

tamanhoLista = len(numerosLista)

while tamanhoLista > 0:
    somaTotal += numerosLista[tamanhoLista - 1]
    tamanhoLista -= 1

print(f"O total da soma dos elementos é {somaTotal}.")
