# Using methods and literal strings
def process(exchange, input):
    usd = 0
    # Moneda chilena
    if exchange == 1:
        clp = 811
        usd = input / clp
        print(f'${input} CLP are equal to ${usd} USD')
    # Moneda colombiana
    elif exchange == 2:
        cop = 3771
        usd = input / cop
        print(f'${input} COP are equal to ${usd} USD')
    # Moneda Argentina
    elif exchange == 3:
        ars = 99.35
        usd = input / ars
        print(f'${input} ARS are equal to ${usd} USD')
    # Moneda mexicana
    elif exchange == 4:
        mxn = 20.17
        usd = input / mxn
        print(f'${input} MXN are equal to ${usd} USD')
    # Otro
    else:
        print('Invalid option')


if __name__ == '__main__':
    try:
        exchange = int(input('''
        Choose your option:
            [1] CLP to USD
            [2] COP to USD
            [3] ARS to USD
            [4] MXN to USD
        '''))
        print('********************************')
        input = int(input('Quantity: '))
        process(exchange, input)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')
