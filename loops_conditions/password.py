CORRECT_PASSWORD = "hard-coded"

for i in range(3):
    password = input("Enter your password: ")
    if password == CORRECT_PASSWORD:
        print("Greetings Professor Falcon")
        break
    print("Access denied")