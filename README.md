# Algorize Chatbot

## Descripción del proyecto

Algorize Chatbot es una solución desarrollada en Python para automatizar el proceso de recepción, clasificación y derivación de consultas comerciales dentro de una agencia ficticia de marketing digital y SEO denominada **Algorize**.

El proyecto fue desarrollado como Trabajo Práctico Integrador para la materia **Organización Empresarial**, aplicando conceptos de gestión por procesos, modelado BPMN, análisis sistémico, automatización de procesos administrativos y control de versiones mediante Git y GitHub.

La solución busca optimizar el proceso inicial de atención a potenciales clientes, reduciendo tareas manuales y mejorando la calidad de la información recibida.

---

## Objetivo

Automatizar el proceso de recepción y clasificación de consultas de potenciales clientes mediante un chatbot capaz de:

* Solicitar información relevante.
* Validar los datos ingresados.
* Clasificar automáticamente el tipo de solicitud.
* Registrar la información en una base de datos simulada.
* Derivar cada consulta al área correspondiente.

---

## Tecnologías utilizadas

* Python 3
* CSV (Base de datos simulada)
* Git
* GitHub
* Visual Studio Code

---

## Funcionalidades implementadas

### Registro de consultas

El chatbot solicita:

* Nombre del contacto.
* Empresa.
* Sitio web.
* Tipo de servicio requerido.

### Validaciones

* Validación de campos obligatorios.
* Validación de formato de URL.
* Validación de opciones del menú.

### Clasificación automática

El sistema clasifica la solicitud en una de las siguientes categorías:

1. Auditoría SEO
2. SEO Técnico
3. Estrategia de Contenidos
4. Consulta Comercial

### Derivación

Cada solicitud es derivada automáticamente al área correspondiente.

### Persistencia de datos

La información es almacenada en un archivo CSV denominado:

`solicitudes.csv`

---

## Estructura del proyecto

```text
algorize-chatbot
│
├── main.py
├── solicitudes.csv
└── README.md
```

---

## Ejecución del proyecto

### Clonar el repositorio

```bash
git clone https://github.com/guadapereyram/algorize-chatbot.git
```

### Ingresar al proyecto

```bash
cd algorize-chatbot
```

### Ejecutar el chatbot

```bash
python main.py
```

---

## Flujo general del chatbot

1. Inicio de la conversación.
2. Solicitud de nombre.
3. Solicitud de empresa.
4. Solicitud de sitio web.
5. Validación de URL.
6. Selección del servicio requerido.
7. Clasificación de la solicitud.
8. Registro de la información.
9. Derivación al área correspondiente.
10. Finalización del proceso.

---

## Relación con BPMN

El flujo implementado en Python sigue la lógica definida en los diagramas BPMN AS-IS y TO-BE desarrollados durante el análisis del proceso.

La aplicación contempla tanto el camino feliz como diferentes escenarios de error (camino infeliz), garantizando la coherencia entre el modelo de negocio y la implementación.

---

## Autora

Guadalupe Pereyra

Trabajo Práctico Integrador – Organización Empresarial
Tecnicatura Universitaria en Programación
