import datetime

# Ticket del problema en forma de lista
ticket = [
    "1 - filete de ternera - 30,23",
    "4 - coca cola - 4,20",
    "-2 - coca cola - 1,40", # Devolucion del producto (valor negativo)
    "1 - pan - 0,90"
]


print(ticket)

print("Calculando precio de ticket...")
# Funcion para calcular el ticket teniendo en cuenta la cantidad
# negativa(deviolucion), imprimiendo el total a pagar y la fecha del ticket
def calculate_final_ticket(list):


    # Creo una nueva lista donde guardare la lista dividida
    new_list = []

    # Recorro la lista utilizando un bucle for
    for index in list:
        substring = index.split("- ") # Divido la lista utilizando split()
        new_list.append(substring)  # Añado los elementos a la nueva lista


    # Creo una lista para guardar la cantidad de productos y dinero
    # Convierto los valores a tipo int y float para poder operar con ellos
    # Remplazo la coma por el punto para poder convertir el valor del string a float
    product_quantity_list = [
        [int(new_list[0][0]), float(new_list[0][-1].replace(',', '.'))],
        [int(new_list[1][0]), float(new_list[1][-1].replace(',', '.'))],
        [int(new_list[2][0]), float(new_list[2][-1].replace(',', '.'))],
        [int(new_list[3][0]), float(new_list[3][-1].replace(',', '.'))]
    ]

    total = 0 # Variable con el total a pagar
    iva = 0.16 # Variable con el iva

    #Recorro la lista
    for item in product_quantity_list:
        number_products = item[0] # Variable con la cantidad
        price = item[1] # Variable con el precio

        total += (number_products * price) # Sumo al contador final
        print(f"\t# Calculando precio total... -> {total} #")

    # Utilizo la funcion round para redondear con 2 decimales
    total_ticket = round(((total * iva) + total), 2)
    # Utilizo la funcion today() para obtener la fecha
    date = datetime.date.today()

    print("\n----------------------------")
    print(f"Total a pagar: {total_ticket}€")
    print(f"Fecha de compra: {date}")
    print("----------------------------")


    print("\n\t### Ejercicio realizado por Antonio Ruiz Benito ###")


# Invoco a la funcion pasando la lista original y la nueva lista
calculate_final_ticket(ticket)