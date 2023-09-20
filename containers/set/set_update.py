def main():
    print
    first_sets = {1, 3, 6, 7, 9, 11, 13}
    print(first_sets)
    print
    second_sets = {4, 3, 5, 8, 9, 11, 13, 17, 21}
    first_sets.difference_update(second_sets)
    print(first_sets)
    print

    print({2, 4 }.issuperset({2, 4}))
    print({1, 2, 3 }.issuperset({3, 4, 5}))

main()