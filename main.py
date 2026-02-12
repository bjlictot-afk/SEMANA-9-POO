# Programa principal
# Implementa el menú interactivo en consola

from modelos.producto import Producto
from servicios.inventario import Inventario

def menu():
    print("\nSISTEMA DE GESTIÓN DE INVENTARIOS")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese el ID a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("ID inválido.")

        elif opcion == "3":
            try:
                id_producto = int(input("ID del producto: "))
                cantidad = input("Nueva cantidad (enter para omitir): ")
                precio = input("Nuevo precio (enter para omitir): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
