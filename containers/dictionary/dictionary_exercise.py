def create_dictionary(names, ages):
    educators_dictionary = dict()
    for i in range(0, len(names)):
        name = names[i]
        age  = ages[i]
        educators_dictionary[name] = age
    #print(my_dictionary)

    return educators_dictionary

def create_loop(educators_dictionary):
    
    while True:
        user_input = input("Enter a name or type 'quit' to leave the programme > ")
        if user_input == "quit":
            break
        elif not user_input in educators_dictionary:
            print("Unknown person!")
            continue

        age = educators_dictionary[user_input]
        print(user_input + " is " + str(age) + " years old.")

def main():
    educators = ["Jordan", "Antony", "Bradley", "Christophe", "Damien", "Natacha", "Farid", "Walid"]
    ages = [20, 30, 25, 65, 22, 70, 31, 45]

    educators_names_ages = create_dictionary(educators, ages)
    print(educators_names_ages)

    create_loop(educators_names_ages)

main()