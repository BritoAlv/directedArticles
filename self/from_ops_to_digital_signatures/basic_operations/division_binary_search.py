def division_binary_search(x: int, y: int) -> tuple[int, int]:
    def condition(q):
        return x - q * y >= 0

    if x >= 0:
        q_low = 0
        q_up = x
    else:
        q_low = x
        q_up = 0
    q = binary_search_from_low(q_low, q_up, condition)
    return q, x - q * y


def binary_search_from_low(low: int, up: int, f) -> int:
    while up - low > 1:
        mid = low + (up - low) // 2
        if f(mid):
            low = mid
        else:
            up = mid - 1
    while low + 1 <= up and f(low + 1):
        low += 1
    return low
