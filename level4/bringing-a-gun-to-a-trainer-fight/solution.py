example_input = [3, 2], [1, 1], [2, 1], 4  # answer = 7
example_input = [300, 275], [150, 150], [185, 100], 500  # answer = 9
# example_input = [2, 5], [1, 4], [1, 2], 11  # answer = 27
# example_input = [23, 10], [6, 4], [3, 2], 23  # answer = 8
# example_input = [3, 2], [1, 1], [2, 1], 4  # answer = 7
# example_input = [1250, 1250], [1000, 1000], [500, 400], 10000  # answer = 196
# example_input = [3, 2], [1, 1], [2, 1], 7  # answer = 19
# example_input = [2, 3], [1, 1], [1, 2], 4  # answer = 7
# example_input = [3, 4], [1, 2], [2, 1], 7  # answer = 10
# example_input = [4, 4], [2, 2], [3, 1], 6  # answer = 7
# example_input = [300, 275], [150, 150], [180, 100], 500  # answer = 9
# example_input = [3, 4], [1, 1], [2, 2], 500  # answer = 54239
# example_input = [3, 2], [2, 1], [1, 1], 4  # answer = 7


def solution(dimensions, your_position, trainer_position, distance):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    distance_squared = distance ** 2
    infinity = float('inf')
    solutions = dict()
    solutions[apply_euclide_algo(
        (trainer_position[0] - your_position[0], trainer_position[1] - your_position[1]))] = calc_distance(
        your_position, trainer_position)
    possible_solution = (trainer_position[0], -trainer_position[1])
    possible_solution_vector = apply_euclide_algo(
        (possible_solution[0] - your_position[0], possible_solution[1] - your_position[1]))
    solutions[possible_solution_vector] = min(solutions.get(possible_solution_vector, infinity),
                                              calc_distance(your_position, possible_solution))
    forbidden_directions = dict()
    reflected_pos = (your_position[0], -your_position[1])
    reflected_pos_vector = apply_euclide_algo(
        (reflected_pos[0] - your_position[0], reflected_pos[1] - your_position[1]))
    forbidden_directions[reflected_pos_vector] = min(forbidden_directions.get(reflected_pos_vector, infinity),
                                                     calc_distance(your_position, reflected_pos))
    origin_dir = apply_euclide_algo((-your_position[0], -your_position[1]))
    forbidden_directions[origin_dir] = min(forbidden_directions.get(origin_dir, infinity),
                                           calc_distance(your_position, (0, 0)))
    origin_dir = apply_euclide_algo((-your_position[0], -dimensions[1] - your_position[1]))
    forbidden_directions[origin_dir] = min(forbidden_directions.get(origin_dir, infinity),
                                           calc_distance(your_position, (0, -dimensions[1])))

    i = 1
    stop_int = infinity
    origin = [0, -dimensions[1]]
    repeat_value = 1
    solutions_len = len(solutions)
    while i < stop_int:
        dir = directions[(i - 1) % 4]
        if dir[0] == 0:
            repeat_value += 1
        for j in range(repeat_value):
            new_origin = [origin[0] + dir[0] * dimensions[0], origin[1] + dir[1] * dimensions[1]]
            if dir[0] == 0:
                if dir[1] == 1:
                    possible_solution = (
                        possible_solution[0], possible_solution[1] + 2 * (new_origin[1] - possible_solution[1]))
                    reflected_pos = (
                        reflected_pos[0], reflected_pos[1] + 2 * (new_origin[1] - reflected_pos[1]))
                else:
                    possible_solution = (
                        possible_solution[0], possible_solution[1] + 2 * (origin[1] - possible_solution[1]))
                    reflected_pos = (
                        reflected_pos[0], reflected_pos[1] + 2 * (origin[1] - reflected_pos[1]))
            elif dir[1] == 0:
                if dir[0] == 1:
                    possible_solution = (
                        possible_solution[0] + 2 * (new_origin[0] - possible_solution[0]), possible_solution[1])
                    reflected_pos = (
                        reflected_pos[0] + 2 * (new_origin[0] - reflected_pos[0]), reflected_pos[1])
                else:
                    possible_solution = (
                        possible_solution[0] + 2 * (origin[0] - possible_solution[0]), possible_solution[1])
                    reflected_pos = (
                        reflected_pos[0] + 2 * (origin[0] - reflected_pos[0]), reflected_pos[1])

            reflected_pos_vector = apply_euclide_algo(
                (reflected_pos[0] - your_position[0], reflected_pos[1] - your_position[1]))
            forbidden_directions[reflected_pos_vector] = min(
                forbidden_directions.get(reflected_pos_vector, infinity),
                calc_distance(your_position, reflected_pos))

            origin_dir = apply_euclide_algo((new_origin[0] - your_position[0], new_origin[1] - your_position[1]))
            forbidden_directions[origin_dir] = min(forbidden_directions.get(origin_dir, infinity),
                                                   calc_distance(your_position, new_origin))

            c = calc_distance(your_position, possible_solution)
            if c <= distance_squared:
                possible_solution_vector = apply_euclide_algo((
                    possible_solution[0] - your_position[0], possible_solution[1] - your_position[1]))
                solutions[possible_solution_vector] = min(c, solutions.get(possible_solution_vector, infinity))
            elif stop_int == infinity:
                stop_int = i + 4
                solutions_len = len(solutions)
            origin[0], origin[1] = new_origin[0], new_origin[1]
        i += 1
        if stop_int != infinity and solutions_len < len(solutions):
            stop_int = i + 4
            solutions_len = len(solutions)

    result = 0
    for sol_vec, dist in solutions.items():
        forbidden_dist = forbidden_directions.get(sol_vec, None)
        if forbidden_dist is not None and forbidden_dist < dist:
            continue
        elif dist <= distance_squared:
            result += 1
    return result


def calc_distance(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


def apply_euclide_algo(vec):
    a, b = abs(vec[0]), abs(vec[1])
    if a > b:
        gcd = euclide_algo(a, b)
    else:
        gcd = euclide_algo(b, a)
    return vec[0] // gcd, vec[1] // gcd


def euclide_algo(a, b):
    while b:
        a, b = b, a % b
    return a


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = solution(*example_input)
    print(s)
