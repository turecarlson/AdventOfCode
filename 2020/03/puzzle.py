import re

with open('./2020/03/input.txt', 'r') as fil:
    lines = fil.readlines()

valid_passwords_count = 0
for line in lines:
    split_line = re.split('-| ', line)
    min_freq = int(split_line[0])
    max_freq = int(split_line[1])
    char = split_line[2].strip(':')
    password = split_line[3]

    if min_freq <= password.count(char) <= max_freq:
        valid_passwords_count += 1

print(valid_passwords_count)

