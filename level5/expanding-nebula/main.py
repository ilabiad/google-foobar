example_input = [[True, False, True], [False, True, False], [True, False, True]]
example_input = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
example_input = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
# example_input = [[False for _ in range(4)] for _ in range(3)]

possibilities_true = [[True, False, False, False], [False, True, False, False], [False, False, True, False], [False, False, False, True]]
possibilities_false = [[False, False, False, False]]
possibilities_false += [[True, True, False, False], [False, False, True, True], [True, False, True, False], [False, True, False, True], [True, False, False, True], [False, True, True, False]]
possibilities_false += [[True, True, True, False], [True, True, False, True], [True, False, True, True], [False, True, True, True]]
possibilities_false += [[True, True, True, True]]


def solution(g):
    width, height = len(g[0]), len(g)
    sol = [[None for _ in range(width + 1)] for _ in range(height + 1)]
    number_of_sol = [0]
    recursive_sol_anchor(g, sol, [height, width], number_of_sol)
    return number_of_sol[0]


def recursive_sol_anchor(g, tmp_sol, anchor, num_sol):
    if anchor[0] <= 0 and anchor[1] <= 0:
        # print_example_input(tmp_sol)
        # print()
        num_sol[0] += 1
        return

    old_anchor_value = anchor[:]
    if anchor[0] > 0:
        anchor[0] -= 1
    if anchor[1] > 0:
        anchor[1] -= 1

    possibilities = generate_possibilities_a(g[anchor[0]][anchor[1]], (tmp_sol[anchor[0]][anchor[1]+1], tmp_sol[anchor[0]+1][anchor[1]], tmp_sol[anchor[0]+1][anchor[1]+1]), anchor[0]==len(g)-1 and anchor[1]==len(g[0])-1)

    for possibility in possibilities:
        old_values = (tmp_sol[anchor[0]][anchor[1]], tmp_sol[anchor[0]][anchor[1]+1], tmp_sol[anchor[0]+1][anchor[1]], tmp_sol[anchor[0]+1][anchor[1]+1])
        tmp_sol[anchor[0]][anchor[1]] = possibility[0]
        tmp_sol[anchor[0]][anchor[1]+1] = possibility[1]
        tmp_sol[anchor[0]+1][anchor[1]] = possibility[2]
        tmp_sol[anchor[0]+1][anchor[1]+1] = possibility[3]
        recursive_sol_vertical(g, tmp_sol, anchor, anchor[0]-1, num_sol)
        tmp_sol[anchor[0]][anchor[1]] = old_values[0]
        tmp_sol[anchor[0]][anchor[1]+1] = old_values[1]
        tmp_sol[anchor[0]+1][anchor[1]] = old_values[2]
        tmp_sol[anchor[0]+1][anchor[1]+1] = old_values[3]

    anchor[0], anchor[1] = old_anchor_value[0], old_anchor_value[1]


def generate_possibilities_a(anchor_v, three_v, last_col_and_row):
    if anchor_v:
        possibilities = possibilities_true
    else:
        possibilities = possibilities_false

    if last_col_and_row:
        return possibilities

    result = []
    for possibility in possibilities:
        if possibility[1] == three_v[0] and possibility[2] == three_v[1] and possibility[3] == three_v[2]:
            result.append(possibility)
    return result


def recursive_sol_vertical(g, tmp_sol, anchor, ind, num_sol):
    if ind < 0:
        recursive_sol_horizontal(g, tmp_sol, anchor, anchor[1]-1, num_sol)
        return

    possibilities = generate_possibilities_v(g[ind][anchor[1]], (tmp_sol[ind][anchor[1]+1], tmp_sol[ind + 1][anchor[1]], tmp_sol[ind+1][anchor[1]+1]), anchor[1] == len(g[0])-1)
    for possibility in possibilities:
        old_values = (tmp_sol[ind][anchor[1]], tmp_sol[ind][anchor[1]+1])
        tmp_sol[ind][anchor[1]] = possibility[0]
        tmp_sol[ind][anchor[1]+1] = possibility[1]
        recursive_sol_vertical(g, tmp_sol, anchor, ind-1, num_sol)
        tmp_sol[ind][anchor[1]] = old_values[0]
        tmp_sol[ind][anchor[1]+1] = old_values[1]


def generate_possibilities_v(anchor_v, bottom_v, last_col):
    if anchor_v:
        possibilities = possibilities_true
    else:
        possibilities = possibilities_false

    result = []
    for possibility in possibilities:
        if possibility[2] == bottom_v[1] and possibility[3] == bottom_v[2]:
            if not last_col and possibility[1] == bottom_v[0]:
                result.append(possibility)
            elif last_col:
                result.append(possibility)
    return result


def recursive_sol_horizontal(g, tmp_sol, anchor, ind, num_sol):
    if ind < 0:
        recursive_sol_anchor(g, tmp_sol, anchor, num_sol)
        return

    possibilities = generate_possibilities_h(g[anchor[0]][ind], (tmp_sol[anchor[0]][ind+1], tmp_sol[anchor[0]+1][ind], tmp_sol[anchor[0]+1][ind+1]), anchor[0] == len(g) - 1)
    for possibility in possibilities:
        old_values = (tmp_sol[anchor[0]][ind], tmp_sol[anchor[0]+1][ind])
        tmp_sol[anchor[0]][ind] = possibility[0]
        tmp_sol[anchor[0]+1][ind] = possibility[2]
        recursive_sol_horizontal(g, tmp_sol, anchor, ind - 1, num_sol)
        tmp_sol[anchor[0]][ind] = old_values[0]
        tmp_sol[anchor[0]+1][ind] = old_values[1]


def generate_possibilities_h(anchor_v, bottom_h, last_row):
    if anchor_v:
        possibilities = possibilities_true
    else:
        possibilities = possibilities_false

    result = []
    for possibility in possibilities:
        if possibility[1] == bottom_h[0] and possibility[3] == bottom_h[2]:
            if not last_row and possibility[2] == bottom_h[1]:
                result.append(possibility)
            elif last_row:
                result.append(possibility)
    return result


def print_example_input(g):
    for line in g:
        str_line = ""
        for b in line:
            if b is None:
                str_line += "x"
            elif b:
                str_line += "O"
            else:
                str_line += "."
        print(str_line)


if __name__ == '__main__':
    print_example_input(example_input)
    print(solution(example_input))
