import random


def test_division(division_implementation, low = 1, up = 100):
    for _ in range(10000):
        a, b = random.randint(low, up), random.randint(1, 10)
        q, r = division_implementation(a, b)
        q_expected = a // b
        r_expected = a - (q_expected) * b
        if (q, r) != (q_expected, r_expected):
            print(f"Result from divide {a} / {b} should be {q_expected}, {r_expected} but obtained {q}, {r}")
            return
        else:
            print(f"Result from divide {a} / {b} is correct {q}, {r}")
			
def remainder(x : int, y : int, division_implementation) :
	_, r = division_implementation(x, y)
	return r

def quotient(x : int, y : int, division_implementation):
	q, _ = division_implementation(x, y)
	return q