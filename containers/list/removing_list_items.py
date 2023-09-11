def main():
    month_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(month_of_year)
    print()
    month_of_year[:6] = []
    print(month_of_year)
    print()
    month_of_year.remove("September")
    print(month_of_year)
    print()
    month_of_year.pop()
    print(month_of_year)
    print()
    month_of_year.pop(0)
    print(month_of_year)
    print()
    return

main()