import random

def convert_to_base(x: int, base: int) -> list[int]:
    result = []
    while True:
        result.append(x % base)
        x //= base
        if x == 0:
            break
    return result


def base_to_number(x: list[int], base: int) -> int:
    number = 0
    pow = 1
    for i in range(len(x)):
        number += x[i] * pow
        pow *= base
    return number


def compare(x: list[int], y: list[int]) -> bool:
    # true if x < y
    if len(x) > len(y):
        return False
    if len(x) < len(y):
        return True

    for i in range(len(x) - 1, -1, -1):
        if x[i] < y[i]:
            return True
        if x[i] > y[i]:
            return False

    return False


def shift(x: list[int], n) -> list[int]:
    return [0] * n + x


def subtract(x: list[int], y: list[int], base: int) -> list[int]:
    result = [0] * len(x)
    carry = False
    for i in range(0, len(x)):
        d = x[i] - y[i] if i < len(y) else x[i]
        if carry:
            d -= 1

        if d >= 0:
            result[i] = d
            carry = False

        else:
            result[i] = base + d
            carry = True

    while len(result) > 0 and result[-1] == 0:
        result.pop()

    return result


def add(x: list[int], y: list[int], base: int) -> list[int]:
    if len(x) < len(y):
        temp = x
        x = y
        y = temp
    x = x + [0]
    y = y + [0] * (len(x) - len(y))
    result = [0] * (len(x))
    carry = False
    for i in range(0, len(x)):
        d = x[i] + y[i]
        if carry:
            d += 1

        if d < base:
            result[i] = d
            carry = False
        else:
            result[i] = d - base
            carry = True

    while len(result) > 0 and result[-1] == 0:
        result.pop()

    return result


def division_school(x: int, y: int, base=2) -> tuple[int, int]:
    base_x = convert_to_base(x, base)
    base_y = convert_to_base(y, base)

    q = [0]

    while not compare(base_x, base_y):
        shift_len = len(base_x) - len(base_y)
        suffix = base_x[ -len(base_y) :]
        if compare(suffix, base_y):
            shift_len -= 1

        shifted = shift(base_y, shift_len)
        base_x = subtract(base_x, shifted, base)
        q = add(q, shift([1], shift_len), base)

    return base_to_number(q, base), base_to_number(base_x, base)

def division_school_tests():
    for _ in range(1000):
        a, b = random.randint(2, 1000), random.randint(2, 100)
        base_a = convert_to_base(a, b)
        if base_to_number(base_a, b) != a:
            print("Something is wrong when converting the bases")
        c = random.randint(1, 100)
        base_c = convert_to_base(c, b)

        if (a < c) != compare(base_a, base_c):
            print(
                f"Something is wrong on the compare algorithm {a}, {c}, {base_a}, {base_c}"
            )

        s = random.randint(0, 10)
        if a * (b**s) != base_to_number(shift(base_a, s), b):
            print(f"Something is wrong with the shift operation a = {a}, shift = {s}")

        x = random.randint(1, a - 1)
        if a - x != base_to_number(subtract(base_a, convert_to_base(x, b), b), b):
            print(f"Something is wrong when subtracting a = {a}, x = {x}")

        if a + x != base_to_number(add(base_a, convert_to_base(x, b), b), b):
            print(f"Something is wrong when adding a = {a}, x = {x}")