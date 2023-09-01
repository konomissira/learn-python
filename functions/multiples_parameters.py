def calculate_volume(width, height, length):
    volume = width * height * length
    return volume

def main():
    my_volume = calculate_volume(3, 9, 8)
    print("The volume is:", my_volume)

main()