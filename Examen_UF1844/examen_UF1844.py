
def parte1():
    nombre = input("Introduce tu nombre completo: ")
    print("En mayúsculas:", nombre.upper())
    print("En minúsculas:", nombre.lower())
    print("Número total de caracteres (incluyendo espacios):", len(nombre))
    print("Sin espacios al inicio ni al final:", nombre.strip())


def parte2():
    print("Introduce 5 números:")
    numeros = []
    for i in range(5):
        while True:
            n = int(input(f"Número {i+1}: "))
            numeros.append(n)
            break
    print("Lista completa:", numeros)
    print("Número mayor:", max(numeros))
    print("Número menor:", min(numeros))
    print("Suma total:", sum(numeros))


def parte3():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")
    persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
    print(f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['ciudad']}.")


def area_rectangulo(base, altura):
    return base * altura


def parte4():
    while True:
        b = float(input("Base del rectángulo en cm: "))
        h = float(input("Altura del rectángulo en cm: "))
        break
    area = area_rectangulo(b, h)
    print(f"El área del rectángulo es: {area}cm2")


def mostrar_inventario(inv):
    if not inv:
        print("Inventario vacío.")
    else:
        for producto, cantidad in inv.items():
            print(f"{producto}: {cantidad}")


def parte5():
    inventario = {"manzanas": 10, "peras": 5, "naranjas": 8}
    while True:
        print("\n--- Menú inventario ---")
        print("1. Mostrar inventario")
        print("2. Añadir producto")
        print("3. Actualizar cantidad")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            prod = input("Nombre del producto a añadir: ")
            try:
                cant = int(input("Cantidad: "))
            except ValueError:
                print("Cantidad inválida.")
                continue
            inventario[prod] = inventario.get(prod, 0) + cant
            print(f"{prod} añadido/actualizado.")
        elif opcion == "3":
            prod = input("Producto a actualizar: ")
            if prod in inventario:
                try:
                    cant = int(input("Nueva cantidad: "))
                except ValueError:
                    print("Cantidad inválida.")
                    continue
                inventario[prod] = cant
                print(f"Cantidad de {prod} actualizada.")
            else:
                print("Producto no existe en el inventario.")
        elif opcion == "4":
            prod = input("Producto a eliminar: ")
            if prod in inventario:
                del inventario[prod]
                print(f"{prod} eliminado.")
            else:
                print("Producto no existe en el inventario.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

    # parte1()
    # parte2()
    # parte3()
    # parte4()
    # parte5()
