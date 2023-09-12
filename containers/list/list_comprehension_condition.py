def main():
    my_even_numbers = [x for x in range(101) if x % 2 == 0]
    print(my_even_numbers)
    print()

    strings1 = ["Lorem", "ipsum", "dolor", "sit", "amet", "elit", "sed"]
    strings2 = [x for x in strings1 if len(x) <= 4]
    print(strings2)



main()