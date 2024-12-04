if __name__ == "__main__":
    left_list = []
    right_list = []

    with open("data/Day1_file.txt", "r") as f:
        for line in f:
            line = line.strip().split()
            left = int(line[0])
            right = int(line[1])

            left_list.append(left)
            right_list.append(right)

    total_sum = 0
    for i in range(len(left_list)):
        similarity_score = right_list.count(left_list[i])
        total_sum += left_list[i] * similarity_score

    print(total_sum)
