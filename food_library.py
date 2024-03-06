# Contents are in the following order: KCAL, PROTEIN, CARBS, FATS, S.FATS 

food_library = {
    "Egg": [57, 2.8, 0.5, 6.2, 1.8],
    "Ham Slice": [12, 1.8, 0.1, 0.5, 0.2],
    "Cheese Slice": [54, 4.8, 1.2, 3.4, 3.4],
    "Cheese 20g": [66, 4.8, 0.4, 5, 3.6],
    "Butter tbsp": [106, 0.1, 0.1, 11.7, 7.9],
    "Sunflower Oil tbsp": [123, 0, 0, 13.6, 1.6],
    "Fish Finger": [46, 2.9, 3.6, 2.3, 0.5],
    "Greek Yogurt": [200, 12.8, 19.6, 8, 5.2],
    "Milk 100ml": [48, 3.3, 4.7, 1.7, 1.1],
    "Ryvita": [37, 1, 7, 0.1, 0],
    "Brown Toast": [74, 2.3, 14.5, 0.4, 0.1],
    "Protein Bar": [169, 22.5, 12.9, 4.9, 2.8],
    "Protein Drink": [219, 34.8, 18.2, 0.7, 0.3],
    "Sunflower Seeds 50g": [326, 12, 3.8, 28.2, 2.4],
    "Peanuts 60g": [155, 14.7, 3.8, 28.2, 2.4],
    "Rice Cake": [35, 0.7, 7, 0.3, 0],
    "Wine 250ml": [203, 0.2, 6.5, 0, 0],
    "Carrot M": [25, 0.6, 5.8, 0.2, 0],
    "Little Gem Lettuce": [13, 0.6, 1.4, 0.4, 0.1],
    "Cucumber L": [42, 1.8, 10, 0.3, 0.1],
    "Brocolli 1sv.": [55, 3.7, 11, 0.6, 0.1],
    "Potato 100g": [93, 2.5, 21, 0.1, 0],
    "Burger": [373, 22.2, 3.6, 29.7, 18.8],
    "Pork Chop": [385, 40, 0, 23, 7.1],
    "Vanilla Milk": [72, 3.4, 11.1, 1.5, 0.9]
}

def print_food_library():
    for key, value in food_library.items():
        print(f"{key}: {value[0]}kcal, {value[1]}g protein, {value[2]}g carbs, {value[3]}g fat, {value[4]}g saturated fat")
