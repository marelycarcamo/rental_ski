# 🏔️ Rental Ski
## Aplicación Web FullStack con Django y PostgreSQL


Rental Ski es una aplicación diseñada para facilitar la gestión del arriendo de equipos de ski en la zona del volcán Villarrica, resolviendo problemas comunes como la falta de control en la disponibilidad de equipos, la gestión manual de reservas y la comunicación entre clientes y operarios. Esta plataforma permite a los clientes arrendar equipos de manera sencilla y rápida, mientras que los operarios pueden supervisar y administrar los arriendos, incluyendo la evaluación del estado de los equipos.

### Características principales:

- Registro y autenticación de usuarios con roles diferenciados (cliente, operario, superadmin).
- Visualización y filtrado de equipos disponibles para arriendo.
- Formulario de arriendo con validaciones para asegurar fechas válidas y disponibilidad.
- Gestión de arriendos con historial personalizado para clientes.
- Panel para operarios donde pueden comentar y evaluar el estado de los equipos arrendados.
- Bloqueo automático de clientes en caso de daños reportados en los equipos.
- Integración con PostgreSQL para almacenamiento robusto y seguro de datos.
- Interfaz responsiva y amigable basada en Bootstrap para una experiencia óptima en distintos dispositivos.

Esta aplicación es ideal para negocios de arriendo de equipos deportivos que buscan digitalizar y optimizar sus procesos, mejorando la experiencia tanto de clientes como de operarios.

![Django](https://img.shields.io/badge/Django-4.x-green?style=flat-square) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16%2F17-blue?style=flat-square) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple?style=flat-square) ![License](https://img.shields.io/badge/License-Privado-red?style=flat-square)

Aplicación web desarrollada para gestionar el arriendo de equipos de ski en la zona del volcán Villarrica. Permite a clientes registrarse, arrendar equipos disponibles, y a operarios gestionar observaciones de los arriendos.

---

## ⚙️ Instalación del Proyecto

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/marelycarcamo/rental_ski
   cd rental_sky
   ```

2. **Crear entorno virtual**

	```bash
	python -m venv env
	source env/bin/activate  # En Windows: env\Scripts\activate
	```

3. **Instalar dependencias**

	```bash
	pip install -r requirements.txt
	```


4. **Configurar base de datos PostgreSQL**
	- Crear una base de datos llamada ``rental_ski``

	- Restaurar el dump desde pgAdmin o terminal:
	```bash
	pg_restore -U tu_usuario -d rental_ski dump-rental_ski.db-202408150909
	```

5. **Aplicar migraciones**
	```bash
	python manage.py migrate
	```

6. **Correr el servidor**
	```bash
	python manage.py runserver
	```


Aplicación web desarrollada para gestionar el arriendo de equipos de ski en la zona del volcán Villarrica. Permite a clientes registrarse, arrendar equipos disponibles, y a operarios gestionar observaciones de los arriendos.

---

## 👤 Usuarios de Prueba

| Rol        | Usuario               | Contraseña   |
|------------|-----------------------|--------------|
| Superadmin | admin                 | admin        |
| Cliente    | cliente1@example.com  | cliente123   |
| Operario   | operario1@example.com | operario123  |

---

## 🗺️ Rutas y Navegación

| Ruta                        | Descripción                                | Roles      |
|----------------------------|--------------------------------------------|------------|
| `/admin/`                  | Panel de administración Django.            | Superadmin |
| `/`                        | Página inicial con equipos disponibles.    | Cliente    |
| `/registro/`               | Registro de nuevos usuarios.                | Público    |
| `/login/`                  | Login personalizado con redirección por tipo de usuario. | Público    |
| `/logout/`                 | Cierre de sesión.                           | Todos      |
| `/equipos/`                | Lista de equipos disponibles.               | Cliente    |
| `/equipos/<id>/arrendar/`  | Formulario para arrendar equipo.            | Cliente    |
| `/mis-arriendos/`          | Vista personalizada de arriendos del cliente. | Cliente    |
| `/arriendo/`               | Vista de arriendos para operarios.          | Operario   |
| `/comentario-arriendo/<id>/` | Comentario y evaluación de arriendo.      | Operario   |
| `/facebook/`, `/instagram/`, etc. | Redirección a redes sociales oficiales. | Todos      |


---



## 🗄️ Modelos de Datos

| Modelo    | Campos                                   | Descripción / Notas                         |
|-----------|-----------------------------------------|---------------------------------------------|
| Usuario   | `auth_user` (1:1), `created`, `tipo`   | Tipo: cliente u operario                     |
| Categoría | `nombre`                               | Ej: Ski, Botas, Trineo, Snowboard, Otros    |
| Equipo    | `nombre`, `imagen`, `precio`, `estado`, `categoria` | Estado: disponible, arrendado, mantención   |
| Arriendo  | `fecha`, `observacion`, `danado`, `equipo`, `user` | Si `danado=True`, cliente bloqueado 1 mes   |

---

## 📝 Formularios y Validaciones

ArrendarEquipoForm

- Campo ``fecha`` con validación: no puede ser anterior a hoy

- Estilos personalizados con Bootstrap

- Mensajes de error y éxito integrados con ``messages``.

---

## 🎨 Frontend y Templates

- ``base.html``: estructura principal, incluye navbar y footer

- ``navbar.html``: navegación dinámica según rol

- ``equipo_list.html``: lista de equipos con filtro por categoría

- ``arrendar.html``: formulario de arriendo con imagen, precio y fecha

- ``arriendo.html``: vista de operarios para comentar arriendos

- ``mis_arriendos.html``: vista de cliente con historial

---

## 🔐 Reglas de Negocio

- Solo se pueden arrendar equipos en estado disponible

- No se puede arrendar equipos en estado arrendado o en mantención

- La fecha de arriendo debe ser igual o posterior a la fecha actual

- Si un operario comenta un arriendo como dañado, el cliente queda bloqueado por 1 mes

---

## 📌 Supuestos Técnicos

- Las imágenes se almacenan como URL

- Se usa Django Auth para autenticación y encriptación

- Validación de formularios en Backend

- Proyecto estructurado bajo patrón MVP

---

## 🧪 Dependencias

- Python 3.10+

- Django 4.x

- psycopg2

- Bootstrap 5.3.3

- Bootstrap Icons 1.11.3

---

## 🌐 Recursos Externos

Para mejorar la apariencia y funcionalidad, se utilizan los siguientes recursos externos:

- **Google Fonts: Roboto**

  Incluye la fuente Roboto para una tipografía moderna y legible.

  ```html
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
  ```

- 	**jQuery 3.7.1**
	Biblioteca JavaScript para facilitar la manipulación del DOM y eventos.
	```html
	<script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-3gJwYpMe3QewGELvNaK7PYZt27NXFoaoApmYm81iuXo=" crossorigin="anonymous"></script>
	```

---

## 📁 Estructura del Proyecto

rental_ski/
├── rental_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── navbar.html
│   │   ├── equipo_list.html
│   │   ├── arrendar.html
│   │   ├── arriendo.html
│   │   └── mis_arriendos.html
├── static/
│   ├── css/
│   ├── img/
│   └── js/
├── rental_ski.sql
├── README.txt
└── manage.py

---

## 🧭 Créditos

Desarrollado por Marely para Talento Digital — Valdivia 2024.

Si tienes dudas sobre cómo restaurar la base de datos o levantar el entorno, revisa los pasos en la sección de instalación o contacta al instructor a cargo.