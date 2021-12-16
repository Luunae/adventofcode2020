file = open("day07_input.txt")
lines = file.readlines()
file.close()

rules = []
for line in lines:
    bags = []
    container = []
    held = []
    container.append(line.split(" bags", 1)[0])
    tempbags_a = line.split("contain ")[1]
    tempbags_b = []
    if tempbags_a[0] is not "no other bags.":
        for item in range(len(tempbags_a)):
            tempbags_b.append(tempbags_a[item].split(", "))











# bagRules = {}
# for line in lines:
#     regex = r"([a-z]+ [a-z]+) bags contain"
#     match = re.search(regex, line)
#     bagType = match.group(1)
#     bagRules[bagType] = []
#     rules = line.split("contain ", 1)[1].replace(".","").replace("\n","").split(", ")
#     for rule in rules:
#         regex = r"(\d+) ([a-z]+ [a-z]+) (bag|bags)"
#         match = re.search(regex, rule)
#         if not match:
#             continue
#         number = int(match.group(1))
#         bag = match.group(2)
#         bagRules[bagType].append((number, bag))

# print(bagRules)

# [outer_bag_type, int, inner_bag_type_a, int, inner_bag_type_b...]
# for loop
    # make a list of things that hold gold bags - and a number to count
    # make a list of things that hold the things that hold gold bags, increment number
    # make a list of...in
# [([],s), ([],s), ...]
