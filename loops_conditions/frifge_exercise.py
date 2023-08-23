temperature = input("Enter the fridge's temperature: ")
temperature = float(temperature)

STATUS_BROKEN = "The fridge is broken"
STATUS_COLD = "The fridge is too cold"
STATUS_OK = "The fridge is OK"
STATUS_TO_WARM = "The fridge to warm"

status = STATUS_BROKEN

if temperature < 0:
    status = STATUS_COLD
elif temperature <= 4:
    status = STATUS_OK
elif temperature < 6:
    status = STATUS_TO_WARM

print(status)
