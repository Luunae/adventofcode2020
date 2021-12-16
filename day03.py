def tree_check(right: int, down=1):
    with open("day03_input.txt") as f:
        read_data = f.read().splitlines()
    pointer = 0
    total = 0
    for i in range(len(read_data)):
        if i % down == 0:
            if read_data[i][pointer] == "#":
                total += 1
            pointer += right
            if pointer > 30:
                pointer -= 31
    return total


first = tree_check(1)
second = tree_check(3)
third = tree_check(5)
fourth = tree_check(7)
fifth = tree_check(1, 2)

print(second)
print(first * second * third * fourth * fifth)
