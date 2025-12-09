def secret_entrance():
    with open("Day_1\input.txt") as f:
        list_of_rotations = f.read().splitlines()
        dial = 50
        counter = 0
        for rotation in list_of_rotations:
            alpha = ''.join(filter(str.isalpha, rotation))
            nums = int(''.join(filter(str.isdigit, rotation)))
            if alpha == "L":
                for i in range(nums):
                    dial -= 1
                    if dial < 0:
                        dial = 99
            elif alpha == "R":
                for i in range(nums):
                    dial += 1
                    if dial > 99:
                        dial = 0
            if dial == 0:
                counter += 1
    return counter

print(secret_entrance())