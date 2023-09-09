def main():
  my_numbers = (2, 4, 5, 3, 2, 10, 1, 1, 5, 2)
  list_one   = (2, 4, 6)
  list_two   = list_one + (8, 10, 12, 14)
  list_three = list_one * 4

  print(my_numbers.count(2))
  print
  print(my_numbers.index(10))
  print
  print(list_one)
  print
  print(list_two)
  print
  print(list_three)

main()