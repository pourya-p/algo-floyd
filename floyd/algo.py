import numpy as np


class Floyd:
    def __init__(self, matrix):
        self.D = matrix
        self.P = np.full(self.D.shape, -1)

    def compute(self):
        d_row, d_column = self.D.shape
        for k in range(d_column):
            for i in range(d_column):
                for j in range(d_column):
                    res = self.D[i][k] + self.D[k][j]
                    if res < self.D[i][j]:
                        self.D[i][j] = res
                        self.P[i][j] = k



    def router(self, f, t):
        self.compute()
        i, j = f, t
        helper = int(self.P[i][j])
        route = [j]
        while i != j:
            j = int(self.P[i][j])
            if j == -1:
                j = i
            route.append(j)
        route.reverse()

        return route












if __name__ == '__main__':
    matrix = np.array([
        [0, 5, 999, 999],
        [15, 0, 15, 5],
        [30, 999, 0, 15],
        [15, 999, 5, 0]
    ])
    fl = Floyd(matrix)
    fl.compute()
    print(fl.D)
    print(fl.P)
    a = fl.router(0,3)
    print(a)
