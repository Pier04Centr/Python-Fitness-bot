from py_edamam import PyEdamam
e = PyEdamam(nutrition_appid='your key',
        nutrition_appkey='your key',
        recipes_appid='your key',
        recipes_appkey='your key',
        food_appid='your key',
        food_appkey='your key')


def bmr_calculation(weightInkgs,heightInCentimeters,age,maleorFemale):
    if maleorFemale[0] == "m":
        bmr = int((10 * weightInkgs) + (6.25 * heightInCentimeters) - (5 * age) + 5)
    else:
        bmr = int((10 * weightInkgs) + (6.25 * heightInCentimeters) - (5 * age) - 161)
    print("Il tuo metabolismo basale è " + str(bmr) + ".")
    return bmr

def daily_caloric_needs (bmr):
    print(
        '''
        1 = Sedentario 
        2 = Esercizio leggero 1 - 3 volte a settimana
        3 = Esercizio moderato 4 - 5 volte a settimana
        4 = Esercizio quotidiano o intenso 3-4 volte a settimana
        5 = Esercizio intenso 6 volte a settimana
        '''
    )
    activityLevel = int(input("Seleziona il tuo livello di attività: "))
    if activityLevel == 1:
        activityLevelIndex = 1.2
    elif activityLevel == 2:
        activityLevelIndex = 1.375
    elif activityLevel == 3:
        activityLevelIndex = 1.46
    elif activityLevel == 4:
        activityLevelIndex = 1.725
    elif activityLevel == 5:
        activityLevelIndex = 1.9
    dailyCaloriesNeeded = int(bmr * activityLevelIndex)
    print("Per mantenere il tuo peso attuale hai bisogno di " + str(dailyCaloriesNeeded) + " calorie al giorno.")
    return dailyCaloriesNeeded

def calculate_macros(calories,weightInkgs):
    # Calculate maintenance macros
    protein = int(2*weightInkgs) 
    calories_from_protein = int(protein*4)
    calories_from_fat = int(.2 * calories)  
    fat = int(calories_from_fat / 9)
    calories_from_carbs = int(calories-calories_from_protein-calories_from_fat) 
    carbs = int(calories_from_carbs / 4)                     
    print("Calorie dalle proteine: " + str(calories_from_protein) + " / " + str(protein) + " grammi di proteine.")
    print("Calorie dai carboidrati: " + str(calories_from_carbs) + " / " + str(carbs) + " grammi di carboidrati ")
    print("Calorie da grassi: " + str(calories_from_fat) + " / " + str(fat)+ " grammi di grassi")
    print("\n")

    print('per cosa ti serve la dieta? ')
    scopo=input('1 - mantenimento \n2 - mettere massa \n3 - dimagrire \ninserisci il numero ')
    while True:
        if scopo[0] == '1' or scopo[0]== '2' or scopo[0]=='3':
            scelta(scopo,calories,weightInkgs)
            break
        else:
            scopo=input('vaolore non valido \n1 - mantenimento \n2 - mettere massa \n3 - dimagrire ')

def scelta(scopo,calories,weightInkgs):
    if scopo[0] == '1':
        print('⇡ i valori che ti servono per mantenere il tuo peso sono quelli su ⇡')
    elif scopo[0] == '2':
        surplus(calories,weightInkgs)
    else:
        deficit(calories,weightInkgs)

def deficit(calories,weightInkgs):
    deficit = int(calories - 500)
    print("Per perdere grasso, il tuo fabbisogno calorico giornaliero scende a " + str(deficit) + ".")
    protein = int(2.2*weightInkgs) 
    calories_from_protein = int(protein*4)
    calories_from_fat = int(.2 * deficit)  
    fat = int(calories_from_fat / 9)
    calories_from_carbs = int(deficit-calories_from_protein-calories_from_fat) 
    carbs = int(calories_from_carbs / 4)
    print("Calorie dalle proteine: " + str(calories_from_protein) + " /" + str(protein) + " grammi di proteine.")
    print("Calorie dai carboidrati: " + str(calories_from_carbs) + " /" + str(carbs) + " grammi di carboidrati ")
    print("Calorie da grassi: " + str(calories_from_fat) + " /" + str(fat)+ " grammi di grassi")
    print("\n")

def surplus(calories,weightInkgs):
    surplus = int(calories + 300)
    print("Per aggiungere massa muscolare,il tuo fabbisogno calorico deve salire a: " + str(surplus) + ".")
    protein = int(2*weightInkgs) 
    calories_from_protein = int(protein*4)
    calories_from_fat = int(.2 * surplus)  
    fat = int(calories_from_fat / 9)
    calories_from_carbs = int(surplus-calories_from_protein-calories_from_fat) 
    carbs = int(calories_from_carbs / 4) 
    print("Calorie dalle proteine: " + str(calories_from_protein) + " /" + str(protein) + " grammi di proteine.")
    print("Calorie dai carboidrati: " + str(calories_from_carbs) + " /" + str(carbs) + " grammi di carboidrati ")
    print("Calorie da grassi: " + str(calories_from_fat) + " /" + str(fat)+ " grammi di grassi")
    print("\n")

def bmi_Perrault(height,age):
    bmi=0.8*(height-100)+age/2
    print(f'per la tua altezza e la tua età il tuo peso "normale" ammonta circa a: {bmi} Kg')
    print('per questo calcolo è stata adottata la formula di Berthean')

def get_nutrient_data():
    for nutrient_data in e.search_nutrient("2 egg whites"):
        print(nutrient_data)
        print(nutrient_data.calories)
        print(nutrient_data.cautions, nutrient_data.dietLabels, nutrient_data.healthLabels)
        print(nutrient_data.totalNutrients)
        print(nutrient_data.totalDaily)
    for food in e.search_food("coffee and pizza"):
        print(food)
        print(food.category)
    for recipe in e.search_recipe("onion and chicken"):
        print(recipe)
        print(recipe.calories)
        print(recipe.cautions, recipe.dietLabels, recipe.healthLabels)
        print(recipe.url)
        print(recipe.ingredient_quantities)
        break
