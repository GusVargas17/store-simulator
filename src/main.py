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

def ver_carrito():
    if not carro_compras:
        print("Tu carrito está vacío 🛒. ¡Agrega productos para comenzar tu compra!")
        return
    encabezado = f'{"Producto":<13} | {"Cantidad":<10} | {"Precio":<9} | {"Subtotal":<10}'
    print(encabezado)
    print("-" * len(encabezado))

    total = 0

    for articulo in carro_compras:
        producto = articulo["nombre"]
        cantidad = articulo["cantidad"]
        precio = articulo["precio"]
        subtotal = cantidad * precio
        total += subtotal
        linea = f'{producto:<13} | {str(cantidad):^10} | S/{precio:<7.2f} | S/{subtotal:<8.2f}'
        print(linea)
    print("-" * len(encabezado))
    print(f"total a pagar: S/{total:.2f}")

#mostrar_menu()
#ver_catalogo()
#agregar_producto_al_carrito("A002")
#carro_compras.clear()
#carro_compras.append({"codigo": "A001", "nombre": "Pan", "precio": 1.5, "cantidad": 2})
#carro_compras.append({"codigo": "C001", "nombre": "Chocolate", "precio": 1.8, "cantidad": 3})
#ver_carrito()