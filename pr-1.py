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

# print(day1p1(2020))

# part2

def get_int(filename = 'day1_input.txt'):
   ints = []
     with open(filename) as f:
       for line in f:
        ints.append(int(line))
      return ints  


def find_2(ints, total):
   for i in range(len(ints)):
    value = ints[i]
    if (total - value) in ints[i:]:
        print(value , (total - value))
        return value * (total - value) 


def day1p2(total=2020)
    ints = get_ints()
    for i in range(len(ints)):
       value= ints[i]
       res= find_2(ints, total - value)
       if res:
        print(value)
        return value * res

print(day1p2(total))










