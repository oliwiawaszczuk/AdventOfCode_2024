def try_to_calc(result, numbers):
    numbers = [int(n) for n in numbers]
    result = int(result)
    results = []
    for i in range(1, len(numbers)):
        if i == 1:
            results.append(numbers[i-1]+numbers[i])
            results.append(numbers[i-1]*numbers[i])
            results.append(int(str(numbers[i-1])+str(numbers[i])))
        else:
            new_results = []
            for r in results:
                new_results.append(r*numbers[i])
                new_results.append(r+numbers[i])
                new_results.append(int(str(r)+str(numbers[i])))
            results = new_results

    return result if result in results else 0


if __name__ == "__main__":
    rows = []
    total = 0
    with open("data/Day7_file.txt","r") as file:
        for line in file:
            rows.append([x for x in line.strip().split()])

    for row in rows:
        total += try_to_calc(row[0][:-1], row[1:])

    print(f"What is their total calibration result? - {total}")
