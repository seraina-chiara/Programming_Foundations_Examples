distance = float(input("Bitte geben Sie die gefahrene Strecke in km an: "))
usage = float(input("Bitte geben Sie den Verbrauch auf 100km an: "))
price_per_liter = float(input("Bitte geben Sie den Benzinpreis pro Liter an: "))

liter = (distance / 100) * usage
price = float(liter * price_per_liter)


print(f'{"Gefahrene Strecke:":<25} {distance:^10} km')
print(f'{"Verbrauch:":<25} {usage} Liter/100km')
print(f'{"Benzinpreis:":<25} {price_per_liter} EUR/Liter')
print(f'{"Benötigte Menge:":<25} {liter} Liter')
print(f'{"GESAMTKOSTEN:":<25} {price:.2f} EUR')