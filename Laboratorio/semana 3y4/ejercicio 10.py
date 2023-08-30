
def es_palindromo(frase):
    # Convertimos la frase a minúsculas y eliminamos espacios y signos de puntuación
    frase = frase.lower()
    frase = ''.join(c for c in frase if c.isalnum())
    
    # Comparamos la frase original con su reverso
    return frase == frase[::-1]

# Pedimos al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

if es_palindromo(frase):
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
