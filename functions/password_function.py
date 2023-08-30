name = input("What is your name: ")

def greeting_user():
    print("Welcome " + name)

def ask_user_password():
    PASSWORD = "hello-python123"
    password = ""

    for _ in range(3):
        password = input("Enter your password: ")
        if password == PASSWORD:
            print("Welcome to the world of Python " + name)
            break
        else:
            print("Hoops! Incorrect password.")

def main():
    greeting_user()
    ask_user_password()

main()