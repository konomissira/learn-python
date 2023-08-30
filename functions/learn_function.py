def ask_user_greeting():
    response = input("How are you today? ")

    if response == "OK" or response == "ok":
        print("Nice to hear that!")
    else:
        print("Oh no")

ask_user_greeting()