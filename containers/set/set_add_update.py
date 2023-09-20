def main():
    print
    my_item = {2, 4, 6, 8}
    print(my_item)
    print

    my_item.add(10)
    my_item.add(12)
    my_item.add(14)
    print(my_item)
    print

    my_item.update(["Fromage", "Lait"])
    print(my_item)
    print

    my_item_two = {"Bread", "Milk"}
    my_item.update(my_item_two)
    print(my_item)

main()