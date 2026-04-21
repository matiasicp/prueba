import os

# Inicialización de variables
x = 0
y = 1
os.system("clear")
# Lista de campus actualizada según tu topología
campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]

print("¿Qué quiere hacer?")
print("1. Ver los dispositivos\n2. Ver los campus\n3. Añadir dispositivo\n4. Añadir campus\n5. Salir")

selector = input("\nElegir una opción: ")

if selector == "1":
    os.system("clear")
    y = 1
    print("Elija un campus para ver sus dispositivos:\n")
    for item in campus:
        print(f"{y}. {item}")
        y += 1
    
    opcion_c = int(input("\nElija una opción: ")) - 1
    if 0 <= opcion_c < len(campus):
        os.system("clear")
        nombre_archivo = campus[opcion_c].replace(" ", "_") + ".txt"
        
        if os.path.exists(nombre_archivo):
            # Abrimos y leemos el archivo
            with open(nombre_archivo, "r") as file:
                print(f"--- DISPOSITIVOS EN {campus[opcion_c].upper()} ---")
                print(file.read())
        else:
            print("No hay dispositivos registrados en este campus.")

elif selector == "2":
    os.system("clear")
    print("Lista de Campus Actuales:")
    for i, item in enumerate(campus, 1):
        print(f"{i}. {item}")

elif selector == "3":
    os.system("clear")
    y = 1
    servicios = []
    print("¿Dónde agregar nuevo dispositivo?\n")
    for item in campus:
        print(f"{y}. {item}")
        y += 1
    
    opcion_c = int(input("\nElija una opción: ")) - 1
    if 0 <= opcion_c < len(campus):
        os.system("clear")
        # Reemplazamos espacios por guiones bajos para el nombre del archivo
        nombre_archivo = campus[opcion_c].replace(" ", "_") + ".txt"
        
        print("Elija un tipo de dispositivo:\n1. Router\n2. Switch\n3. Switch Multicapa")
        tipo_idx = input("Elija su opción: ")
        tipos = {"1": "Router", "2": "Switch", "3": "Switch Multicapa"}
        tipo_disp = tipos.get(tipo_idx, "Dispositivo")

        nombre_disp = input("Agregue el nombre del dispositivo: ")
        ip_disp = input("Agregue la dirección IP: ")
        vlan_disp = input("Agregue las VLANs (ej: 10, 20, 90): ")

        print("\nElija una jerarquía:\n1. Núcleo\n2. Distribución\n3. Acceso")
        jer_idx = input("Elija una opción: ")
        jerarquias = {"1": "Núcleo", "2": "Distribución", "3": "Acceso"}
        capa = jerarquias.get(jer_idx, "No definida")

        os.system("clear")
        # Lógica de servicios (simplificada para que funcione)
        print(f"Defina servicios para {tipo_disp} (escriba 'fin' para terminar):")
        while True:
            srv = input("Servicio: ")
            if srv.lower() == 'fin': break
            servicios.append(srv)

        # ESCRITURA EN ARCHIVO (Mejora de la estructura)
        with open(nombre_archivo, "a") as file:
            file.write(f"\nDispositivo: {tipo_disp} - {nombre_disp}\n")
            file.write(f"IP: {ip_disp} | VLANs: {vlan_disp}\n")
            file.write(f"Jerarquía: {capa}\n")
            file.write(f"Servicios: {', '.join(servicios)}\n")
            file.write("-" * 30 + "\n")
        print("\nDispositivo guardado con éxito.")

elif selector == "4":
    nuevo_c = input("Nombre del nuevo campus: ")
    campus.append(nuevo_c)
    print(f"Campus {nuevo_c} añadido (temporalmente en esta sesión).")
