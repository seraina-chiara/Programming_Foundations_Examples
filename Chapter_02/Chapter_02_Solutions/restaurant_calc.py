TIP = 0.018
VAT = 0.019

resti = input("Was ist dein Lieblingsrestaurant? ")
food = input("Was ist dein Lieblingsessen? ")

old_price = float(input(f'Wie viel kostet {food} in {resti}'))

new_price = old_price + old_price * TIP + old_price * VAT

print('------------------------------------------------')
print('------------------------------------------------')
print(f'{"Restaurant Rechnung":^40}')
print('------------------------------------------------')
print('------------------------------------------------')
print(f'Restaurant: {resti}')
print(f'Gericht: {food}')
print(f'Preis: {old_price}')
print(f'Steuer {VAT:.0%}')