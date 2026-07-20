# Lista básica de contraseñas más comunes y débiles conocidas
CONTRASEÑAS_COMUNES = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "abc123", "password1", "admin", "letmein"
]


def analizar_contraseña(contraseña):
    """
    Analiza una contraseña y devuelve un diccionario con:
    - puntaje (0 a 5)
    - nivel ("Débil", "Media", "Fuerte")
    - razones (lista de observaciones)
    """
    puntaje = 0
    razones = []

    # Criterio 1: longitud
    if len(contraseña) >= 12:
        puntaje += 2
        razones.append("Longitud excelente (12+ caracteres)")
    elif len(contraseña) >= 8:
        puntaje += 1
        razones.append("Longitud aceptable (8-11 caracteres)")
    else:
        razones.append("Muy corta (menos de 8 caracteres)")

    # Criterio 2: contiene mayúsculas y minúsculas
    if any(c.islower() for c in contraseña) and any(c.isupper() for c in contraseña):
        puntaje += 1
        razones.append("Combina mayúsculas y minúsculas")
    else:
        razones.append("Falta combinar mayúsculas y minúsculas")

    # Criterio 3: contiene números
    if any(c.isdigit() for c in contraseña):
        puntaje += 1
        razones.append("Contiene números")
    else:
        razones.append("No contiene números")

    # Criterio 4: contiene símbolos especiales
    simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    if any(c in simbolos for c in contraseña):
        puntaje += 1
        razones.append("Contiene símbolos especiales")
    else:
        razones.append("No contiene símbolos especiales")

    # Criterio 5: no está en la lista de contraseñas comunes
    if contraseña.lower() in CONTRASEÑAS_COMUNES:
        puntaje = 0
        razones = ["¡Esta contraseña está en la lista de las más usadas y débiles del mundo!"]
    else:
        puntaje += 1
        razones.append("No está en la lista de contraseñas comunes")

    # Clasificación final según el puntaje
    if puntaje <= 2:
        nivel = "Débil"
    elif puntaje <= 4:
        nivel = "Media"
    else:
        nivel = "Fuerte"

    return {
        "puntaje": puntaje,
        "nivel": nivel,
        "razones": razones
    }