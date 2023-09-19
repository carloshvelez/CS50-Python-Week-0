def main():
    texto = input("Ingrese un texto: ")
    print(conversion(texto))


def conversion(texto):
    convertido = texto.replace(":)","🙂").replace(":(","🙁" )
    return convertido

main()
