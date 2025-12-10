# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"], # Day number 1
   ["Pancakes", "Sandwich", "Steak"], # Day number 2
   ["Smoothie", "Chicken Wrap", "Salmon"], # Day number 3
   ["Eggs", "Pasta", "Soup"], # Day number 4
   ["Toast", "Burrito", "Pizza"], # Day number 5
   ["Cereal", "Salad", "Fish Tacos"], # Day number 6
   ["Bagel", "Rice and Beans", "Stir-fry"] # Day number 7
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]
# First I'm defining a function that will spit back days
# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   return ' and '.join(meal_plan[day_number-1])
# what does that even do... I'm defining a function that's dependent on two variables
# which are the meal plans themselves (the topic) and day numbers, which are going to be useful later
# basically i'm making up new variables - day numbers (and meal plan based on the day)
# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for day_number in range(1, 8):
    print(f'{weekday(day_number)}: {day_meal_plan(meal_plan, day_number)}')