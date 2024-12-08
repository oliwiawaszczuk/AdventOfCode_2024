def check_pair_akt_with_reguls(reguls, akt1, akt2):
    return [akt1, akt2] in reguls


def check_one_aktualizacja(reguls, update):
    for i in range(1, len(update)):
        flag = check_pair_akt_with_reguls(reguls, update[i - 1], update[i])
        # print(flag, update[i-1], update[i])
        if not flag:
            return False
    return True


def sort_update(reguls, update):
    sorted_update_list = []

    while update:
        for akt in update:
            if all(akt != y or x not in update for x, y in reguls):
                sorted_update_list.append(akt)
                update.remove(akt)
                break

    return sorted_update_list


if __name__ == "__main__":
    reguls = []
    updates = []
    total_sum = 0
    total_sum2 = 0

    with open("data/Day5_file.txt", "r") as f:
        to_reguls = True
        for line in f:
            line = line.strip()
            if line == '':
                to_reguls = False
            else:
                if to_reguls:
                    reguls.append(line)
                else:
                    updates.append(line)

    updates = [akt.split(",") for akt in updates]

    reguls = [reg.split("|") for reg in reguls]

    for update in updates:
        is_good = check_one_aktualizacja(reguls, update)
        if is_good:
            mid = int(update[len(update)//2])
            total_sum += mid
        else:
            sorted_update = sort_update(reguls, update)
            mid = int(sorted_update[len(sorted_update)//2])
            total_sum2 += mid

    print("total sum: ", total_sum)
    print("total sum2: ", total_sum2)
