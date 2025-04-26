bodega = [
    {
        "codigo": "A001",
        "nombre": "Pan",
        "precio": 1.50,
        "stock": 10
    },
    {
        "codigo": "B001",
        "nombre": "Leche",
        "precio": 3.50,
        "stock": 10
    },
    {
        "codigo": "C001",
        "nombre": "Chocolate",
        "precio": 1.80,
        "stock": 10
    }
]

carro_compras = []

def mostrar_menu():
    print("""Bienvenido a la tienda virtual 🛍️
¿Qué deseas hacer?

1. Ver catálogo
2. Agregar producto al carrito
3. Eliminar producto del carrito
4. Vaciar carrito
5. Mostrar carrito
6. Finalizar compra
7. Salir
    """)

def ver_catalogo():
    encabezado = f'{"Código":<10} | {"Producto":<15} | {"Precio":<8} | {"stock":<6}'
    print(encabezado)
    print("-" * len(encabezado))

    for producto in bodega:
        codigo = producto["codigo"]
        nombre = producto["nombre"]
        precio = producto["precio"]
        stock = producto["stock"]
        linea = f'{codigo:<10} | {nombre:<15} | S/{precio:<6} | {stock:<6}'
        print(linea)

def agregar_producto_al_carrito(codigo_producto):
    for producto in bodega:
        if codigo_producto == producto["codigo"]:
            cantidad_ingresada = input(f"¿Cúantos unidades de {producto['nombre']} desea agregar? (Stock disponible: {producto['stock']}): ")
            if not cantidad_ingresada.isdigit():
                print("Ingrese un número válido porfavor.")
                return

            cantidad = int(cantidad_ingresada)

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                return
            if cantidad > producto["stock"]:
                print(f"No hay suficiente stock. Solo hay {producto['stock']} unidades")
                return

            carro_compras.append({
                "codigo": producto["codigo"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            })
            producto["stock"] -= cantidad
            print(f'Se agregó el producto: {producto["nombre"]} al carro de compras')
            return
    print(f"El código: {codigo_producto} es inválido, ingrese otro código")

#mostrar_menu()
ver_catalogo()
#agregar_producto_al_carrito("A002")