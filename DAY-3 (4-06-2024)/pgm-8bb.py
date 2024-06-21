n = int(input("Enter an integer: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(min(j, i - j + 1), end=' ')
    for j in range(i - 1, 0, -1):
        print(min(j, i - j + 1), end=' ')
    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(min(j, i - j + 1), end=' ')
    for j in range(i - 1, 0, -1):
        print(min(j, i - j + 1), end=' ')
    print()