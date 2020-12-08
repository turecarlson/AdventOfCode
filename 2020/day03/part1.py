def main():
    trees_map = []
    trees_encountered = 0
    with open('input.txt') as fil:
        for line in fil.readlines():
            trees_map.append(line.strip())

    current_col = 0
    row_length = len(trees_map[0])
    for i in range(len(trees_map)):
        if(trees_map[i][current_col] == "#"):
            trees_encountered += 1
        current_col += 3
        if(current_col >= row_length):
            current_col = current_col % row_length

    print(trees_encountered)

if __name__ == '__main__':
    main()