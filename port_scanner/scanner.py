import socket

def escanear_puerto(ip, puerto, timeout=1):
    """
    Intenta conectarse a un puerto específico de una IP.
    Devuelve True si el puerto está abierto, False si está cerrado.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    resultado = sock.connect_ex((ip, puerto))
    sock.close()
    return resultado == 0


def escanear_rango(ip, puerto_inicio, puerto_fin):
    """
    Escanea un rango de puertos en una IP y devuelve
    una lista con los puertos que están abiertos.
    """
    puertos_abiertos = []
    print(f"\nEscaneando {ip} desde el puerto {puerto_inicio} hasta {puerto_fin}...\n")

    for puerto in range(puerto_inicio, puerto_fin + 1):
        if escanear_puerto(ip, puerto):
            print(f"[ABIERTO] Puerto {puerto}")
            puertos_abiertos.append(puerto)

    return puertos_abiertos