example_input = [[True, False, True], [False, True, False], [True, False, True]]
example_input = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
example_input = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
example_input = [[False for _ in range(4)] for _ in range(4)]


def solution(g):
    width, height = len(g[0]), len(g)
    num_w, num_h = width // 3, height // 3
    configurations = []
    n = 2
    for i in range(0, height, n):
        tmp_l = []
        for j in range(0, width, n):
            tmp_g = [g[row][j:min(j+n, width)] for row in range(i, min(i+n, height))]
            tmp_l.append(create_parent_configurations(tmp_g))
        configurations.append(tmp_l)
    a = 1
    configurations_choice = [[None for _ in range(len(configurations[0]))] for _ in range(len(configurations))]
    count = [0]
    cout_solutions(configurations, configurations_choice, 0, 0, count)
    return count[0]


def cout_solutions(configurations, conf_choice, i, j, count):
    if i >= len(configurations):
        count[0] += 1
        return
    
    for ind, config in enumerate(configurations[i][j]): 
        if j > 0:
            cont = False
            for row in range(len(config)):
                if config[row][0] != configurations[i][j-1][conf_choice[i][j-1]][row][-1]:
                    cont = True
                    break
            if cont:
                continue
        if i > 0:
            cont = False
            for col in range(len(config[0])):
                if config[0][col] != configurations[i-1][j][conf_choice[i-1][j]][-1][col]:
                    cont = True
                    break
            if cont:
                continue

        conf_choice[i][j] = ind
        if j >= len(configurations[0])-1:
            cout_solutions(configurations, conf_choice, i+1, 0, count)
        else:
            cout_solutions(configurations, conf_choice, i, j+1, count)
        conf_choice[i][j] = None


def create_parent_configurations(g):
    width, height = len(g[0]), len(g)
    configurations = [[]]
    for i in range(height+1):
        for config in configurations:
            config.append([])
        for j in range(width+1):
            n = len(configurations)
            for ind in range(n):
                configurations.append(copy_list_list(configurations[ind]))
                configurations[ind][-1].append(True)
                configurations[-1][-1].append(False)
    result = []
    for config in configurations:
        if downstream_and_verify(config, g):
            result.append(config)
    return result


def copy_list_list(liste):
    result = []
    for i in range(len(liste)):
        result.append(liste[i][:])
    return result


def downstream_and_verify(config, g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            c = config[i][j] + config[i][j+1] + config[i+1][j] + config[i+1][j+1]
            if g[i][j] != (c == 1):
                return False
    return True


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
