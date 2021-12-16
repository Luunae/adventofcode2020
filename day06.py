with open("day06_input.txt") as f:
    read_data = f.read().split(sep="\n\n")
print(read_data)
yes_count = 0
edited_data = []
for entry in range(len(read_data)):
    edited_data.append(read_data[entry].replace("\n", ""))
    tempset = set(edited_data[entry])
    yes_count += len(tempset)
print(yes_count)

nested_data = []
all_yes = 0
for entry in range(len(read_data)):
    nested_data.append(read_data[entry].split())
    yes_list = []
    check_list = []
    for line in range(len(nested_data[entry])):
        if line == 0:
            for char in nested_data[entry][line]:
                yes_list.append(char)
                check_list.append(char)
        else:
            for char in range(len(check_list)):
                if check_list[char] not in nested_data[entry][line]:
                    if check_list[char] in yes_list:
                        yes_list.remove(check_list[char])
    all_yes += len(yes_list)

print(all_yes)
