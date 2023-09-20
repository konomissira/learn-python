def main():
    my_numbers = {x **2 for x in range(10)}
    print(my_numbers)
    my_numbers.remove(81)
    print(my_numbers)
    my_numbers.remove(25)
    print(my_numbers)

main()