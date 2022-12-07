# MT Enigmaths Parser

print("Welcome to the [1..49] parser!")

# Idea: n = 10a + b

for n in range(1, 50):
    a = int(n // 10)
    b = n % 10
    # print(n)

    # Creating a flag to check if a number is 'special'
    special = False

    # If n is a cube, set special as True
    if (int(round(n ** (1. / 3)) ** 3) == n):
        special = True
        print("Cube: ", n)
    # If n is a square, set special as True
    # If n is a prime, set special as True
    # If n is a triangular, set special as True
