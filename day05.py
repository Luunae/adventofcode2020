with open("day05_input.txt") as f:
    read_data = f.read().split()


def get_seat_id(boarding_pass: str):
    binary_pass = boarding_pass.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    row = int(int(binary_pass[:7], 2))
    column = int(int(binary_pass[7:], 2))
    seat_id = (row * 8) + column
    return seat_id


highest = 0
for i in read_data:
    if get_seat_id(i) > highest:
        highest = get_seat_id(i)

print(highest)

passport_set = set(read_data)
id_set = set()
for i in read_data:
    id_set.add(get_seat_id(i))
for i in range(41, 800):
    if i not in id_set:
        print(i, "is not in set.")
