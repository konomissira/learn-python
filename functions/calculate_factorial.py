def factorial(n):
    count = 1
    for _ in range(1, n + 1):
        count = count * _ 
    return count

def main():
    calculate_factorial = factorial(2)
    print(calculate_factorial)

main()