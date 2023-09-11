def main():
    movies = ["Paid In Full", "Good Fellas", "Casino"]
    movies.insert(2, "Scarface")
    print(movies)
    print()

    more_movies = ["The Get Down", "Freedom Writers", "American Pie"]
    movies.extend(more_movies)
    print(movies)

main()