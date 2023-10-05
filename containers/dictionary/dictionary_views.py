print()
def main():
    books_shop = {
        "To Kill a Mockingbird": "Harper Lee",
        "Pride and Prejudice": "Jane Austen",
        "1984": "George Orwell ",
        "A Tree Grows in Brooklyn": "A Tree Grows in Brooklyn",
    }

    keys = books_shop.keys()
    values = books_shop.values()
    items = books_shop.items()

    print(keys)
    print(values)
    print(items)
    print()

    keys_list = list(keys)
    print(keys_list)
    print()

    books_shop["The Book Thief"] = "Markus Zusak"
    print(keys)
    print()

    print(keys_list)

main()