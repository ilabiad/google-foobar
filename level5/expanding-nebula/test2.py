example_input = [[True, False, True], [False, True, False], [True, False, True]]
example_input = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
example_input = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
# example_input = [[False for _ in range(4)] for _ in range(4)]


def solution(g):
    width, height = len(g[0]), len(g)
    possible_cols = generate_possible_col(height+1)
    count = {poss_col: 1 for poss_col in possible_cols}
    for i in range(width-1, -1, -1):
        count_tmp = dict()
        for p_col_right in count.keys():
            for p_col_left in possible_cols:
                if verify(g, (p_col_left, p_col_right), i):
                    count_tmp[p_col_left] = count_tmp.get(p_col_left, 0) + count[p_col_right]
        count = count_tmp
    return sum(count.values())


def verify(g, col_l_r, ind):
    for i in range(len(col_l_r[0])-1):
        r = col_l_r[0][i] + col_l_r[0][i+1] + col_l_r[1][i] + col_l_r[1][i+1]
        if (r == 1) != g[i][ind]:
            return False
    return True


def generate_possible_col(col_len):
    result = [()]
    for i in range(col_len):
        n = len(result)
        for j in range(n):
            result.append(result[j] + (False,))
            result[j] = result[j] + (True,)
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
    print(solution(example_input))