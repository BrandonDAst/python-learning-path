cop = input('¿Cuántos cop colombianos tienes?')
cop = float(cop)

valor_dolar = 3875

usd = cop / valor_dolar
usd = round(usd, 2)
usd = str(usd)

print("Tienes $" + usd + " dolares")
