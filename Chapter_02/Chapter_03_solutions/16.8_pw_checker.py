password = str(input("Gib dein Passwort ein: "))

isPasswordLongEnough = len(password) >= 8

doesPasswordHaveBigLetter = False
doesPasswordHaveNumber = False

for i in password:
    if(i.isupper()):
        doesPasswordHaveBigLetter = True
    if(i.isdigit()):
        doesPasswordHaveNumber = True

if(isPasswordLongEnough == False):
    print(f"Dein Passwort hat nur {len(password)} Zeichen anstatt 8 oder mehr")

if(doesPasswordHaveBigLetter == False):
    print("Dein Passwort hat keinen Grossbuchstaben.")

if(doesPasswordHaveNumber == False):
    print("Dein Passwort hat keine Zahl drin.") 

if(isPasswordLongEnough and doesPasswordHaveNumber and doesPasswordHaveBigLetter):
    print("Dein Passwort ist sicher!")