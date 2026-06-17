import csv

print("===================================")
print("Bienvenido a Algorize")
print("Agencia de Marketing Digital y SEO")
print("===================================")

nombre = input("Ingrese su nombre: ")
empresa = input("Ingrese el nombre de su empresa: ")
url = input("Ingrese la URL de su sitio web: ")

print("\nSeleccione el servicio requerido:")
print("1 - Auditoría SEO")
print("2 - SEO Técnico")
print("3 - Estrategia de Contenidos")
print("4 - Consulta Comercial")

opcion = input("Opción: ")

servicios = {
    "1": "Auditoría SEO",
    "2": "SEO Técnico",
    "3": "Estrategia de Contenidos",
    "4": "Consulta Comercial"
}

servicio = servicios.get(opcion, "Consulta Comercial")

with open("solicitudes.csv", "a", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([nombre, empresa, url, servicio])

print("\nSolicitud registrada correctamente.")
print(f"Servicio asignado: {servicio}")
print("Gracias por contactarse con Algorize.")