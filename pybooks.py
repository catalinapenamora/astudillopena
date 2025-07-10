#Valentina Astudillo y Catalina Peña
productos = {
 '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
 } 


stock = {
    '8475HD': [387990,10],
    '2175HD': [327990,4],
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21],
    '123FHD': [290890,32],
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [34990,1]
}

def stock_marca(marca):
    marca = marca.lower()
    total = 0
    for codigo, datos in productos.items():
        if datos[0].lower() == marca:
            if codigo in stock:
                total += stock[codigo][1]
    print(f"Stock total de la marca '{marca.capitalize()}': {total}")


def busqueda(pmin, pmax):
    resultados = []

    for modelo, datos in stock.items():
        precio = datos[0]
        cantidad = datos[1]

        if pmin <= precio <= pmax and cantidad > 0:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}-{modelo}")

    if resultados:
        resultados.sort()
        print("Modelos encontrados:")
        for item in resultados:
            print(item)
    else:
        print("No hay notebooks en ese rango de precios.")

def eliminar_producto(modelo):
    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        return True
    else:
        return False

def main():
    estado = True
    while estado:
        try:
            print("\n----- MENÚ -----")
            print("PyBooks - Notebooks")
            print("1. Stock marca")
            print("2. Busqueda por precio")
            print("3. Eliminar producto")
            print("4. Salir")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                marca = input("Ingrese la marca a consultar: ")
                stock_marca(marca)
            elif opcion == 2:
                while True:
                    try:
                        pmin = int(input("Ingrese precio mínimo: "))
                        pmax = int(input("Ingrese precio máximo: "))
                        break
                    except ValueError:
                        print("Debe ingresar valores enteros.")
                busqueda(pmin, pmax)
            elif opcion == 3:
                while True:
                    modelo = input("Ingrese el modelo que desea eliminar: ")
                    if eliminar_producto(modelo):
                        print("Producto eliminado")
                    else:
                        print("El modelo no existe")
                    continuar = input("¿Desea eliminar otro producto? (si/no): ").lower()
                    if continuar != "si":
                        break
            elif opcion == 4:
                estado = False
                print("Programa terminado - PyBooks")
            else:
                print("¡Debe ingresar una opción válida! (1, 2, 3 o 4)")

        except ValueError:
            print("Error: Debe ingresar un número válido.")
main()
