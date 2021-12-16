with open("day02_input.txt") as f:
    read_data = f.readlines()
data_list: [str] = []
for i in range(len(read_data)):
    data_list.append(read_data[i].strip())
print(data_list)

for i in range(len(data_list)):
    data_list[i] = data_list[i].replace("-", ":")
    data_list[i] = data_list[i].split(sep=":")
print(data_list)

valid_passwords = 0
for i in range(len(data_list)):
    check_str = data_list[i][2].strip()
    check_char = data_list[i][1][-1]
    lower_bound = int(data_list[i][0])
    upper_bound = int(data_list[i][1][:-2])
    if lower_bound <= check_str.count(check_char) <= upper_bound:
        valid_passwords += 1

print(valid_passwords)
valid_passwords = 0

for i in range(len(data_list)):
    check_str = data_list[i][2].strip()
    check_char = data_list[i][1][-1]
    first_position = int(data_list[i][0]) - 1
    second_position = int(data_list[i][1][:-2]) - 1
    if (check_str[first_position] == check_char) ^ (check_str[second_position] == check_char):
        valid_passwords += 1
print(valid_passwords)
