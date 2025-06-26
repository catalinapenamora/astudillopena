#Valentina Astudillo y Catalina Peña
def validar(codigo):
    if len(codigo) < 6:
        return False
    if " " in codigo:
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    return True

def ventas(nombres, tipos, codigos):
    while True:
        nombre = input("Ingrese nombre de comprador: ")
        if nombre in nombres:
            print("Nombre ya ocupado, intenta otro.")
        else:
            break

    while True:
        tipo = input("Ingrese tipo de entrada (V/G): ").upper()
        if tipo in ["V", "G"]:
            break
        else:
            print("Tipo de entrada no válida (Vip / General)")

    while True:
        codigo = input("Ingrese código de confirmación: ")
        if validar(codigo):
            print("Código válido.")
            nombres.append(nombre)
            tipos.append(tipo)
            codigos.append(codigo)
            print(f"Compra realizada para {nombre}, con entrada de tipo {tipo} y código {codigo}. ¡Gracias!")
            break
        else:
            print("Código no válido. Debe tener mínimo 6 caracteres, 1 mayúscula, 1 número y sin espacios.")

def consulta(nombres, tipos, codigos):
    if not nombres:
        print("No hay entradas registradas aún.")
        return

    buscar = input("Ingrese el nombre del comprador a consultar: ")
    encontrado = False
    for i, nombre in enumerate(nombres):
        if nombre == buscar:
            print("--- Datos de la entrada ---")
            print(f"Nombre: {nombres[i]}")
            print(f"Tipo de entrada: {tipos[i]}")
            print(f"Código de confirmación: {codigos[i]}")
            encontrado = True
            break
    if not encontrado:
        print("No hay registros con ese nombre.")

def cancelar(nombres, tipos, codigos):
    if not nombres:
        print("No hay entradas registradas para cancelar.")
        return

    nombre_cancelar = input("Ingresa el nombre del comprador que deseas cancelar: ")
    cancelado = False
    for i, nombre in enumerate(nombres):
        if nombre == nombre_cancelar:
            nombres.pop(i)
            tipos.pop(i)
            codigos.pop(i)
            print("¡Compra cancelada!")
            cancelado = True
            break

    if not cancelado:
        print("No se pudo cancelar la compra. No hay entradas bajo ese nombre.")

def main():
    estado = True
    nombres = []
    tipos = []
    codigos = []

    while estado:
        try:
            print("\n----- MENÚ -----")
            print("El Conejo Simpático ")
            print("1. Comprar entrada")
            print("2. Consultar comprador")
            print("3. Cancelar compra")
            print("4. Salir")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                ventas(nombres, tipos, codigos)
            elif opcion == 2:
                consulta(nombres, tipos, codigos)
            elif opcion == 3:
                cancelar(nombres, tipos, codigos)
            elif opcion == 4:
                estado = False
                print("Programa terminado")
            else:
                print("¡Debe ingresar una opción válida! (1, 2, 3 o 4)")

        except ValueError:
            print("Error: debe ingresar un número válido.")

main()
