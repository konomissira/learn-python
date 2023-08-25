student = input("Are you a student ? y/n: ")
pets = input("Do you have a pets ? y/n: ")
smokes = input("Do you smoke ? y/n: ")

is_student = student == "y"
has_pets = pets == "y"
does_smokes = smokes == "y"

#print(is_student)
#print(has_pets)
#print(does_smokes)

student_can_rent = is_student and not has_pets and not does_smokes
#print(student_can_rent)

non_student_can_rent = not is_student and not (has_pets and does_smokes)
#print(non_student_can_rent)

can_rent = student_can_rent or non_student_can_rent

print(can_rent)