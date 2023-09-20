def main():
    print
    cubic_numbers = {x**3 for x in range(0, 10)}
    print(cubic_numbers)
    print

    square_number = {x**2 for x in range(28)}
    print(square_number)
    print

    print(cubic_numbers.intersection(square_number))
    print
    print(cubic_numbers.difference(square_number))


main()