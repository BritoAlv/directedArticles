## Division

### Definition

The integer division is about given two integers $a, b$ such that $b > 0$, then there are always two unique integers $q, r$ such that:

$$
\begin{align}
a &= q \cdot b + r \\
0 &\leq r < b
\end{align}
$$

#### Notes of the Proof:

To find $(q, r)$, there is the sequence $a - b$, $a - 2 \cdot b$, $a - 3 \cdot b$, $\dots$, in the case that $a > 0$.

There can't be a strictly decreasing sequence of positive integers.

### Naive Algorithm

The next step involves having an algorithm to obtain those two numbers, with the idea of the subsequence a naive algorithm could be written.

The problem of this algorithm is that the number of steps it takes depends on how many times $b$ can be subtracted / added from $a$. So the question is about whether there is a better one?

### Binary Search Algorithm

One way to solve the problem is with binary search on $q$, this gives a number of steps proportional to the number of bits $m$ of $q$.

The problem of this approach is that to check the condition every time multiplication $q \cdot b$ is needed, and this can't be done in a single step like addition / subtraction.

The number of steps of the binary search approach is $m \cdot (\text{multiplication cost})$, multiplying two numbers in base $2$, with at most $m$ digits each with the school method takes $m^2$ steps, so the number of steps will be $m^3$.

### Division School

The algorithm of division taught in classes:

Let's say $a, b$ are represented in base $X$ as:

$$
\begin{align}
a &= a_1 a_2 \dots a_n a_{n+1} \dots a_m \\
b &= b_1 b_2 \dots b_n
\end{align}
$$

As long as $a_1 a_2 \dots a_n \geq b$ we can subtract $b \cdot X^{n - m}$ from $a$, this can be done at most $(X - 1)$ times.

After that either $a_1 a_2 \dots a_n = 0$, in which case the digits of $a$ decreased by $n$, or $0 < a_1 \dots a_n < b$.

At this point it happens that if we again subtract $b \cdot X^{n - m}$ from $a$, at most $(X - 1)$ times steps will be executed before $a$ loses one digit.

To see why:

Here is the thing for example:
$24 \mid 3$

$3 = 3 \cdot 10$ is bigger than $24$, this means that if we subtract $3$ from $24$ in less than $10$ operations we will decrease one digit.

$$
\begin{align}
a_1 a_2 \dots a_n (X - 1) &< b_1 b_2 \dots b_n 0 \\
&= a_1 a_2 \dots a_n \cdot X + (X - 1) \\
&= (b_1 b_2 \dots b_n - d) \cdot X + (X - 1) \\
&= (b_1 b_2 \dots b_n) \cdot X - d \cdot X + (X - 1) \\
&< (b_1 b_2 \dots b_n) \cdot X
\end{align}
$$

This means it will take a number of steps proportional of $X \cdot m$ steps, in each step we do at most $2 \cdot X$ operations, shift / addition and subtraction, and there are at most $m$ steps. The cost of addition / subtraction / shift is $m$, $m$ is the number of digits, so this algorithm uses a number of steps proportional to $m^2$ steps.
