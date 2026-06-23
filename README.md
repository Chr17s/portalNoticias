# 📰 Noticias FAC - Portal de Noticias Full Stack

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-092E20.svg?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791.svg?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?logo=docker)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-F80000.svg?logo=oracle)

## 📋 Descripción del Proyecto

**Noticias FAC** es una plataforma web de publicación de noticias con un diseño editorial profesional y limpio.

Desarrollado como proyecto universitario Full Stack, el sistema permite a los usuarios registrarse, iniciar sesión y comentar las noticias. Cuenta con una arquitectura modular basada en Class Based Views (CBV), gestión de accesos y permisos según roles de usuario, y un panel de control (Dashboard) con estadísticas generales.

---

## 🚀 Características Principales

- **Autenticación y Seguridad:** Implementación de autenticación completa utilizando un modelo de usuario personalizado llamado `CustomUser`. Incluye registro de usuarios, inicio de sesión, cierre de sesión, y flujos de cambio y restablecimiento de contraseña.
- **CRUD de Noticias Protegido:** Funcionalidad completa para crear noticia, listar noticias, ver detalle, editar noticia y eliminar noticia. Los permisos garantizan que solo los autores o administradores puedan editar o eliminar sus noticias.
- **Interacción y Participación:** Sistema donde los usuarios normales registrados pueden comentar en las publicaciones.
- **Búsqueda Avanzada y Filtros:** Incorpora funcionalidad diferenciadora para buscar noticias por título y por categoría, además de filtro por categoría.
- **Dashboard de Estadísticas:** Panel de control que muestra el total de noticias, noticias aprobadas, total de comentarios y total de usuarios registrados.
- **Manejo de Archivos Multimedia:** Capacidad para subir imágenes para las noticias y visualizarlas correctamente mediante la configuración de `MEDIA_ROOT` y `MEDIA_URL`.
- **Interfaz Profesional:** Construida con Bootstrap 5, utilizando herencia de templates a partir de un archivo `base.html` con barra de navegación (`navbar`) y pie de página (`footer`) reutilizables.

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.12**
- **Django 5.2**
- **Pillow** para el manejo de imágenes en los modelos
- **WhiteNoise** para el despacho de archivos estáticos en producción

### Base de Datos & Contenedores
- **PostgreSQL** como motor relacional obligatorio
- **psycopg2-binary** como adaptador de base de datos
- **Docker y Docker Compose** para la ejecución local con servicios de `web` y `db`, asegurando la persistencia de datos mediante volúmenes

### Frontend
- **Bootstrap 5** para el diseño de la interfaz
- **crispy-bootstrap5** y **django-crispy-forms** para la renderización y visualización de formularios

---

## ⚙️ Configuración de Variables de Entorno (.env)

La seguridad y configuración del proyecto se manejan mediante un archivo `.env`. Crea este archivo en la raíz del proyecto con la siguiente estructura:

```env
# Configuración Core de Django
SECRET_KEY=clave_secreta_generada_aleatoriamente_y_segura
DEBUG=True  # Cambiar a False en producción en Oracle Cloud
ALLOWED_HOSTS=localhost,127.0.0.1,150.136.193.94

# Configuración de Base de Datos PostgreSQL en Docker
POSTGRES_DB=noticias_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=Admin#1234
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Credenciales de Servidor de Correos SMTP
EMAIL_USER=crishdz690@gmail.com
EMAIL_PASS=xxxx_xxxx_xxxx_xxxx
