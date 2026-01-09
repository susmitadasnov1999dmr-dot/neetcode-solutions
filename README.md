## Problem1
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

## Solution (Python)

```python
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        d = []
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                d.append(i)
        return sum(d)









## Problem2
you are given an integer n.

Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n) is the integer formed by reversing the digits of n.

Return an integer denoting the mirror distance of n​​​​​​​.

abs(x) denotes the absolute value of x.

## Solution (Python)

```python
class Solution:
    def mirrorDistance(self, n: int) -> int:
        r=int(str(n)[::-1])
        return abs(n-r)
