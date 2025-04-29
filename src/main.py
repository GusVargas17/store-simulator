from datetime import datetime
from typing import List, Dict, Optional

bodega: List[Dict[str, str | float | int]] = [
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

carro_compras: List[Dict[str, str | float | int]] = []

def buscar_producto_en_bodega(codigo: str) -> Optional[Dict[str, str | float | int]]:
    for producto in bodega:
        if producto["codigo"] == codigo:
            return producto
    return None

def mostrar_menu() -> None:
    print("""Bienvenido a la tienda virtual 🛍️
¿Qué deseas hacer?

1. Ver catálogo
2. Agregar producto al carrito
3. Eliminar producto del carrito
4. Vaciar carrito
5. Mostrar carrito
6. Finalizar compra
7. Ver historial de compras
8. Salir
    """)

def ver_catalogo() -> None:
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

def agregar_producto_al_carrito(codigo_producto: str) -> None:
    producto = buscar_producto_en_bodega(codigo_producto)

    if not producto:
        print(f"El código: {codigo_producto} es inválido, ingrese otro código")
        return
    cantidad_ingresada = input(f"¿Cúantos unidades de {producto['nombre']} desea agregar? (Stock disponible: {producto['stock']}): ")
    if not cantidad_ingresada.isdigit():
        print("Ingrese un número válido por favor.")
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

def calcular_total(carrito: List[Dict[str, str | float | int]]) -> float:
    return round(sum(item["cantidad"] * item["precio"] for item in carrito), 2)

def ver_carrito() -> None:
    if not carro_compras:
        print("Tu carrito está vacío 🛒. ¡Agrega productos para comenzar tu compra!")
        return

    encabezado = f'{"Producto":<13} | {"Cantidad":<10} | {"Precio":<9} | {"Subtotal":<10}'
    print(encabezado)
    print("-" * len(encabezado))

    for articulo in carro_compras:
        producto = articulo["nombre"]
        cantidad = articulo["cantidad"]
        precio = articulo["precio"]
        subtotal = round(cantidad * precio, 2)
        linea = f'{producto:<13} | {str(cantidad):^10} | S/{precio:<7.2f} | S/{subtotal:<8.2f}'
        print(linea)

    print("-" * len(encabezado))
    total = calcular_total(carro_compras)
    print(f"total a pagar: S/{total:.2f}")

def eliminar_producto_del_carrito(codigo_ingresado: str) -> None:
    for idx, producto in enumerate(carro_compras):
        if producto["codigo"] == codigo_ingresado:
            cantidad_ingresada = input("¿Cuántas unidades va a eliminar?: ")

            if not cantidad_ingresada.isdigit():
                print("Ingrese un numero válido")
                return

            cantidad_a_eliminar = int(cantidad_ingresada)

            if cantidad_a_eliminar <= 0:
                print("Debe eliminar al menos una unidad")
                return
            if cantidad_a_eliminar > producto["cantidad"]:
                print(f"Solo tienes {producto['cantidad']} unidades de {producto['nombre']} en el carrito")
                return
            
            producto["cantidad"] -= cantidad_a_eliminar

            item_bodega = buscar_producto_en_bodega(codigo_ingresado)
            if item_bodega:
                item_bodega["stock"] += cantidad_a_eliminar
            else:
                print("No se encontró producto en la bodega")
                return
            
            if producto["cantidad"] == 0:
                del carro_compras[idx]
                print(f"Se eliminó el producto {producto['nombre']} completamente del carrito.")
            else:
                print(f"Se eliminaron {cantidad_a_eliminar} unidades de {producto['nombre']} del carrito.")

            return
    print("El producto no está en tu carrito")

def vaciar_carrito() -> None: 
    if not carro_compras:
        print("Tu carrito está vacio.")
        return
    
    for producto in carro_compras:
        item_bodega = buscar_producto_en_bodega(producto["codigo"])
        if item_bodega:
            item_bodega["stock"] += producto["cantidad"]

    carro_compras.clear()
    print("Se ha vaciado el carrito correctamente")

def finalizar_compra() -> None:
    if not carro_compras:
        print("No tienes productos en tu carrito")
        return

    print("\nResumen de compra 🧾")
    print("-" * 30)

    for articulo in carro_compras:
        producto = articulo["nombre"]
        cantidad = articulo["cantidad"]
        precio = articulo["precio"]
        subtotal = round(cantidad * precio, 2)
        print(f"{producto} x{cantidad} -> S/{subtotal:.2f}")

    total = calcular_total(carro_compras)
    print("-" * 30)
    print(f"Total a pagar: S/{total:.2f}")
    print("\nProcesando pago... ✅")
    print("¡Gracias por su compra! 🛍️")

    guardar_historial(carro_compras)
    carro_compras.clear()

def guardar_historial(carrito: List[Dict[str, str | float | int]]) -> None:
    if not carrito:
        return
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\nFecha: {fecha}\n")
        archivo.write("Compra:\n")
        for producto in carrito:
            nombre = producto["nombre"]
            cantidad = producto["cantidad"]
            precio = producto["precio"]
            subtotal = cantidad * precio
            archivo.write(f"- {nombre} x{cantidad} -> S/{subtotal:.2f}\n")

        total = calcular_total(carrito)
        archivo.write(f"Total: S/{total:.2f}\n")
        archivo.write("-" * 30 + "\n")

def ver_historial() -> None:
    try:
        with open("historial.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print("\nHistorial de compras:")
                print(contenido)
            else:
                print("\nNo hay historial de compras aún.")
    except FileNotFoundError:
        print("\nEl historial no existe aún. Primero realiza una compra.")

def salir() -> None:
    print("\nGracias por visitar nuestra tienda virtual 🛍️")
    print("¡Hasta pronto! 👋")

def pausar() -> None:
    input("\nPresiona ENTER para continuar...")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            ver_catalogo()
            pausar()
        elif opcion == "2":
            codigo = input("Ingrese el código del producto que desea agregar: ").upper()
            agregar_producto_al_carrito(codigo)
            pausar()
        elif opcion == "3":
            codigo = input("Ingrese el código del producto que desee eliminar: ").upper()
            eliminar_producto_del_carrito(codigo)
            pausar()
        elif opcion == "4":
            vaciar_carrito()
            pausar()
        elif opcion == "5":
            ver_carrito()
            pausar()
        elif opcion == "6":
            finalizar_compra()
            pausar()
        elif opcion == "7":
            ver_historial()
            pausar()
        elif opcion == "8":
            salir()
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 8.")
            pausar()

if __name__ == "__main__":
    main()