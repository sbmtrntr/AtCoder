from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
N = int(input())
memo = defaultdict(int)
memo[0] = 1

def f(x):
    if x in memo:
        return memo[x]
    memo[x] = f(x//2) + f(x//3)
    return memo[x]
    
print(f(N))