example_input = [20, 3, 10, 2, 8], 8
# example_input = [1, 2, 3, 4], 15
# example_input = [4, 3, 5, 7, 8], 12
example_input = [1, 2, 6, 9, 3, 4, 8], 9


def solution(l, t):
    s = [l[0]]
    i, j = 0, 0

    while i < len(l):
        j = move_end(i, j, s, l, t)
        if s[0] < t and j == len(l) - 1:
            return [-1, -1]
        elif s[0] == t:
            return [i, j]
        s[0] -= l[i]
        i += 1
        if j < i:
            j = i
            s[0] = l[i]


def move_end(i, j, s, l, t):
    if s[0] < t:
        while j < len(l) - 1 and s[0] < t:
            j += 1
            s[0] += l[j]
        return j
    else:
        while j > i and s[0] > t:
            s[0] -= l[j]
            j -= 1
        return j


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(*example_input))
