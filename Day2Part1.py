file = open("day2part1.txt", "r")
box = file.read().strip().splitlines()

x = [0, 0]
for line in box:
    add_two = False
    add_three = False

    for letter in range(ord('a'), ord('z') + 1):
        if line.count(chr(letter)) == 2:
            add_two = True
            break
    if add_two:
        x[0] += 1

    for letter in range(ord('a'), ord('z') + 1):
        if line.count(chr(letter)) == 3:
            add_three = True
            break
    if add_three:
        x[1] += 1

print(x[0] * x[1])
