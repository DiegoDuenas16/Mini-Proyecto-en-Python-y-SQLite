import sqlite3
import msvcrt

# Función para ocultar la contraseña
def leer_password():
    password = ""
    while True:
        tecla = msvcrt.getwch()
        if tecla == "\r":
            print()
            break
        elif tecla == "\b":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += tecla
            print("*", end="", flush=True)
    return password

# Inicio de sesión
def iniciar_sesion():
    print("\n===========================================")
    print("       SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("===========================================")
    print("\n              INICIO DE SESIÓN")
    print("-------------------------------------------")

    usuario = input("Usuario: ")
    print("Contraseña: ", end="", flush=True)
    password = leer_password()

    # Conexión con la base de datos
    conexion = sqlite3.connect("empleados.db")
    cursor = conexion.cursor()

    # Verificar las credenciales
    cursor.execute("""
        SELECT * FROM usuarios
        WHERE usuario = ? AND password = ?
    """, (usuario, password))

    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        print("\nAcceso correcto.")
        print("Bienvenido al sistema.\n")
        return True
    else:
        print("\nUsuario o contraseña incorrectos.\n")
        return False