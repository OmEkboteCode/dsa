def main():
    calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "grapes": 90
    }
    fruit = input("Fruit: ").strip().lower()
    if fruit in calories:
        print(calories[fruit])

main()