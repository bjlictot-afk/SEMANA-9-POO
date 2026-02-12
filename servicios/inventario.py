# Clase Inventario
# Gestiona las operaciones sobre los productos

from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []  # Lista principal de almacenamiento

    def añadir_producto(self, producto):
        # Validar que el ID no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print(" Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(" Producto eliminado.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_inventario(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for p in self.productos:
                print(p)
