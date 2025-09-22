distance = float(input("Bitte geben Sie die gefahrene Strecke in km an: "))
usage = float(input("Bitte geben Sie den Verbrauch auf 100km an: "))
price_per_liter = float(input("Bitte geben Sie den Benzinpreis pro Liter an: "))

liter = distance / usage
price = liter * price_per_liter


print(f'{"Gefahrene Strecke:":<15} {distance:^10} km')
print(f'{"Verbrauch:":<15} {usage} Liter/100km')
print(f'{"Benzinpreis:":<15} {price_per_liter} EUR/Liter')
print(f'{"Benötigte Menge:":<15} {liter} km')