from itertools import combinations

example_input = 2, 1


def solution(num_buns, num_required):
    bunnies_keys = [[] for _ in range(num_buns)]

    key_copies = num_buns - (num_required - 1)
    for key, bunnies in enumerate(combinations(range(num_buns), key_copies)):
        for bunny in bunnies:
            bunnies_keys[bunny].append(key)
    return bunnies_keys


if __name__ == '__main__':
    s = solution(*example_input)
    print(s)
