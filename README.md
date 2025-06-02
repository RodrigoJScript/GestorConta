# 🧠 Arquitectura del Gestor de Contraseñas en Python

Este proyecto es un gestor de contraseñas con interfaz gráfica usando **Tkinter**, base de datos **SQLite3**, y cifrado de contraseñas con **AES**. Soporta autenticación con contraseña maestra (hash + sal), y permite crear, editar y eliminar entradas de credenciales.

---

## 📁 Estructura de Carpetas

password_manager/
│
├── main.py # Punto de entrada de la aplicación
│
├── ui/ # Interfaces gráficas con Tkinter
│ ├── login_window.py # Ventana para el login con contraseña maestra
│ └── main_window.py # Interfaz principal para gestión de contraseñas
│
├── db/ # Manejo de la base de datos SQLite3
│ └── database.py # Conexión y operaciones CRUD
│
├── security/ # Funciones de seguridad
│ ├── hash_utils.py # Hashing + sal para la contraseña maestra
│ └── crypto_utils.py # Cifrado y descifrado AES para contraseñas
│
├── models/ # Representación de objetos del dominio
│ └── credential.py # Modelo de datos para credenciales
│
└── config/
└── settings.py # Constantes y configuración global


---

## ⚙️ Funcionalidades Principales

### 🔐 1. Login con Contraseña Maestra
- La primera vez, se solicita crear una contraseña maestra.
- Se guarda un `hash(sal + contraseña)` junto con la sal en SQLite.
- En inicios posteriores, se compara el hash para autenticar.

### 📝 2. Gestión de Credenciales
- **Guardar** sitio web, usuario y contraseña cifrada (AES).
- **Editar** datos existentes con recifrado seguro.
- **Eliminar** entradas directamente desde la interfaz.

### 🔒 3. Cifrado de Contraseñas
- Cifrado simétrico AES usando el módulo `cryptography`.
- Se almacena también el IV usado en el cifrado para poder descifrar después.
- La clave se deriva de la contraseña maestra o se guarda en entorno seguro.

---

## 🧰 Stack de Herramientas

| Componente             | Herramienta              | Descripción                                           |
|------------------------|--------------------------|-------------------------------------------------------|
| Interfaz Gráfica       | Tkinter                  | UI nativa simple y funcional                          |
| Base de Datos          | SQLite3                  | Base de datos embebida para credenciales              |
| Cifrado                | `cryptography` (AES)     | Cifrado de contraseñas y gestión de IV                |
| Hash                   | `hashlib` + `os.urandom` | Hash seguro con sal para la contraseña maestra        |
| Derivación de Clave    | `PBKDF2HMAC`             | Deriva claves seguras para el cifrado AES             |

---