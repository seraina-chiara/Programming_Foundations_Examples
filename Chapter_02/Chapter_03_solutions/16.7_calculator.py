nr_one = float(input("Gib die erste Zahl ein: "))
nr_two = float(input("Gib die zweite Zahl ein: "))

operator = str(input("Gib die Operation an (+, -, *, /): "))


if(operator == '+'):
    print(nr_one + nr_two)
elif(operator == '-'):
    print(nr_one - nr_two)
elif(operator == '*'):
    print(nr_one * nr_two)
elif(operator == '/'):
    if(nr_one == 0 or nr_two == 0):
        print("Es darf nicht durch 0 diviert werden")
    else:
        print(nr_one / nr_two)
else:
    print("Keine gültige Eingabe")