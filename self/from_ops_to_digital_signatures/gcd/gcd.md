# GCD

To every positive number can be associated a nonempty set of numbers, its divisors, if two of these sets are intersected is obtained another set. The greatest value of this new set, is the greatest common divisor of those two numbers.

$$g = \gcd(a, b)$$

Factoring a number is not an easy task, so finding this number without having to compute the divisors of both $a$, $b$ is interesting.

## How Compute It

It can be done, starting with the fact that:

$$a \geq b, \gcd(a, b) = \gcd(a, a - b)$$

This is proven by showing that the set of common divisors of $(a, b)$ is the same set of common divisors of $(a, a-b)$.

To show that two sets are equals one shows that each is a subset of the other.

$$\gcd(a, b) = \gcd(b, a \bmod b)$$

Again show that those two sets are equal. This allows the following algorithm:

```python
gcd(a, b):
    if a < b:
        swap(a, b)

    return gcd(b, a % b)
```

Why it stops: $a \geq b > a \bmod b$, this process every time decreases the remainder number, eventually it will be $0$.

### Number of Steps of the Algorithm.

Moreover, the number of steps this algorithm takes will be proportional to the number of bits of $a$.

The sequence is:

$$(r + q \cdot k, q, r) \Rightarrow (q, r, \text{rem}(q, r))$$

But the thing is that if $k \geq 2$, then $(r + q \cdot k) \geq 2 \cdot q$, which means that in every step the first number is at least halved, but if $k = 1$, looks like this $(r + q, q, r)$, but this is Fibonacci sequence.

$$2 \cdot (a \bmod b) \leq a$$

$$a = q \cdot b + r$$

$$2 \cdot r =  2 \cdot (a - q \cdot b)$$
$$       =  2 \cdot a - 2 \cdot q \cdot b$$
$$       =  a + (a - 2 \cdot q \cdot b)$$
$$       =  a + ( (a - q \cdot b) - q \cdot b)$$
$$       =  a + (r - q \cdot b)$$
$$       \leq a + (r - b)$$
$$       \leq a$$

Because $a \geq b$ this means that $q \geq 1$, and so $q \cdot b \geq b$ and so

$$0 \leq a - q \cdot b < b \leq q \cdot b$$

So $(a, b) \Rightarrow (b, a \bmod b) \Rightarrow$ one of the inputs is halved.

The observation is that $2 \cdot (a \bmod b) \leq a$, as long as $a \geq b$, which means that if start with input $(a, b)$, after two steps then have $(a \bmod b, ?)$, which is at most half of $a$.

## Linear Combination.

There is another property about the gcd, and it's that if $(a, b)$ are positive integers.

Any linear combination of them $x \cdot a + y \cdot b$ results in a number that is divisible by all the common divisors of both $a$ and $b$.

Let's consider the set $S = \{ x \cdot a + y \cdot b, (x, y) \in \mathbb{Z} \text{ and those numbers are } > 0 \}$ choosing $(x, y)$ big enough shows that this set is not empty, so it has a smallest element.

Somehow the gcd is the smallest positive element of this set.

To see why, the integers $a, b$ exists, linear algebra can be used, as $[a_n, b_n]$ is a linear transformation of $[a_{n-1}, b_{n-1}]$.

This not only shows that those integers exists, but also gives a way to compute them, and the number of steps is the same as the one of the gcd algorithm.

The linear transformation is:

$$M_1 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \text{identity matrix}$$

$$M_{i+1} = M_i \cdot \begin{bmatrix} 0 & 1 \\ 1 & -d_{n-1} \end{bmatrix}$$

$$d_i = \frac{a_i}{b_i}$$

Finally:

$$\begin{bmatrix} a_n \\ b_n \end{bmatrix} = M_n \cdot \begin{bmatrix} a_{n-1} \\ b_{n-1} \end{bmatrix}$$

The linear algebra approach, gives the formula for the integers, and allows computing them in the original euclid algorithm.

Proves that $g$ is on the set, to show that it should be the smallest element, assume otherwise.

The thing is that because $g \mid a, g \mid b$, $g \mid g_1$ and so this means that $g \leq g_1$, so $g = g_1$. In short $g$ is a divisor of every element on that set.

### Proof Taken.

$$x \cdot a + y \cdot b = g_1$$

$$a = q \cdot g_1 + r$$
$$a = q \cdot (x \cdot a + y \cdot b) + r$$

$$r = a \cdot (1 - qx) + b \cdot (-y)$$

So $r$ which is smaller than $g_1$ is in the set, $r$ must be $0$, analogously for $b$, so as a conclusion the smallest element of the set is in the set of the common divisors of both $a$ and $b$.

That does not prove it's the greatest divisor, but it proves that this number $g_1$ is divisible by all the common divisors of both $a$ and $b$.

$$d \mid a, d \mid b \Rightarrow d \mid g_1.$$

In particular $\gcd(a, b) \mid g_1$.

But $g_1$ is a common divisor of both $a$ and $b$, in particular $g_1 \leq \gcd(a, b)$, so it should be the case that $g_1 = \gcd(a, b)$.

Why those two numbers are important?

## Notes

- gcd algorithm is fast, number of steps is $m \cdot \text{division cost}$, $m$ is the number of bits of $\max(a, b)$.
- the linear algebra approach allows to express the computational process of finding a pair of $x, y$, such that $ax + by = \gcd(a, b)$ in a concise way.
- the fact that the gcd is the smallest element of the set formed by the linear combinations is not trivial.
