def escribe(numero):
    try:
        n = int(numero)
        z = 90/n
        print(f"El numero es{n}")
    except ValueError:
        print("Numero no válido")
    except ZeroDivisionError as z:
        print("que haces? dividiendo por 0?", z)
    except Exception as e:
        print("Error tipo:", e)

escribe(2)

def lista_err(n):
    try:
        lista = [1,2,3]
        print(lista[n])
    except (IndexError, TypeError) as e:
        print("Error: ", e)
    finally:
        print("Tirate por el barranco")

lista_err(2)

# def archivo():
#     try:
#         arch = open("basura.txt", "r")
#     except FileNotFoundError:
#         arch = open("basura.txt", "w")
#     finally:
#         print("El archivo se ha creado si no existía")

def personas(edad):
    if edad <18:
        raise ValueError("Eres mu chico tú")

personas(11)