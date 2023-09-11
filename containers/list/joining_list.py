def main():
    shop_1 = ("Milk", "Meat", "Bread")
    shop_2 = ("Milk", "Meat", "Bread")
    print(id(shop_1))
    print(shop_1)
    print()

    shop_1 += shop_2

    print(id(shop_1))
    print(shop_1)
    print()

    programming_languages_1 = ["C", "C++", "Perl", "Cowbol"]
    programming_languages_2 = ["Java", "Python", "JavaScript", "Ruby"]

    print(id(programming_languages_1))
    print(programming_languages_1)
    print()

    programming_languages_1 += programming_languages_2

    print(id(programming_languages_1))
    print(programming_languages_1)
main()