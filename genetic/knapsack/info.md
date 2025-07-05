# 🧮 Knapsack Problem

The **Knapsack Problem** is a classic combinatorial optimization problem that
arises in resource allocation where the goal is to select a subset of items to
maximize total value without exceeding a given capacity.

## 🧾 Problem Definition

Given a set of `n` items, each with:
- a **weight** `w_i`
- and a **value** `v_i`

And a knapsack with a maximum weight **capacity** `W`, the objective is to
determine the **optimal subset of items** to include in the knapsack so that:
- The **total weight** does not exceed `W`
- The **total value** is **maximized**

This is typically referred to as the **0/1 Knapsack Problem**, where each item
can either be included **(1)** or not **(0)** — no partial items allowed.

## 📥 Input

- A list of items:  
  ```python
  items = [
      {"weight": w_1, "value": v_1},
      {"weight": w_2, "value": v_2},
      ...
      {"weight": w_n, "value": v_n}
  ]

## Solution
A binary vector of length `n`, for example:
```python
solution = [1, 0, 1, 0, ..., 1]
```
We can also say that a solution is a vector
$S = (s_1, s_2, \ldots, s_n) \in \mathbb{R}^n$ and that every
$s_i \in \{0, 1\}$.

## Objective
Maximize function: $f(S) = \sum_i^n s_i * v_i,$
subject to: $\sum_i^n w_i * x_i \leq W$.
