# 🛡️ Security Toolkit

Suite de herramientas de ciberseguridad desarrollada en Python, enfocada en fundamentos de redes, buenas prácticas de seguridad y protección de contraseñas.

## 📋 Menú principal

Al ejecutar el programa, se muestra un menú para elegir entre los módulos disponibles:

```bash
python main.py
```
---
=== Security Toolkit ===

Escáner de puertos
Analizador de contraseñas

## 📌 Módulo 1: Escáner de Puertos

Analiza una dirección IP y detecta qué puertos están abiertos dentro de un rango definido por el usuario.

### ¿Cómo funciona?

El programa intenta establecer una conexión TCP con cada puerto del rango especificado. Si la conexión es exitosa, el puerto se marca como abierto; si no responde dentro del tiempo límite, se considera cerrado.

## 📌 Módulo 2: Analizador de Contraseñas

Evalúa qué tan segura es una contraseña, asignándole un puntaje y un nivel (Débil, Media, Fuerte) según varios criterios.

### Criterios evaluados

- Longitud (mínimo recomendado: 12+ caracteres)
- Combinación de mayúsculas y minúsculas
- Presencia de números
- Presencia de símbolos especiales
- Verificación contra una lista de contraseñas comunes/débiles conocidas

## 🧰 Tecnologías utilizadas

- **Python 3** — lenguaje principal
- **Sockets** (librería estándar) — conexiones de red para el escáner de puertos
- Lógica de validación de cadenas de texto para el analizador de contraseñas

## 📂 Estructura del proyecto
seguridad/
├── main.py
├── port_scanner/
│   └── scanner.py
├── password_analyzer/
│   └── analyzer.py
├── requirements.txt
└── readme.md
## ⚠️ Uso ético

Esta herramienta fue creada con fines educativos y de aprendizaje. Escanear puertos de sistemas o redes sin autorización explícita puede ser ilegal según la legislación de cada país. Úsala únicamente en tus propios sistemas o con permiso explícito del propietario.

## 🚀 Próximos módulos

- [x] Escáner de puertos
- [x] Analizador de fortaleza de contraseñas
- [ ] Registro de resultados en base de datos (MongoDB/MySQL)

## Autor

Sebastián David Jiménez Sarmiento — Ingeniero de Sistemas
