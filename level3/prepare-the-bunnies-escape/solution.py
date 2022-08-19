example_input = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
#example_input = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1],
#[0, 1, 1, 1, 1,1], [0, 0, 0, 0, 0, 0]]

example_input = [[0, 1, 1, 1, 1, 1],
                 [0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 1, 1, 0],
                 [0, 1, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1, 0]]


def solution(map):
    w, h = len(map[0]), len(map)
    dist_map = [[[float('inf'), float('inf')] for _ in range(w)] for _ in range(h)]
    dist_map[0][0] = [0, 0]
    sptSet = [[[False, False] for _ in range(w)] for _ in range(h)]
    for _ in range(2*w*h):
        i, j, bit = min_distance(dist_map, sptSet)
        if i is None or j is None or bit is None:
            break
        sptSet[i][j][bit] = True
        if i + 1 < h:
            if map[i+1][j] and dist_map[i][j][0] + 1 < dist_map[i+1][j][1]:
                dist_map[i + 1][j][1] = dist_map[i][j][0] + 1
            elif not map[i+1][j]:
                if dist_map[i][j][0] + 1 < dist_map[i+1][j][0]:
                    dist_map[i+1][j][0] = dist_map[i][j][0] + 1
                if dist_map[i][j][1] + 1 < dist_map[i+1][j][1]:
                    dist_map[i + 1][j][1] = dist_map[i][j][1] + 1
        if i - 1 >= 0:
            if map[i-1][j] and dist_map[i][j][0] + 1 < dist_map[i-1][j][1]:
                dist_map[i - 1][j][1] = dist_map[i][j][0] + 1
            elif not map[i-1][j]:
                if dist_map[i][j][0] + 1 < dist_map[i-1][j][0]:
                    dist_map[i-1][j][0] = dist_map[i][j][0] + 1
                if dist_map[i][j][1] + 1 < dist_map[i-1][j][1]:
                    dist_map[i - 1][j][1] = dist_map[i][j][1] + 1
        if j + 1 < w:
            if map[i][j+1] and dist_map[i][j][0] + 1 < dist_map[i][j+1][1]:
                dist_map[i][j+1][1] = dist_map[i][j][0] + 1
            elif not map[i][j+1]:
                if dist_map[i][j][0] + 1 < dist_map[i][j+1][0]:
                    dist_map[i][j+1][0] = dist_map[i][j][0] + 1
                if dist_map[i][j][1] + 1 < dist_map[i][j+1][1]:
                    dist_map[i][j+1][1] = dist_map[i][j][1] + 1
        if j - 1 >= 0:
            if map[i][j-1] and dist_map[i][j][0] + 1 < dist_map[i][j-1][1]:
                dist_map[i][j-1][1] = dist_map[i][j][0] + 1
            elif not map[i][j-1]:
                if dist_map[i][j][0] + 1 < dist_map[i][j-1][0]:
                    dist_map[i][j-1][0] = dist_map[i][j][0] + 1
                if dist_map[i][j][1] + 1 < dist_map[i][j-1][1]:
                    dist_map[i][j-1][1] = dist_map[i][j][1] + 1
    # TODO: uncomment the next comment if working to debug an example or just for extra visualisation
    # print_dist_map(dist_map, map)
    return min(dist_map[-1][-1][0], dist_map[-1][-1][1]) + 1


def min_distance(dist_map, sptSet):
    min_v = float('inf')
    min_indexes = None, None, None
    for i in range(len(dist_map)):
        for j in range(len(dist_map[0])):
            if dist_map[i][j][0] < min_v and not sptSet[i][j][0]:
                min_v = dist_map[i][j][0]
                min_indexes = i, j, 0
            if dist_map[i][j][1] < min_v and not sptSet[i][j][1]:
                min_v = dist_map[i][j][1]
                min_indexes = i, j, 1
    return min_indexes


def print_dist_map(d_map, map):
    for i in range(len(d_map)):
        print(d_map[i])
    print()
    for i in range(len(map)):
        print(map[i])


if __name__ == '__main__':
    print(solution(example_input))
