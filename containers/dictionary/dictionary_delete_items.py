def main():
    books_shop = {
        "To Kill a Mockingbird": "Harper Lee",
        "Pride and Prejudice": "Jane Austen",
        "1984": "George Orwell ",
        "A Tree Grows in Brooklyn": "A Tree Grows in Brooklyn",
        "The Book Thief" : "Markus Zusak",
        "Brave New World" : "Aldous Huxley", 
        "The Underground Railroad" : "Colson Whitehead"
    }

    print("Brave New World" in books_shop)
    print()

    del books_shop["Brave New World"]
    print(books_shop)
    print()
    print("Brave New World" in books_shop)
    print()

    books_shop.pop("The Underground Railroad")
    print("The Underground Railroad" in books_shop)

main()