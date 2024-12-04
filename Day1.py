if __name__ == "__main__":
    f = open("data/Day1_file.txt", "r")

    left_list = []
    right_list = []

    for line in f:
        line = line.strip().split("  ")
        left = line[0].strip()
        right = line[1].strip()

        left_list.append(int(left))
        right_list.append(int(right))

    f.close()

    left_list.sort()
    right_list.sort()

    total_sum = 0

    for i in range(len(left_list)):
        total_sum += abs(left_list[i] - right_list[i])

    print(total_sum)
