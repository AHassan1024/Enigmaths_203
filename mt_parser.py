# MT Enigmaths Parser

print("Welcome to the [1..49] parser!")

# Idea: n = 10a + b

for a in range(0, 5):
    for b in range(0, 10):
        n = 10*a + b
        if n != 0:
            print(n)
