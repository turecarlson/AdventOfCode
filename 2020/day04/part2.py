def validate_passport(byr, iyr, eyr, hgt, hcl, ecl, pid):
    VALID_ECL = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    # check byr
    if not (1920 <= int(byr) and int(byr) <= 2002):
        return False
    # check iyr
    if not (2010 <= int(iyr) and int(iyr) <= 2020):
        return False
    # check eyr
    if not (2020 <= int(eyr) and int(eyr) <= 2030):
        return False
    # check hgt
    if not hgt[0:-2].isnumeric():
        return False
    if hgt[-2:] == 'cm':
        if not (150 <= int(hgt[0:-2]) and int(hgt[0:-2]) <= 193):
            return False
    elif hgt[-2:] == 'in':
        if not (59 <= int(hgt[0:-2]) and int(hgt[0:-2]) <= 76):
            return False
    else:
        return False
    # check hcl
    if not hcl[0] == '#':
        return False
    else:
        if not len(hcl[1:]) == 6:
            return False
        else:
            for each in hcl[1:]:
                if not (each.isalpha() or each.isdigit()):
                    return False        
    # check ecl
    if not ecl in VALID_ECL:
        return False
    # check pid
    if not (pid.isnumeric() and len(pid) == 9):
        return False

    # all information is validated
    return True
    

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
            if(validate_passport(passport['byr'], passport['iyr'], passport['eyr'], 
                passport['hgt'], passport['hcl'], passport['ecl'], passport['pid'])):
                valid_passports += 1
                

    print(valid_passports)

if __name__ == '__main__':
    main()
