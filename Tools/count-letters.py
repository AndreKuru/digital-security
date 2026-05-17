from collections import Counter
import unicodedata


def remove_acentos(texto: str) -> str:
    # transforma caracteres acentuados em base + marca e remove as marcas
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def count_letters(text: str):
    # remove acentos e converte para minúsculas
    text = remove_acentos(text).lower()

    # mantém apenas letras
    letters = [c for c in text if c.isalpha()]

    counts = Counter(letters)

    # ordenar do mais frequente para o menos frequente
    for letter, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter}: {count}")


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    count_letters(user_input)
