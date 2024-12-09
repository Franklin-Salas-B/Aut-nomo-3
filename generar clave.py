import secrets
import string

def generar_contraseña(longitud: int = 12) -> str:
    """
    Genera una contraseña segura de la longitud especificada.

    Args:
        longitud (int): longitud de la contraseña.

    Returns:
        str: La contraseña generada.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud < 8:
                print("La longitud mínima es 8 caracteres.")
            else:
                break
        except ValueError:
            print("Ingrese un valor numérico.")

    contraseña = generar_contraseña(longitud)
    print("Contraseña generada:", contraseña)

if __name__ == "__main__":
    main()
