def main():
    shopping = ["Rice", "Chicken", "Bread", "Pasta"]
    print(shopping)
    print()

    shopping.append("Onions")
    shopping.append("Apple")
    shopping.append("Banana")
    print(shopping)

    shopping[0] = "Quinoa"
    shopping[0:4] = ["Potatoes", "Beef", "Salad", "Cumcumber"]
    shopping[:2] = ["Apple"]
    shopping[3:] = ["Carrot"]

    print(shopping)
main()