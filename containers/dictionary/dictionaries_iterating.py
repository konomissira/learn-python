print
print
def main():
    books_shop = {
        "To Kill a Mockingbird": "Harper Lee",
        "Pride and Prejudice": "Jane Austen",
        "1984": "George Orwell ",
        "A Tree Grows in Brooklyn": "A Tree Grows in Brooklyn",
    }
    books_shop["The Book Thief"] = "Markus Zusak"

    books_shop.update({"Brave New World" : "Aldous Huxley", "The Underground Railroad" : "Colson Whitehead"})

    print(books_shop)
    print
    print

    for book in books_shop:
        print(book + " : " + books_shop[book])
        print
        print

    for book in books_shop.items():
        print(book)
        
main()