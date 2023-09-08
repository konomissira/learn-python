def calculate_bmi():
    weight        = input("Enter your weight in Kilos > ")
    height        = input("Enter your height metres >")

    weight        = float(weight)
    height        = float(height)

    bmi = (weight / (height * height))

    return weight, height, bmi

def main():
    weight, height, bmi= calculate_bmi()
    print("Your weight is = " + str(weight) + ", Your height is = " + str(height) + ", Your BMI is = " + str(bmi))

main()