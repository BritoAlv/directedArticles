def division_naive(x : int, y : int) -> tuple[int, int]:
	assert y > 0
	q = 0
	r = x
	while r < 0:
		r += y
		q -= 1
	while y <= r:
		r -= y
		q += 1
	return q, r
