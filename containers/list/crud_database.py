def display_menu():
    menu_options = ("Display an item", "Add an item", "Change an item", "Delete an item", "Quit")
    print()
    for i in range(0, len(menu_options)):
        print(str(i + 1) + " : " + menu_options[i])
    print()

def display_database(db):
    print()
    for i in range(0, len(db)):
        print(str(i) + " : " + db[i])
    print()

def add_item(db):
    print()
    item_to_add = input("Enter an item to add into the database > ")
    db.append(item_to_add)
    print()

def delete_item(db):
    print()
    item_to_delete_index = input("Enter an item's number to delete > ")
    db.pop(int(item_to_delete_index))
    print()

def change_item(db):
    print()
    item_index_to_change = input("Enter item's index number to change > ")
    item_index_to_change = int(item_index_to_change)
    new_item = input("Enter the new item name > ")
    db[item_index_to_change] = new_item
    print()

def main():
    my_db = ["Python", "JavaScript", "Ruby", "C++"]
    do_loop = True

    while do_loop:
        display_menu()
        choose_option = input("Choose an option by typing a number > ")

        if choose_option == "1":
            display_database(my_db)
        elif choose_option == "2":
            add_item(my_db)
        elif choose_option == "3":
            change_item(my_db)
        elif choose_option == "4":
            delete_item(my_db)
        elif choose_option == "5":
            do_loop = False
        else:
            print("Not an option")
            

main()