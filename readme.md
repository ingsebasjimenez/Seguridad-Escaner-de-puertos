# 🛡️ Security Toolkit

Suite de herramientas de ciberseguridad desarrollada en Python, enfocada en fundamentos de redes y buenas prácticas de seguridad.

## 📌 Módulo 1: Escáner de Puertos

Herramienta que analiza una dirección IP y detecta qué puertos están abiertos dentro de un rango definido por el usuario.

### ¿Cómo funciona?

El programa intenta establecer una conexión TCP con cada puerto del rango especificado. Si la conexión es exitosa, el puerto se marca como abierto; si no responde dentro del tiempo límite, se considera cerrado.

### Tecnologías utilizadas

- **Python 3** — lenguaje principal
- **Sockets** (librería estándar de Python) — para las conexiones de red

### Cómo ejecutarlo

```bash
python main.py
```

El programa te pedirá:
- La IP a escanear (ej. `127.0.0.1` para tu propia máquina)
- El puerto inicial del rango
- El puerto final del rango

### Ejemplo de uso
## ⚠️ Uso ético

Esta herramienta fue creada con fines educativos y de aprendizaje. Escanear puertos de sistemas o redes sin autorización explícita puede ser ilegal según la legislación de cada país. Úsala únicamente en tus propios sistemas o con permiso explícito del propietario.

## 🚀 Próximos módulos

- [ ] Analizador de fortaleza de contraseñas
- [ ] Registro de resultados en base de datos (MongoDB/MySQL)

## Autor

Sebastián David Jiménez Sarmiento — Ingeniero de Sistemas