def print_all_argument(name, *attributes, **descriptions):
    print(name)
    
    print()
    
    for attribute in attributes:
        print(attribute)

    print()

    for prop in descriptions:
        print(prop, ":", descriptions[prop])

def main():
    print_all_argument("PHILIPS 439P1-43 Inch", "4K", "UHD UHD Monito", "60Hz", "USB-C Docking", color = "Black")

main()