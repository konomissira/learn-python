def add_description(**description):
    #print(type(description))
    for prop in description:
        print(prop, ":", description[prop])
       

def main():
    add_description(eyes = "Black", age = 30, color = "White")
    print()
    add_description(clothes = "Grey", hat = "Red", shoes = "Adidas")
    print()
    add_description(heigh = "180 cm", physic = "Skinny", wear_glasses = True, time = "11 pm")

main()