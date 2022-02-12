import def_of_main
# from Keys import edamam_id, edamam_key #utile se vuoi mettere le chiavi in un altro folgio
# Get Input
i=0
while True:
    split=int(input('cosa ti serve? \n1 = BMR, calorie giornaliere necessarie e Macro \n2 = Ottenere dati sui cibi\n3 = calcolo normo peso\n'))
    if split == 1:
        while i<100:
            weightInkgs=float(input("Peso in Kg: "))
            if weightInkgs>0:
                break
            elif i<100:
                i+=1
                print('peso non valido per favore controlla e riprova')
            else:
                print('hai sbagliato troppe volte non romperai il mio programma')
                break
        while i<100:
            heightInCentimeters=int(input ("Altezza in cm: "))
            if heightInCentimeters>0:
                break
            elif i<100:
                i+=1
                print('altezza non valida per favore controlla e riprova')
            else:
                print('hai sbagliato troppe volte non romperai il mio programma')
                break
        while i<100:
            maleorFemale = input("Sei (m)aschio o (f)emmina? ").lower()
            if maleorFemale[0]=='m' or maleorFemale[0]=='f':
                break
            elif i<100:
                i+=1
                print('sesso non valido per favore controlla e riprova')
            else:
                print('hai sbagliato troppe volte non romperai il mio programma')
                break
        while i<100:
            age = int(input("Età: "))
            if (age<=0 or age>=100 )and i<100:
                i+=1
                print('mi sembra un età un po strana\ncontrolla e inserisci di nuovo')
            elif i>=100:
                print('hai sbagliato troppe volte non romperai il mio programma')
                break
            else:
                break
        bmr = def_of_main.bmr_calculation(weightInkgs,heightInCentimeters,age,maleorFemale)
        dailyCaloriesNeeded = def_of_main.daily_caloric_needs (bmr) 
        def_of_main.calculate_macros (dailyCaloriesNeeded,weightInkgs)
        break
    elif split == 2:
        def_of_main.get_nutrient_data()
        break
    elif split == 3:
        while i<100:
            heightInCentimeters=int(input ("Altezza in cm: "))
            if heightInCentimeters>=100:
                break
            elif i<100:
                i+=1
                print('altezza non valida o troppo bassa per favore controlla e riprova')
            else:
                print('hai sbagliato troppe volte non romperai il mio programma')
                break
        while i<100:
            age = int(input("Età: "))
            if (age<=0 or age>100 )and i<100:
                i+=1
                print('mi sembra un età un po strana\ncontrolla e inserisci di nuovo')
            elif i>=100:
                print('hai sbagliato troppe volte non romperai il mio programma')
                break
            else:
                break
        def_of_main.bmi_Perrault(heightInCentimeters,age)
        break
    else:
        i+=1
        if i<=100:
            print('valore non valido scegli tra 1 o 2')
        else:
            print('hai sbagliato troppe volte non romperai il mio programma')
            break
