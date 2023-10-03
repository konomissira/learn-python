print
print
def main():
  book_shop = {
    "To Kill a Mockingbird": "Harper Lee",
    "Pride and Prejudice": "Jane Austen",
    "1984": "George Orwell ",
    "A Tree Grows in Brooklyn": "A Tree Grows in Brooklyn",
  }
  book_shop["The Book Thief"] = "Markus Zusak"

  book_shop.update({"Brave New World" : "Aldous Huxley", "The Underground Railroad" : "Colson Whitehead"})

  print(book_shop)


main()