def cifra_cesar(texto, deslocamento=3):
    texto_cifrado = ""

    for caractere in texto:
        # Verifica se é letra
        if caractere.isalpha():

            # Define base ASCII
            if caractere.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Aplica a cifra de César
            novo_caractere = chr(
                (ord(caractere) - base + deslocamento) % 26 + base
            )

            texto_cifrado += novo_caractere

        else:
            # Mantém espaços e símbolos
            texto_cifrado += caractere

    return texto_cifrado


# Entrada do usuário
mensagem = input("Digite uma mensagem: ")

# Criptografa
resultado = cifra_cesar(mensagem)

# Saída
print("Texto cifrado:", resultado)
