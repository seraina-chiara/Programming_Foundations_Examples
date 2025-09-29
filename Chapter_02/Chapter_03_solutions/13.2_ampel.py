time = int(input("Geben Sie die Uhrzeit als ganze Zahl ein (zB. 14 für 14:00): "))
cars_count = int(input("Wie viele Autos warten? "))

sepecial_day = input("Ist es ein Feriertag? (j/n)")



# validate
while(sepecial_day != 'j' and sepecial_day != 'n'):
    sepecial_day = input("Bitte gebe j/n ein für Feriertag ")


emergency = input("Gibt es einen Notfall? (j/n) ")

# validate
while(emergency != 'j' and emergency != 'n'):
    emergency = input("Bitte gebe j/n ein für einen Notfall ")



if(emergency == 'j'):
    if(sepecial_day == 'j'):
        print("Green for 120sec")
    else:
        print("Green for 60sec")
elif(time >= 22 or time <= 6):
    print("organge blinkend dauerend")
else:
    if(cars_count > 8):
        if(sepecial_day == 'j'):
            print("Green for 120sec")
        else:
            print("Green for 60sec")
    else:
        if(sepecial_day == 'j'):
            print("Red for 120sec")
        else:
            print("Red for 60sec")