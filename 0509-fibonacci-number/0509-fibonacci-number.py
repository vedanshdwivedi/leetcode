class Solution:
    def fib(self, n: int) -> int:
        cache = {}

        def calculateFib(n):
            if n <= 1:
                return n
            if n in cache:
                return cache[n]
            cache[n] = calculateFib(n-1) + calculateFib(n-2)
            return cache[n]

        return calculateFib(n)