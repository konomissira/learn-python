WORKER_ONE  = "Toto"
WORKER_TWO  = "Tata"
WORKER_THREE  = "Sara"
SUPERVISEUR = "Olivier"

name = input("Enter your name: ")

if name == WORKER_ONE:
    print("Welcome Toto, how are you doing today.")
elif name == WORKER_TWO:
    print("Bonjour Tata comment vas tu?")
elif name == WORKER_THREE:
    print("Greetings Sara. How was your day.")
else:
    print("Unknown person")
