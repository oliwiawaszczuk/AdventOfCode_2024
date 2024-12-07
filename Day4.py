looking_for = "XMAS"
m_pkt = [(-1, -1), (0, -1), (1, -1), (0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0)]
matrix_size = 10


def print_matrix(matrix):
    for line in matrix:
        for char in line:
            print(char, end=" ")
        print("")


def checking_one_x(x, y):
    count = 0
    checking_positions = []
    for mx, my in m_pkt:
        if 0 <= x + mx < matrix_size and 0 <= y + my < matrix_size:
            if matrix[mx+x][my+y] == "M":
                if 0 <= x + 2*mx < matrix_size and 0 <= y + 2*my < matrix_size:
                    if matrix[2*mx + x][2*my + y] == "A":
                        if 0 <= x + 3*mx < matrix_size and 0 <= y + 3*my < matrix_size:
                            if matrix[3*mx + x][3*my + y] == "S":
                                count += 1
                                checking_positions.append([x, y])
                                checking_positions.append([mx+x, my+y])
                                checking_positions.append([2*mx+x, 2*my+y])
                                checking_positions.append([3*mx+x, 3*my+y])

    return list(checking_positions), count


if __name__ == "__main__":
    with open("data/example.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]

    matrix_size = len(matrix[0])

    new_positions = []
    counter = 0

    for line in range(len(matrix)):
        for char in range(len(matrix[line])):
            if matrix[line][char] == "X":
                checking_positions, count = checking_one_x(line, char)
                new_positions += checking_positions
                counter += count

    new_positions_set = set(map(tuple, new_positions))

    for line in range(len(matrix)):
        for char in range(len(matrix[line])):
            if not (line, char) in new_positions_set:
                matrix[line][char] = "."

    print_matrix(matrix)

    print("Count: ", counter)
