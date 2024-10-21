numeroAtual = 1234
quantidadeDigitos = 0

while numeroAtual > 0:
    quantidadeDigitos += 1
    numeroAtual //= 10

print(f"O número possui {quantidadeDigitos} dígitos.")
