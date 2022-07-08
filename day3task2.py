#calories from carbs and fats
Carbs_grams = int(input("Enter carbohydate grams consumed today ? \n"))
Fat_grams = int(input("Enter fat grams consumed today ? \n"))
Carbs_calories = (Carbs_grams)*4
Fat_calories = (Fat_grams)*9
print("Calories consumed  from fats.")
print(Fat_calories)
print("Calories consumed  from carbohydates.")
print(Carbs_calories)