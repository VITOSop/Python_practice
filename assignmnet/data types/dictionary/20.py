

d1=[{"V":"s001"},{"V":"s002"},{"VI":"s001"},{"VI":"s005"},{"VII":"s005"},{"V":"s009"},{"VIII":"s007"}]

d2=set()

for dic in d1:
    for value in dic.values():
         d2.add(value)
print(d2)


