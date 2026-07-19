from port_scanner.scanner import escanear_rango

def main():
    print("=== Security Toolkit - Escáner de Puertos ===")
    ip = input("Ingresa la IP a escanear (ej. 127.0.0.1 para tu propia máquina): ")
    puerto_inicio = int(input("Puerto inicial: "))
    puerto_fin = int(input("Puerto final: "))

    abiertos = escanear_rango(ip, puerto_inicio, puerto_fin)

    print("\n--- Resultado ---")
    if abiertos:
        print(f"Puertos abiertos encontrados: {abiertos}")
    else:
        print("No se encontraron puertos abiertos en ese rango.")


if __name__ == "__main__":
    main()