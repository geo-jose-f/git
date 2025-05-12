def eliminar_acentos(texto):
    
    # Esta función va a reemplazar caracteres acentuados por sus equivalentes sin acento.
    
    acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'a', 'É': 'e', 'Í': 'i', 'Ó': 'o', 'Ú': 'u',
        'ü': 'u', 'Ü': 'u'
    }
    for acentuada, normal in acentos.items():
        texto = texto.replace(acentuada, normal)
    return texto

def esPalindromo(cadena):
    
    # Esta función (es Palindromo) va a determinar si una cadena dada por el usuario es un palíndromo.
    # Un palíndromo es una cadena que se lee igual de izquierda a derecha que de derecha a izquierda.
    # Eliminar acentos y convertir a minúsculas
    cadena_sin_acentos = eliminar_acentos(cadena.lower())
    # Eliminar espacios y caracteres no alfanuméricos
    cadena_limpia = ''.join(c for c in cadena_sin_acentos if c.isalnum())
    # Comprobar si la cadena es igual al revés
    return cadena_limpia == cadena_limpia[::-1]

def main():
    """
    Función principal que solicita al usuario una frase y comprueba si es un palíndromo.
    """
    # Solicitar la frase al usuario
    frase = input("Introduce una frase: ")
    # Verificar si la frase es palíndroma
    if esPalindromo(frase):
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")

# Esta línea es una convención estándar en Python que se utiliza para controlar el comportamiento del script.
if __name__ == "__main__":
    main()
