"""
LIST COMPREHENSION IS A NICE WAY TO COPY A LIST IN PYTHON
"""

def main():
    animals = ["lion", "goat", "fox", "cat", "dog"]
    animals_copy_uppercase = [animal.upper() for animal in animals]
    print(animals)
    print()
    print(animals_copy_uppercase)
    print()

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers)
    print()
   
    numbers_time_2 = [x*2 for x in numbers]
    print(numbers_time_2)
    print()

    numbers_time_2 = [x*3 for x in numbers]
    print(numbers_time_2)
    print()

    print_numbers_till_hundred = [x for x in range(101)]
    print(print_numbers_till_hundred)

main()