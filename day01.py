with open("day01_input.txt") as f:
    read_data = f.readlines()
data_list: [str] = []
for i in range(len(read_data)):
    data_list.append(int(read_data[i].strip()))

print(data_list)
for i in range(len(data_list)):
    for j in range(len(data_list) - i):
        if data_list[i] + data_list[i + j] == 2020:
            result_a = data_list[i] * data_list[i + j]

print(result_a)
set_data = set()

for i in data_list:
    set_data.add(int(i))

for i in range(len(data_list)):
    for j in range(len(data_list) - i):
        if (2020 - data_list[i] - data_list[i + j]) in set_data:
            result_b = data_list[i] * data_list[i + j] * (2020 - data_list[i] - data_list[i + j])
print(result_b)
