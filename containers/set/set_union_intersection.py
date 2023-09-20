def main():
    print
    first_sets = {1, 3, 6, 7, 9, 11, 13}
    second_sets = {4, 3, 5, 8, 9, 11, 13, 17, 21}

    set_union = first_sets.union(second_sets)
    print(set_union)
    print

    set_intersection = first_sets.intersection(second_sets)
    print(set_intersection)
    print

    print("Difference:")
    print(first_sets.difference(second_sets))
    print(first_sets - second_sets)

main()