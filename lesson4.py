A, B = int(input()), int(input())

for x in range(-100000, 1000000):
    if A * x + B == 0:
        print(x)

        