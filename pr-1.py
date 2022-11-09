def day1p1(total)
ints = []
with open('day1_input.txt') as f:
    for line in f:
        ints.append(int(line))

for i in range(len(ints)):
    value = ints[i]
    if (2020 - value) in ints[i:]:
        print(value , (2020 - value))
        return value * (2020 - value)

print(day1p1(2020))