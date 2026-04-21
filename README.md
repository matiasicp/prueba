# Sistema de Gestión de Red Jerárquica (Evaluación Ítem I)

Este proyecto consiste en un script de Python diseñado para la documentación y gestión de una topología de red basada en el modelo jerárquico de Cisco (Acceso, Distribución y Núcleo).

##  Mejoras Implementadas
Partiendo del código base, se realizaron las siguientes optimizaciones para cumplir con los requisitos de la asignatura:

1.  **Escalabilidad Dinámica:** Se implementó una lógica que permite añadir nuevos campus y servicios sin necesidad de modificar el código fuente.
2.  **Persistencia de Datos:** El programa genera y lee archivos de texto externos (`.txt`) por cada campus, asegurando que la información se mantenga guardada localmente.
3.  **Atributos Técnicos Críticos:** Se añadieron campos obligatorios para la administración de redes:
    * Direccionamiento IP (IPv4/IPv6).
    * Configuración de VLANs (VLAN Nativa 90, Administración 20, etc.).
    * Clasificación por Capas (Modelo Jerárquico).
4.  **Gestión de Errores:** Se optimizó la lectura de archivos utilizando context managers (`with open`), evitando bloqueos en la memoria de la máquina virtual.

## Documentación del Modelo Jerárquico
Basado en la topología analizada, el sistema permite registrar dispositivos en las siguientes capas:

* **Capa de Núcleo (Core):** Gestión de enrutamiento de alta velocidad (Routers de borde y VPN Site-to-Site).
* **Capa de Distribución:** Switches multicapa que gestionan el enrutamiento Inter-VLAN y servicios de redundancia.
* **Capa de Acceso:** Switches finales y conectividad para usuarios (VLANs de Ventas, Procesos, Finanzas).


