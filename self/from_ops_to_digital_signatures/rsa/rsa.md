# RSA

## Problem to Solve:

How do Bob allows others send him messages privately, without others have to agree with him on a secret shared key before.

One approach is that Bob has a way of producing locks that only he can unlock, thus he gives locks to everyone that wishes to communicate with him, those people put the data on the lock, and lock it. Only Bob can unlock them.

The challenge is come with a computational / mathematical system that implement this, one of those systems is RSA.

The lock can be mathematically described as one-way functions, with a trap-door.

Assuming that the data to be hidden are integers.

A function $f$ can take an integer $m$ and convert it to $f(m)$, if this function $f$ has properties that ensures that is no possible to get $m$ from $f$, that's where one-way comes from. They are useless in this setting because they allow encrypting the message, but not to decrypt it, unless somehow they have an exit-door that allows somehow get $m$ back.

So in the lock analogy:

Bob needs a function that can be give out, so that everyone can use it, but only Bob knows how to recover the original input given to the function having the transformed input by the function.

The RSA system is a way to build this lock.

## Idea

Given a modulus $n$, the plain data will be a number from the set $0, 1, \dots, n-1$, and the encrypted data will be another number on this set also.

Start with a message plain $P$, then look at the numbers:

$$P, P^2, \dots, P^{n-1} \mod n,$$

Public key (lock) will be one exponent $e$ and the modulus $n$, so to encrypt a message $P$, what's done is simply $P \rightarrow P^e \mod n$. To decrypt is used other exponent $d$ that has the ideal property that $X^{de} = X \mod n$, so $P^{de} = P$.

If $n$ is big enough, how do $P^e \mod n$, fast exponentiation.

Let's say $D$ is the set composed by all the messages that Bob can receive, this set can't be infinite, because those messages will be mapped to integers on $(0, n-1)$, so an implementation needs to provide this mapping somehow.

## Security

To decrypt a message $P$ having $(e, n, \text{and } C = P^e \mod n)$ one way is to iterate over all the integers $1, 2, \dots, n - 1$, this is not feasible if $n$ is big enough.

The other way to get $P$ back from $P^e \mod n$, is try to search an integer $d$, such that $P^{ed} = P \mod n$, the thing is that if $(e, n) = 1$, then $d$ is the integer such that $ed = 1 \mod \phi(n)$.

This integer $d$ can be found using extended euclides algorithm if both $e$ and $\phi(n)$ are known, but the trick idea here is find a way of giving $n$ public, but making finding $\phi(n)$ not feasible from a computational point of view.

To achieve this $n$ is chosen in a specific way, $n = p * q$, where $p, q$ are primes large enough to make $n$ large, $\phi(n) = (p-1) * (q-1)$.

One question that remains to me is let's say I know $e$ and $n$, and $P^e$, why the only way to get $P$ back is to find the integer $d$, what shows that there isn't another trick, property, etc, that could get $P$ back. Seems like this is called the RSA problem.

## The Factoring Problem

It's believed that factoring a number does not have efficient algorithm, there are algorithms but they aren't efficient in all the cases.

### Smallest Prime Factor

To factor $n$, iteration from $2$ to $\sqrt{N}$ can be done, checking if the number divides $n$, this is inefficient since if $N$ has $n$ bits, then $\sqrt{N}$ will have $N / 2$ bits. Of course if a $n$ has a small prime factor, then it will be found faster.

## Finding the Exponents Pair.

In modular arithmetic given $x$ and modulo $m$, there could exist $y$ such that $x * y = 1 \mod m$,

The idea is start with $P$, the lock is an exponent and a modulus $(e, n)$, the lock will be $P^e \mod n$, now to get $P$, someone will need to find the number $d$ such that:

$$\begin{align}
P^{ed} &= P \mod n \\
P^{(ed) - 1} &= 1 \mod n
\end{align}$$

Is known that $P^{\phi(n)} = 1 \mod n$, so $d$ should be chosen such that:

$$ed - 1 = 0 \mod \phi(n)$$

Which means finding the inverse of $e$ with respect to $\phi(n)$,

There is no difference mathematically between $e$ and $d$, one is used publicly and the other privately.

Can start with $P$ then $P^d \mod n$, then $P^{d^e} = P \mod n$, the thing is that there is no computationally feasible way of getting back to $P$, without knowing the other number.

If I have $P^d$, to get $P$ I need $e$, and vice versa.
