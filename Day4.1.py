looking_for = "X-MAS"
m_pkt = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
matrix_size = 0


def print_matrix(matrix):
    for line in matrix:
        for char in line:
            print(char, end=" ")
        print("")


def checking_one_x(x, y):
    checking_positions = []
    if 0 <= x-1 < matrix_size and 0 <= y-1 < matrix_size and 0 <= x+1 < matrix_size and 0 <= y+1 < matrix_size:
        if ((matrix[1 + x][1 + y] == "M" and matrix[-1 + x][1 + y] == "S" and
             matrix[1 + x][-1 + y] == "M" and matrix[-1 + x][-1 + y] == "S") or
            (matrix[1 + x][1 + y] == "S" and matrix[-1 + x][1 + y] == "M" and
             matrix[1 + x][-1 + y] == "S" and matrix[-1 + x][-1 + y] == "M") or
            (matrix[1 + x][1 + y] == "S" and matrix[-1 + x][1 + y] == "S" and
             matrix[1 + x][-1 + y] == "M" and matrix[-1 + x][-1 + y] == "M") or
            (matrix[1 + x][1 + y] == "M" and matrix[-1 + x][1 + y] == "M" and
             matrix[1 + x][-1 + y] == "S" and matrix[-1 + x][-1 + y] == "S")):
            checking_positions.append([x, y])
            checking_positions.append([1+x, 1+y])
            checking_positions.append([-1+x, 1+y])
            checking_positions.append([1+x, -1+y])
            checking_positions.append([-1+x, -1+y])

    return list(checking_positions)


if __name__ == "__main__":
    with open("data/Day4_file.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]

    matrix_size = len(matrix[0])

    new_positions = []
    counter = 0

    for line in range(len(matrix)):
        for char in range(len(matrix[line])):
            if matrix[line][char] == "A":
                checking_positions = checking_one_x(line, char)
                if checking_positions:
                    new_positions += checking_positions
                    counter += 1

    new_positions_set = set(map(tuple, new_positions))

    for line in range(len(matrix)):
        for char in range(len(matrix[line])):
            if not (line, char) in new_positions_set:
                matrix[line][char] = "."

    print_matrix(matrix)

    print("Count: ", counter)
