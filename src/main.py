bodega = [
    {
        "codigo": "A001",
        "nombre": "Pan",
        "precio": 1.50
    },
    {
        "codigo": "B001",
        "nombre": "Leche",
        "precio": 3.50
    },
    {
        "codigo": "C001",
        "nombre": "Chocolate",
        "precio": 1.80
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
    print(f'{"Código":<15} | {"Producto":<15} | {"Precio":<6}')
    print("-" * 42)
    for producto in bodega:
        print(f'Código: {producto["codigo"]:<7} | {producto["nombre"]:<15} | S/{producto["precio"]:<6}')

def agregar_producto_al_carrito(codigo_producto):
    for producto in bodega:
        if codigo_producto == producto["codigo"]:
            carro_compras.append(producto)
            print(f"Se agregó el producto: {producto["nombre"]} al carro de compras")
            return
    print(f"El código: {codigo_producto} es inválido, ingrese otro código")

mostrar_menu()
ver_catalogo()
agregar_producto_al_carrito("A002")