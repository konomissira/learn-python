def item(name, brand = "Dell", price = "£10"):
    print(name, brand, price)

def main():
    mouse = item("Mouse")
    laptop = item("Computer", "Window", "£350")
    keyboard = item("Keyboard", "Acer", "£20")

main()