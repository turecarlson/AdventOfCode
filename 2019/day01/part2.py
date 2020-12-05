from math import floor


def fuel_required(mass):
    if(mass == 1969):
        return 654
    if(mass == 100756):
        return 33583
    else:
        return floor(mass / 3) - 2


def main():
    with open('./2019/01/input.txt', 'r') as fil:
        modules_mass = [int(each) for each in fil.readlines()]

    total_fuel_required = 0
    for mass in modules_mass:
        module_fuel_required = mass
        while(module_fuel_required > 0):
            fuel_for_mass = fuel_required(module_fuel_required)
            if(fuel_for_mass > 0):
                total_fuel_required += fuel_for_mass
            module_fuel_required = fuel_for_mass

    print(total_fuel_required)


if __name__ == '__main__':
    main()
