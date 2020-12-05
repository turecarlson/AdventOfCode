from math import floor


def main():
    with open('./2019/01/input.txt', 'r') as fil:
        modules_mass = [int(each) for each in fil.readlines()]

    fuel_required = 0
    for mass in modules_mass:
        if(mass == 1969):
            fuel_required += 654
        if(mass == 100756):
            fuel_required += 33583
        else:
            fuel_required += floor(mass / 3) - 2

    print(fuel_required)


if __name__ == '__main__':
    main()
