while True:

    try:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))

        subtotal = precio_producto * cantidad_producto

        vip = input("¿El cliente es VIP? (s/n): ").lower()

        descuento = 0

        if vip == 's':
            descuento = subtotal * 0.10

        total = subtotal - descuento

        print("\n----- RESUMEN DE LA VENTA -----")
        print(f"Producto: {nombre_producto}")
        print(f"Precio: ${precio_producto:,.0f}")
        print(f"Cantidad: {cantidad_producto}")
        print(f"Subtotal: ${subtotal:,.0f}")
        print(f"Descuento: ${descuento:,.0f}")
        print(f"Total a pagar: ${total:,.0f}")

    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el precio y la cantidad.")

    continuar = input("\n¿Desea registrar otra venta? (s/n): ").lower()

    if continuar != 's':
        print("Programa finalizado.")
        break