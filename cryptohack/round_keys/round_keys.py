state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    # state = [y for x in s for y in x]
    # round_key = [y for x in k for y in x]
    return ''.join([chr(i ^ j) for x, y in zip(s, k) for i, j in zip(x, y)])
    # dog = [chr(round_key[x] ^ y) for x, y in enumerate(state)]

    # return ''.join(dog)

print(add_round_key(state, round_key))

