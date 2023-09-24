from os import system
import Profesores
import Encargados
import Inscripciones

system("clear")


def salir():
    print("")
    print("Gracias por utilizar nuestro sistema")


def main():
    print("*********************************************")
    print("Bienvenido")
    print("Ingrese al sistema")
    print("")

    # Ingresar a la plataforma de usuarios.
    user = input("Ingrese su nombre y apellido: ").lower()

    # abrir los archivos de textos
    encarg_file = open("Encargados.txt", "r")
    profe_file = open("Profesores.txt", "r")
    create_file = open("Inscripciones.txt", "w")
    create_file.close()

    # guardar la info de los archivos
    encargados = encarg_file.read().split("\n")
    profesores = profe_file.read().rstrip().split("\n")

    # cerrar los archivos de texto
    encarg_file.close()
    profe_file.close()

    encar_auth_list = {}
    prof_auth_list = {}


if __name__ == "__main__":
    main()
