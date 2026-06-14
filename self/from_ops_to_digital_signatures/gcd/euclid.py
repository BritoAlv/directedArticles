def euclid(a: int, b: int):
    if a < b:
        temp = a
        a = b
        b = temp
    r = a % b
    if r == 0:
        return b
    return euclid(b, r)


def extended_euclid(a: int, b: int) -> tuple[int, int, int]:
    import numpy as np
    assert a > 0 and b > 0
    m = a
    n = b
    r = m % n
    d = m // n

    matrix = [[1, 0], [0, 1]]

    while r > 0:
        updated_matrix = [[0, 1], [1, -d]]
        updated_matrix = np.matmul(updated_matrix, matrix)
        matrix = updated_matrix

        m = n
        n = r
        r = m % n
        d = m // n

    return n, matrix[1][0], matrix[1][1]
