class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.matrix[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.matrix[i][j] = value
        else:
            return None

    def transpose(self):
        transposed_matrix = []
        for j in range(self.m):
            new_row = []
            for i in range(self.n):
                new_row.append(self.matrix[i][j])
            transposed_matrix.append(new_row)
        # in cazul in care matricea nu este patratica trebuie sa interschimbam n cu m
        self.n, self.m = self.m, self.n
        self.matrix = transposed_matrix

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Incompatible matrices")

        result_matrix = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result_matrix.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result_matrix

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = func(self.matrix[i][j])


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("S pop")
print(s.pop())

print("S peek")
print(s.peek())

q = Queue()
q.push(1)
q.push(2)
q.push(3)
print("Q pop")
print(q.pop())
print("Q peek")
print(q.peek())

m1 = Matrix(3, 3)
m1.set(0, 0, 1)
m1.set(0, 1, 2)
m1.set(0, 2, 3)
m1.set(1, 0, 4)
m1.set(1, 1, 5)
m1.set(1, 2, 6)
m1.set(2, 0, 7)
m1.set(2, 1, 8)
m1.set(2, 2, 9)
"""
[1,2,3]
[4,5,6]
[7,8,9]
"""

m2 = Matrix(3, 2)
m2.set(0, 0, 7)
m2.set(0, 1, 8)
m2.set(1, 0, 9)
m2.set(1, 1, 10)
m2.set(2, 0, 11)
m2.set(2, 1, 12)
"""
[7,8]
[9,10]
[11,12]
"""
m1.transpose()
print("M1 transposed:")
for row in m1.matrix:
    print(row)

try:
    m3 = m1.multiply(m2)
    for row in m3.matrix:
        print(row)
except ValueError as e:
    print(e)

m1.apply(lambda x: x ** 2)
for row in m1.matrix:
    print(row)
