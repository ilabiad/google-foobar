example_input = 3, [7, 3, 5, 1]
example_input = 5, [19, 14, 28]


def solution(h, q):
    # each element is the parent of the index value
    liste = [0]*(2**h)
    populate_l(liste, h, 0, [2**h-1], -1)
    result = []
    for i in q:
        result.append(liste[i])
    return result


def populate_l(l, h, current_h, current_v, parent_v):
    if current_h >= h:
        return
    l[current_v[0]] = parent_v

    parent_v = current_v[0]
    current_v[0] -= 1
    populate_l(l, h, current_h + 1, current_v, parent_v)
    populate_l(l, h, current_h + 1, current_v, parent_v)


if __name__ == '__main__':
    print(solution(*example_input))

