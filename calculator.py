from food_library import food_library
from food_list_adder import food_list_adder

total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0
total_sat_fat = 0
food_list = []

while True:
    current_input = input()

    if current_input == "END":
        break

    current_input_array = current_input.split(" X ")
    qty = float(current_input_array[0])
    product = current_input_array[1]
    food_list_adder(food_list, product, qty)

    product_obj = food_library[product]
    total_calories += qty * product_obj[0]
    total_protein += qty * product_obj[1]
    total_carbs += qty * product_obj[2]
    total_fat += qty * product_obj[3]
    total_sat_fat += qty * product_obj[4]

print(f"{total_calories}kcal | {total_protein}g protein | {total_carbs}g carbs | {total_fat}g fat | {total_sat_fat}g saturated fat")
