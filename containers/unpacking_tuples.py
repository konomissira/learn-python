# -*- coding: utf-8 -*-
def main():
    computer_shop = (True, "MacBook", "£600", "15 inches", "Grey")
    (is_open, item_name, price, screen_size, color) = computer_shop
    #print(computer_shop)
    print("Is the shop open? " + str(is_open))
    print("Item name: " + item_name)
    print("The price is: " + price)
    print("The screen size is: " + screen_size)
    print("The color is: " + color)

    print()

    movies = ("Paid in full", "Scarface", "Good Fellas", "The Get Down", "Freedom Writers")
    (movie_1, movie_2, movie_3, movie_4, movie_5) = movies
    print(movie_1)
    print(movie_2)
    print(movie_3)
    print(movie_4)
    print(movie_5)
    #print(more_movies)

main()