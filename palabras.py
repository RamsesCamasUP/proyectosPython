if __name__ == "__main__":
    """
    palabra = str("amad a la dama")
    palabra = palabra.replace(" ","")
    # En este caso imprime "Es Palindroma"
    if palabra == ''.join(reversed(palabra)):
        print("Es Palindroma")
    else:
        print("No es Palindroma")
    """

    minus = "Este TextO seRá en MinuSculAs"
    print(minus.lower())
    print(minus.capitalize())
    minus = minus.replace("MinuSculAs","mayusculas")
    print(minus.upper())
