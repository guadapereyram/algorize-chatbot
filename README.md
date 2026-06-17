# Algorize Chatbot

## Descripción del proyecto

Algorize Chatbot es una aplicación desarrollada en Python que automatiza el proceso de recepción, validación, clasificación y derivación de consultas comerciales para una agencia ficticia de Marketing Digital y SEO denominada **Algorize**.

El proyecto fue desarrollado como **Trabajo Práctico Integrador** para la materia **Organización Empresarial** de la **Tecnicatura Universitaria en Programación (UTN)**, aplicando conceptos de análisis sistémico, modelado BPMN 2.0, automatización de procesos administrativos, máquinas de estados y control de versiones mediante Git y GitHub.

La solución reemplaza parte del proceso manual de atención inicial mediante un chatbot capaz de validar información, clasificar solicitudes y derivarlas automáticamente al área correspondiente.

---

# Objetivo

Automatizar el proceso de recepción de consultas comerciales mediante un chatbot capaz de:

- Solicitar información del potencial cliente.
- Validar datos obligatorios.
- Validar la URL del sitio web.
- Clasificar automáticamente el servicio solicitado.
- Registrar la solicitud en una base de datos simulada (CSV).
- Derivar la consulta al área correspondiente.
- Gestionar el camino principal y escenarios de excepción.

---

# Tecnologías utilizadas

- Python 3
- CSV (Base de datos simulada)
- Git
- GitHub
- Visual Studio Code

---

# Funcionalidades implementadas

## Registro de consultas

El chatbot solicita la siguiente información:

- Nombre del contacto.
- Empresa.
- Sitio web.
- Servicio requerido.

---

## Validaciones

El sistema incorpora las siguientes validaciones:

- Campos obligatorios.
- Formato de URL.
- Selección válida del servicio.

---

## Clasificación automática

Las solicitudes son clasificadas automáticamente en una de las siguientes categorías:

1. Auditoría SEO
2. SEO Técnico
3. Estrategia de Contenidos
4. Consulta Comercial

---

## Derivación automática

Según el servicio seleccionado, el chatbot deriva la solicitud al área responsable:

- Equipo de Auditoría SEO
- Equipo Técnico SEO
- Equipo de Contenidos
- Área Comercial

---

## Persistencia de datos

Las solicitudes son registradas automáticamente en un archivo CSV denominado:

`solicitudes.csv`

Cada registro contiene:

- Fecha
- Nombre
- Empresa
- URL
- Servicio
- Área responsable
- Estado

---

## Manejo de excepciones

El chatbot contempla escenarios alternativos durante la ejecución:

- Solicitud de datos faltantes cuando existen campos vacíos.
- Solicitud de una nueva URL cuando el formato es inválido.
- Verificación del registro en la base de datos.
- Notificación de error y derivación a registro manual si el almacenamiento falla.

---

# Estructura del proyecto

```text
algorize-chatbot
│
├── main.py
├── solicitudes.csv
└── README.md
```

---

# Ejecución del proyecto

## Clonar el repositorio

```bash
git clone https://github.com/guadapereyram/algorize-chatbot.git
```

## Ingresar al proyecto

```bash
cd algorize-chatbot
```

## Ejecutar el chatbot

```bash
python main.py
```

---

# Flujo general del chatbot

1. Inicio del proceso.
2. Solicitud de datos del cliente.
3. Validación de datos obligatorios.
4. Validación de la URL.
5. Selección del servicio.
6. Clasificación automática.
7. Derivación al área correspondiente.
8. Registro de la solicitud en el archivo CSV.
9. Verificación del registro.
10. Notificación al cliente.
11. Finalización del proceso.

---

# Máquina de estados implementada

Durante la ejecución, el chatbot atraviesa los siguientes estados:

- INICIO
- ESPERANDO_NOMBRE
- ESPERANDO_EMPRESA
- ESPERANDO_URL
- CLASIFICANDO_SOLICITUD
- VALIDANDO_DATOS_COMPLETOS
- REGISTRANDO_SOLICITUD
- VERIFICANDO_REGISTRO
- FINALIZADO

---

# Relación con BPMN

La implementación desarrollada en Python mantiene la coherencia con el modelo BPMN TO-BE elaborado para el proyecto.

El chatbot contempla tanto el camino principal como los escenarios alternativos representados mediante compuertas exclusivas (Gateways), incluyendo:

- Validación de datos obligatorios.
- Validación de URL.
- Clasificación automática de solicitudes.
- Derivación al área correspondiente.
- Manejo de errores durante el registro de la información.

De esta manera se garantiza la correspondencia entre el análisis del proceso de negocio y su implementación.

---

# Autora

**Guadalupe Pereyra**

Trabajo Práctico Integrador

Materia: Organización Empresarial

Tecnicatura Universitaria en Programación

Universidad Tecnológica Nacional (UTN)