# To utilize the dynamic programming MatrixChainMultiplication
# instantiate the class with the single parameter of
# a list of matrix dimensions.  Then call the dp
# function.
#
# (See __main__ section for example)

import sys
import math

# Source logic from Chapter 15 of MIT Press
# Introduction to Algorithms

class MatrixChainMultiplication:
    p = []
    T = []
    MAX = None

    def __init__(self, dimensions):
        self.p = dimensions
        n = len(self.p)

        # (Adapt for Python2 or Python3)
        if (sys.version_info > (3, 0)):
            # Python3
            self.MAX = math.inf
        else:
            # Python2
            self.MAX = float("inf")

        for i in range(0, n):
            temp = []
            for j in range(0, n):
                # Init cell to a very large number, then work backwards
                # to find the smallest number of multiplications
                temp.append(0)
            self.T.append(temp)

    def dp(self):
        n = len(self.p)
        for l in range(2, n):
            for i in range(1, n-l+1):
                j = i+l-1
                try:
                    self.T[i][j] = self.MAX
                except:
                    print("n = " + str(n) + ", l = " + str(l))
                    print("i = " + str(i) + ", j = " + str(j))
                for k in range(1, j):
                    q = self.T[i][k] + self.T[k+1][j] + (self.p[i-1] * self.p[k] * self.p[j])
                    if q < self.T[i][j]:
                        self.T[i][j] = q 
        return self.T[1][n-1]

if __name__ == "__main__":
    dimensions = [1, 2, 3, 4, 3]
    mcm = MatrixChainMultiplication(dimensions)
    print("Result = " + str(mcm.dp()))
