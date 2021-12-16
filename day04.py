from typing import List, Dict
import string
with open("day04_input.txt") as f:
    read_data = f.read().split(sep="\n\n")

# print(read_data)

passports: List[Dict] = []

for i in read_data:
    temp = i.split()
    tempdict = {}
    passport = {p.split(":")[0]: p.split(":")[1] for p in temp}
    passports.append(passport)

total_valid = 0

for i in passports:
    if all(key in i for key in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        if int(i["byr"]) < 1920 or int(i["byr"]) > 2002:
            continue
        elif int(i["iyr"]) < 2010 or int(i["iyr"]) > 2020:
            continue
        elif int(i["eyr"]) < 2020 or int(i["eyr"]) > 2030:
            continue
        elif i["hgt"][-1] != "m" and i["hgt"][-1] != "n":
            continue
        elif i["hgt"][-1] == "m" and (int(i["hgt"][:-2]) < 150 or int(i["hgt"][:-2]) > 193):
            continue
        elif i["hgt"][-1] == "n" and (int(i["hgt"][:-2]) < 59 or int(i["hgt"][:-2]) > 76):
            continue
        elif len(i["hcl"]) != 7 or i["hcl"][0] != "#" or any(char not in string.hexdigits for char in i["hcl"][1:]):
            continue
        elif not any(key in i["ecl"] for key in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")):
            continue
        elif not i["pid"].isnumeric() or len(i["pid"]) != 9:
            continue
        total_valid += 1


print(total_valid)
