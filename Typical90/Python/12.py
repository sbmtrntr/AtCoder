from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
H, W = map(int, input().split())
Q = int(input())
masu = [['.']*(W+1) for _ in range(H+1)]
UF = UnionFind((H+1)*(W+1))

def index(x, y):
    return x*(W+1) + y

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1:]
        r -= 1
        c -= 1
        masu[r][c] = '#'
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if masu[r + dir[0]][c + dir[1]] == '#':
                UF.union(index(r, c), index(r + dir[0], c + dir[1]))
    else:
        if masu[q[1]-1][q[2]-1] == '#' and masu[q[3]-1][q[4]-1] == '#' and UF.same(index(q[1]-1, q[2]-1), index(q[3]-1, q[4]-1)):
            print('Yes')
        else:
            print('No')