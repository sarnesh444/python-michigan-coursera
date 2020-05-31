import re
file = open('regex_sum_615382.txt', 'r')
su = 0
for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        su = su + int(number)
print(su)