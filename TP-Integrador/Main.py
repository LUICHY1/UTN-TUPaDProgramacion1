import archivo
import operaciones
import estadisticas
import validaciones

def mostrar_menu():
    print("\n--- Gestíon de Datos de Países ---")
    print("1. Cargar datos desde CSV")
    print("2. Agregar un nuevo país")
    print("3. Actualizar datos de un país")
    print("4. Buscar un país por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Salir")

def main():
    paises = []
    datos_cargados = False
    while True:
        mostrar_menu()
        opcion = validaciones.validar_entero_positivo("Seleccione una opción (1-8): ")

        if opcion == 1:
            nombre_arch = input("Ingrese el nombre del archivo CSV (ej: paises.csv): ")
            #Aquí abajo llamas a la función que esta en el otro archivo
            paises = archivo.cargar_datos(nombre_arch)
            if paises:
                datos_cargados = True
                print(f"Se cargaron {len(paises)} países.")
        elif opcion == 8:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        #Validamos que los datos estén cargados para las otras opciones
        elif datos_cargados:
            if opcion == 2:
                paises = operaciones.agregar_pais(paises)
            elif opcion == 3:
                paises = operaciones.actualizar_pais(paises)
            elif opcion == 4:
                operaciones.buscar_pais(paises)
            elif opcion == 5:
                operaciones.menu_filtrar(paises)
            elif opcion == 6:
                operaciones.menu_ordenar(paises)
            elif opcion == 7:
                estadisticas.mostrar_estadisticas(paises)
            else:
                print("Error: Opción no válida (1-8).")
        else:
            print("Error: Primero debe cargar los datos (Opción 1).")

# .. (resto de las opciones) ..
main()