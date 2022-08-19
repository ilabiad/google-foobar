example_input = 200


def solution(n):
    cache = [[None]*(n+1) for _ in range(n+1)]
    s = solution_recu(n, n, cache)
    return s


def solution_recu(previous_step, remaining_v, cache):
    if previous_step <= 1 and remaining_v > 0:
        cache[previous_step][remaining_v] = 0
        return 0
    elif remaining_v < 0:
        return 0
    if remaining_v == 0:
        return 1

    if cache[previous_step][remaining_v] is not None:
        return cache[previous_step][remaining_v]

    return_value = 0
    for i in range(previous_step-1, 0, -1):
        return_value += solution_recu(i, remaining_v-i, cache)

    cache[previous_step][remaining_v] = return_value

    return return_value


if __name__ == '__main__':
    print(solution(example_input))


