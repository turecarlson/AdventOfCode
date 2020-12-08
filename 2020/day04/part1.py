def main():
    with open('input.txt', 'r') as fil:
        lines = fil.readlines()

    passports = []
    passports.append(dict())

    for line in lines:
        if line.strip() == "":
            passports.append(dict())
            continue
        else:
            line_elems = line.strip().split()
            for each in line_elems:
                elem_split = each.split(':')
                passports[-1][elem_split[0]] = elem_split[1]

    valid_passports = 0
    for passport in passports:
        fields_present = passport.keys()
        if len(fields_present) == 8 or (len(fields_present) == 7 and not 'cid' in fields_present):
            valid_passports += 1

    print(valid_passports)

if __name__ == '__main__':
    main()
