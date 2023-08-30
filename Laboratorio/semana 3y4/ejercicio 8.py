
def invertir_frase(frase):
    palabras = frase.split()  # Dividir la frase en una lista de palabras
    palabras_invertidas = palabras[::-1]  # Invertir el orden de las palabras
    frase_invertida = ' '.join(palabras_invertidas)  # Unir las palabras en una frase

    return frase_invertida

frase_original = "Aprendiendo Python con Edem"
frase_invertida = invertir_frase(frase_original)
print(frase_invertida)
