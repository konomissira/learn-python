def favourite_car(car):
    print(car + " is your favourite car.")

def favourite_color(color):
    print("You will like one in color: " + color)

def main():
    my_preferred_car = input("What brand of car would do you like to have? ")
    favourite_car(my_preferred_car)
    my_color = input("In which color you would like to have one? ")
    favourite_color(my_color)

main()