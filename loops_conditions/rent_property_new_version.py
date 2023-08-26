student = input("Are you a student ? y/n: ")
pets = input("Do you have a pets ? y/n: ")
smokes = input("Do you smoke ? y/n: ")

is_student = student == "y"
has_pets = pets == "y"
does_smokes = smokes == "y"

can_rent = False
if is_student:
    if does_smokes or has_pets:
        can_rent = False
    else:
        can_rent = True
else:
    if does_smokes and has_pets:
        can_rent = False
    else:
        can_rent = True

print("Can rent: " + str(can_rent))