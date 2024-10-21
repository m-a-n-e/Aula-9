textoPalavra = "reviver"
tamanhoPalavra = len(textoPalavra)

ehPalindromo = True

while tamanhoPalavra > 1:
    if textoPalavra[0] != textoPalavra[tamanhoPalavra - 1]:
        ehPalindromo = False
        break
    textoPalavra = textoPalavra[1:tamanhoPalavra - 1]
    tamanhoPalavra -= 2

print("A palavra é palíndroma!" if ehPalindromo else "A palavra não é palíndroma.")
