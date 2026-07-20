# 🛡️ Security Toolkit

Suite de herramientas de ciberseguridad desarrollada en Python, enfocada en fundamentos de redes, buenas prácticas de seguridad y protección de contraseñas, con persistencia de datos en MySQL.

## 📋 Menú principal

Al ejecutar el programa, se muestra un menú para elegir entre los módulos disponibles:

```bash
python main.py
```
=== Security Toolkit ===

Escáner de puertos
Analizador de contraseñas

---

## 📌 Módulo 1: Escáner de Puertos

Analiza una dirección IP y detecta qué puertos están abiertos dentro de un rango definido por el usuario. Cada resultado se guarda automáticamente en una base de datos MySQL.

### ¿Cómo funciona?

El programa intenta establecer una conexión TCP con cada puerto del rango especificado. Si la conexión es exitosa, el puerto se marca como abierto; si no responde dentro del tiempo límite, se considera cerrado.

### Ejemplo de uso
Ingresa la IP a escanear: 127.0.0.1
Puerto inicial: 1
Puerto final: 1000
--- Resultado ---
Puertos abiertos encontrados: [135, 445]
✅ Resultado guardado en la base de datos.
---

## 📌 Módulo 2: Analizador de Contraseñas

Evalúa qué tan segura es una contraseña, asignándole un puntaje y un nivel (Débil, Media, Fuerte) según varios criterios.

### Criterios evaluados

- Longitud (mínimo recomendado: 12+ caracteres)
- Combinación de mayúsculas y minúsculas
- Presencia de números
- Presencia de símbolos especiales
- Verificación contra una lista de contraseñas comunes/débiles conocidas

### Ejemplo de uso
Ingresa la contraseña a analizar: MiClave2026!Segura
Nivel de seguridad: Fuerte (6/6 puntos)
Detalles:

Longitud excelente (12+ caracteres)
Combina mayúsculas y minúsculas
Contiene números
Contiene símbolos especiales
No está en la lista de contraseñas comunes
---

## 📌 Módulo 3: Persistencia en Base de Datos (MySQL)

Cada escaneo de puertos se registra automáticamente en una base de datos MySQL, permitiendo consultar el historial de escaneos realizados.

### Estructura de la tabla `escaneos`

| Campo             | Tipo      | Descripción                          |
|-------------------|-----------|---------------------------------------|
| id                | INT       | Identificador único (autoincremental) |
| ip                | VARCHAR   | IP escaneada                          |
| puerto_inicio     | INT       | Puerto inicial del rango              |
| puerto_fin        | INT       | Puerto final del rango                |
| puertos_abiertos  | VARCHAR   | Lista de puertos abiertos encontrados |
| fecha_escaneo     | DATETIME  | Fecha y hora del escaneo (automática) |

### Seguridad de credenciales

La contraseña de la base de datos se maneja mediante variables de entorno (archivo `.env`, excluido del repositorio vía `.gitignore`), evitando exponer credenciales en el código fuente.

---

## 🧰 Tecnologías utilizadas

- **Python 3** — lenguaje principal
- **Sockets** (librería estándar) — conexiones de red para el escáner de puertos
- **MySQL** — persistencia de resultados
- **mysql-connector-python** — conexión entre Python y MySQL
- **python-dotenv** — manejo seguro de variables de entorno

## 📂 Estructura del proyecto
seguridad/
├── main.py
├── .env                    (no incluido en el repositorio)
├── .gitignore
├── port_scanner/
│   └── scanner.py
├── password_analyzer/
│   └── analyzer.py
├── database/
│   └── db.py
├── requirements.txt
└── readme.md
## ⚙️ Instalación y configuración

1. Clona el repositorio
2. Instala las dependencias:
```bash
pip install mysql-connector-python python-dotenv
```
3. Crea una base de datos MySQL llamada `security_toolkit` con la tabla `escaneos` (ver estructura arriba)
4. Crea un archivo `.env` en la raíz del proyecto con tu contraseña de MySQL:
DB_PASSWORD=tu_contraseña_aqui
5. Ejecuta el programa:
```bash
python main.py
```

## ⚠️ Uso ético

Esta herramienta fue creada con fines educativos y de aprendizaje. Escanear puertos de sistemas o redes sin autorización explícita puede ser ilegal según la legislación de cada país. Úsala únicamente en tus propios sistemas o con permiso explícito del propietario.

## 🚀 Módulos completados

- [x] Escáner de puertos
- [x] Analizador de fortaleza de contraseñas
- [x] Persistencia de resultados en MySQL

## Autor

Sebastián David Jiménez Sarmiento — Ingeniero de Sistemas
