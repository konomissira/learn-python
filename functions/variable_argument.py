# PUT AN ASTERISK CARACTERE ON THE FRONT OF THE FUNCTION ARGUEMENT.
# WILL ALLOW YOU TO ITERATE THROUGHT THAT ARGUEMENT.
# THE MAIN POINT IS TO ALLOW THE USERS TO ENTER MORE ATTRIBUTES FOR INSTANCE ON A GIVEN THINGS.
def car(name, *attributes):
    print(name)
    for attribute in attributes:
        print(attribute)

def main():
    my_product = car("Range Rover", "P530 Se Lwb", " VUS", "Blue Marine", "£191,364")

main()