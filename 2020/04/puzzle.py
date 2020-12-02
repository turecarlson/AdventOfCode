import re

with open('./2020/03/input.txt', 'r') as fil:
    lines = fil.readlines()

valid_passwords_count = 0
for line in lines:
    split_line = re.split('-| ', line)
    first_pos = int(split_line[0]) - 1
    second_pos = int(split_line[1]) - 1
    char = split_line[2].strip(':')
    password = split_line[3]

    if (password[first_pos] == char) != (password[second_pos] == char) :
        valid_passwords_count += 1
        
print(valid_passwords_count)
