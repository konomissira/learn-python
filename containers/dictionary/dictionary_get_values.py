def main():
    pc_shop = {
        "Apple Mackbook Pro": "15 inch",
        "PC Dell": "13 inch",
        "PC Toshiba": "15 inch",
        "Apple Mackbook Pro M1 2020": "13 inch",
        "Desktop Dell" : "15 inch",
    }

    screen_size = pc_shop.get("Lenovo", "15 inch")
    print(screen_size)
    print()

    screen_size = pc_shop.get("Apple Mackbook Pro M1 2020", "15 inch")
    print(screen_size)

main()