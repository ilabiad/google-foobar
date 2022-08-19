example_input = '1'


def solution(n):
    return_s = [float('inf'), False]
    input_num = map(int, list(n))
    # solution_recu(input_num, 0, return_s)
    # return return_s[0]
    return solution_iter(input_num)


def solution_iter(input_n):
    steps = 0
    while not (len(input_n) == 1 and input_n[0] == 1):
        steps += 1
        if input_n[-1] % 2 == 0:
            input_n = devide_by_two(input_n)
        elif (len(input_n) == 1 and input_n[-1] in (3, 5, 9)) or (len(input_n) >= 2 and (10 * input_n[-2] + input_n[-1]) % 4 == 1):
            input_n = minus_one(input_n)
        else:
            input_n = add_one(input_n)
    return steps


def add_one(num):
    i = len(num) - 1
    rest = 1
    while i >= 0 and rest > 0:
        if num[i] == 9:
            num[i] = 0
        else:
            num[i] += 1
            rest = 0
        i -= 1
    if rest > 0:
        num = [1] + num
    return num


def minus_one(num):
    i = len(num) - 1
    rest = 1
    while i >= 0 and rest > 0:
        if num[i] == 0:
            num[i] = 9
        else:
            num[i] -= 1
            rest = 0
        i -= 1
    if num[0] == 0:
        num = num[1:]
    return num


def devide_by_two(num):
    i = 0
    rest = 0
    while i < len(num):
        old_num_i = num[i]
        num[i] = num[i] // 2 + rest
        if old_num_i % 2 == 1:
            rest = 5
        else:
            rest = 0
        i += 1

    if num[0] == 0:
        num = num[1:]
    return num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(example_input))
