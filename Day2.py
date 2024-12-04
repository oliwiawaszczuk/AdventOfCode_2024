def is_decreasing(list: list) -> bool:
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            return False
    return True


def is_increasing(list: list) -> bool:
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            return False
    return True


def is_list_safe(list: list) -> bool:
    if not (is_decreasing(list) or is_increasing(list)):
        return False
    for i in range(1, len(list)):
        if 1 > abs(list[i] - list[i - 1]) or abs(list[i] - list[i - 1]) > 3:
            return False
    return True


def can_be_safe_with_dampener(lst: list) -> bool:
    for i in range(len(lst)):
        temp_list = lst[:i] + lst[i + 1:]
        if is_list_safe(temp_list):
            return True
    return False


if __name__ == "__main__":
    how_many_safe = 0

    with open("data/Day2_file.txt", "r") as f:
        for line in f:
            line = list(map(int, line.strip().split()))

            if is_list_safe(line) or can_be_safe_with_dampener(line):
                how_many_safe += 1

    print(how_many_safe)
