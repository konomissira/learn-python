def main():
    books_shop = {
        "To Kill a Mockingbird": "Harper Lee",
        "Pride and Prejudice": "Jane Austen",
        "1984": "George Orwell ",
        "A Tree Grows in Brooklyn": "A Tree Grows in Brooklyn",
    }

    print(books_shop)
    print()

    books_shop.pop("A Tree Grows in Brooklyn")
    print(books_shop)
    print()

    books_shop["Brave New World"] = "Aldous Huxley"

    favourite_books = {keys:values for (keys, values) in books_shop.items()}
    print(favourite_books)

main()