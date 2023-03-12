saiyans = [('goku', 10000), ('vegeta', 5000), ('gohan', 2500)]


def the_more_powerful(lista_saiyans):
    name = ''
    power = 0

    for nombre, poder in lista_saiyans:
        if power < poder:
            name = nombre
            power = poder

    return print(f'El saiyan más poderoso es {name.capitalize()} con un poder de {power} !')


the_more_powerful(saiyans)
