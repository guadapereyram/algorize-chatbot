import csv
import re
from datetime import datetime


ARCHIVO_SOLICITUDES = "solicitudes.csv"


def mostrar_bienvenida():
    print("===================================")
    print("Bienvenido a Algorize")
    print("Agencia de Marketing Digital y SEO")
    print("===================================")


def solicitar_dato_obligatorio(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato:
            return dato

        print("Dato inválido. Este campo no puede quedar vacío.\n")


def validar_url(url):
    patron = r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}.*$"
    return re.match(patron, url) is not None


def solicitar_url():
    while True:
        url = input("Ingrese la URL de su sitio web: ").strip()

        if validar_url(url):
            return url

        print("URL inválida. Ingrese una URL válida, por ejemplo: www.algorize.com\n")


def seleccionar_servicio():
    servicios = {
        "1": ("Auditoría SEO", "Equipo de Auditoría SEO"),
        "2": ("SEO Técnico", "Equipo Técnico SEO"),
        "3": ("Estrategia de Contenidos", "Equipo de Contenidos"),
        "4": ("Consulta Comercial", "Área Comercial")
    }

    while True:
        print("\nSeleccione el servicio requerido:")
        print("1 - Auditoría SEO")
        print("2 - SEO Técnico")
        print("3 - Estrategia de Contenidos")
        print("4 - Consulta Comercial")

        opcion = input("Opción: ").strip()

        if opcion in servicios:
            return servicios[opcion]

        print("Opción inválida. Debe seleccionar una opción del 1 al 4.\n")


def registrar_solicitud(nombre, empresa, url, servicio, area):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARCHIVO_SOLICITUDES, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([fecha, nombre, empresa, url, servicio, area, "Registrada"])


def main():
    mostrar_bienvenida()

    print("\nEstado actual: INICIO")

    print("\nEstado actual: ESPERANDO_NOMBRE")
    nombre = solicitar_dato_obligatorio("Ingrese su nombre: ")

    print("\nEstado actual: ESPERANDO_EMPRESA")
    empresa = solicitar_dato_obligatorio("Ingrese el nombre de su empresa: ")

    print("\nEstado actual: ESPERANDO_URL")
    url = solicitar_url()

    print("\nEstado actual: CLASIFICANDO_SOLICITUD")
    servicio, area = seleccionar_servicio()

    print("\nEstado actual: REGISTRANDO_SOLICITUD")
    registrar_solicitud(nombre, empresa, url, servicio, area)

    print("\nSolicitud registrada correctamente.")
    print(f"Servicio asignado: {servicio}")
    print(f"Derivación interna: {area}")
    print("Estado final: FINALIZADO")
    print("Gracias por contactarse con Algorize.")


main()