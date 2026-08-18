# Optimization Subset


## Motivation

When I was trying to understand how the function of the mean squares error behaves, I had to stop, because I didn't know what was going on.

The function is this one: 

$$\sum_{v \in V} (w^T v - y_v)^2$$

In this situation, there is a set of vectors $V$ from $\mathbb{R}^n$, and each vector $v \in V$ has assigned a scalar $y_v$, the goal is find a vector $w \in \mathbb{R}^n$ that minimizes that function. 

Seems like this function is convex, and it has a global minimum, that can be easily found, but I don't know about any of that.

Seems like any attempt to understand things on machine learning depends on knowing ideas from linear algebra, analysis, and optimization. 

So I tried to study what convex optimization was about. 

The problem is that lecture videos and books use an approach bottom-up, what I mean is that they provide definitions, prove facts and theorems, and keep going, but that does not explain, how does the definitions came up. 

Why use those and not others, this is the typical scenario that occurs on programming, one does not always start with the abstractions directly, the abstractions came after seeing the same behavior / structure repeated in many places.

The approach I'll use is study the theory but in the chronological order that the theory was developed.

## Timeline

### Simplex Method by George B. Dantzig 


#### Event: 

George B. Dantzig develops the simplex method.

#### Description:



[Simplex](simplex.md)