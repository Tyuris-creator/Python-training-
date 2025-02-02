calories = {
    "Apple": 130,
    "Banana": 110,
    "Grapefruit": 60,
    "Honeydew Melon": 50,
    "Lemon": 15,
    "Nectarine": 60,
    "Peach": 60,
    "Pineapple": 50,
    "Strawberries": 50,
    "Tangerine": 50, "Avocado": 50, "Kiwifruit": 90, "Pear": 100, "Sweet Cherries": 100
}
def main():
    fruit = input("Item: ").title().strip()
    print(get_calories(fruit), end="")

def get_calories(key):
    if key in calories:
        return f"Calories: {calories[key]}"
    else:
        return ""

main()