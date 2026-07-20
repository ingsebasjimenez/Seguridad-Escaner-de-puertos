from port_scanner.scanner import escanear_rango
from password_analyzer.analyzer import analizar_contraseña
from database.db import guardar_escaneo


def menu_escaner():
    print("\n=== Escáner de Puertos ===")
    ip = input("Ingresa la IP a escanear (ej. 127.0.0.1): ")
    puerto_inicio = int(input("Puerto inicial: "))
    puerto_fin = int(input("Puerto final: "))

    abiertos = escanear_rango(ip, puerto_inicio, puerto_fin)

    print("\n--- Resultado ---")
    if abiertos:
        print(f"Puertos abiertos encontrados: {abiertos}")
    else:
        print("No se encontraron puertos abiertos en ese rango.")

    # Guardar el resultado en la base de datos
    guardar_escaneo(ip, puerto_inicio, puerto_fin, abiertos)


def menu_analizador():
    print("\n=== Analizador de Contraseñas ===")
    contraseña = input("Ingresa la contraseña a analizar: ")

    resultado = analizar_contraseña(contraseña)

    print(f"\nNivel de seguridad: {resultado['nivel']} ({resultado['puntaje']}/6 puntos)")
    print("Detalles:")
    for razon in resultado["razones"]:
        print(f"  - {razon}")


def main():
    print("=== Security Toolkit ===")
    print("1. Escáner de puertos")
    print("2. Analizador de contraseñas")

    opcion = input("\nElige una opción (1 o 2): ")

    if opcion == "1":
        menu_escaner()
    elif opcion == "2":
        menu_analizador()
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()