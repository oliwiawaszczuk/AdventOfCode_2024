import time

allowed_numbers = "0123456789"

if __name__ == "__main__":
    start_time = time.time()
    total_sum = 0
    flag = True
    with open("data/Day3_file.txt", "r") as f:
        whole_str = f.read()
        while len(whole_str) >= 7:
            index_m = whole_str.find("mul(")
            do = whole_str[:index_m].find("do()")
            do_not = whole_str[:index_m].find("don't()")

            if do != -1 and do > do_not:
                flag = True
            if do_not != -1 and do < do_not:
                flag = False

            if index_m == -1:
                whole_str = ""
            else:
                whole_str = whole_str[index_m+4:]
                first = ""
                second = ""

                while whole_str and whole_str[0] in allowed_numbers:
                    first += whole_str[0]
                    whole_str = whole_str[1:]

                if whole_str and whole_str[0] == "," and first != "":
                    whole_str = whole_str[1:]

                    while whole_str and whole_str[0] in allowed_numbers:
                        second += whole_str[0]
                        whole_str = whole_str[1:]

                    if whole_str and second.strip() == "" or whole_str[0] != ")":
                        first = 0
                        second = 0
                    else:
                        if flag:
                            total_sum += int(first) * int(second)

                # print(first, second)

    print(total_sum)

    end_time = time.time()
    print(f"Execution time: {(end_time - start_time)*1000:.2f} ms")
