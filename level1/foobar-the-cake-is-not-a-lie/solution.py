example_input = "abcabcabcabc"
example_input = "abccbaabccba"


def solution(input_string):
    n = len(input_string)
    for i in range(n, 1, -1):
        found_solution = True
        step = int(n/i)
        if step != n * 1.0/i:
            continue
        for j in range(step, n, step):
            if input_string[j:j+step] != input_string[0:step]:
                found_solution = False
                break
        if found_solution:
            return i
    return 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(example_input))
