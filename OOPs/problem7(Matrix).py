class Matrix:
    def __init__(self, l):
        self.l = list(l)
    
    # Matrix Multiplication
    def matrixMult(self, a):
        n, m, x, y = len(self.l), len(self.l[0]), len(a), len(a[0])

        if m != x:
            raise ValueError("Matrix Multiplication is not defined")
        else:
            c = [[0 for i in range(x)] for j in range(n)]

            for i in range(n):
                for j in  range(x):
                    for p in range(x):
                        c[i][j] += (self.l[i][p] * a[p][j]) 

        return Matrix(c)
    
    # Transpose
    def Transpose(self):    
        newl = [[j[i] for j in self.l] for i in range(len(self.l[0]))]
        return Matrix(newl)
    
    # Add
    def add(self, a):
        n, m, x, y = len(self.l), len(self.l[0]), len(a.l), len(a.l[0])
        if n != x and m != y:
            raise ValueError("Order of matrices are not equal")
        x = self.l
        y = a.l
        newl = []
        for i in range(n):
            l = []
            for j in range(m):
                l.append(x[i][j] + y[i][j])
            newl.append(l)

        return Matrix(newl)
    
a = Matrix([[1, 5], [2, 0]])
b = [[-1, 2], [0, 3]]
d = a.add(Matrix(b))
print(d.l)
print(a.Transpose().l)
c = a.matrixMult(b)
print(c.l)


