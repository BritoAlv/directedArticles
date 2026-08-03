# Perceptron

The Perceptron algorithm solves the problem of finding a line if exists that separate a set of points that belongs to two classes.

The problem is given a set of points $x_i \in R^n$, and $y_i \in \{-1, 1\}$, i.e. each point $x_i$ has assigned a label $y_i$.

Find a line $f(x) = \langle w, x \rangle + b$, such that $y_i \cdot f(x_i) \ge 0$, for all the points.

See that $f(x_i) / |w|$ is the signed distance of the point $x_i$ to this line, the goal is to find a line given by $w$, $b$ that meet those conditions.

**Approach 1:** each constraint is linear on $w$, $b$, so a linear programming solver can do the job.

**Approach 2:** do the following iterative algorithm:

$$
\begin{aligned}
&\text{while } \text{True}: \\
&\quad \text{for } x_i \in x: \\
&\quad\quad \text{if } y_i \cdot f(x_i) < 0: \quad \text{// is wrong} \\
&\quad\quad\quad w = w + y_i \cdot x_i \\
&\quad\quad\quad b = b + y_i \cdot R^2
\end{aligned}
$$
