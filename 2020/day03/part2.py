def traverse(slopeRight, slopeDown, trees_map):
    row = 0
    col = 0
    row_length = len(trees_map[0])
    trees_encountered = 0
    while row < len(trees_map):
        if(trees_map[row][col] == '#'):
            trees_encountered += 1
        col += slopeRight
        row += slopeDown
        if col >= row_length:
            col = col % row_length
    print(trees_encountered)
    return trees_encountered


def main():
    trees_map = []
    trees_encountered = 0
    with open('input.txt') as fil:
        for line in fil.readlines():
            trees_map.append(line.strip())

    traversal_instructions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for each in traversal_instructions:
        if trees_encountered == 0:
            trees_encountered = traverse(each[0], each[1], trees_map)
        else:
            trees_encountered = trees_encountered * traverse(each[0], each[1], trees_map)

    print(trees_encountered)


if __name__ == '__main__':
    main()