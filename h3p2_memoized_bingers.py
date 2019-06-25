# To utilize the memoized MatrixChainMultiplication
# instantiate the class with the single parameter of
# a list of matrix dimensions.  Then call the memoized
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
        n = len(self.p) - 1

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
                temp.append(self.MAX)
            self.T.append(temp)

    def memoized(self, i = None, j = None):
        if i and j:
            if self.T[i-1][j-1] < self.MAX:
                return self.T[i-1][j-1]

            if i == j:
                self.T[i-1][j-1] = 0
                return 0
                
            # Set m to a very large number, then work backwards
            # to find the smallest number of multiplications
            m = self.MAX

            for k in range(i, j):
                q = self.memoized(i, k) + self.memoized(k+1, j) + (self.p[i-1] * self.p[k] * self.p[j])
                if q < m:
                    m = q
                    self.T[i-1][j-1] = q
            return self.T[i-1][j-1]
        else:
            return self.memoized(1, len(self.p)-1)

if __name__ == "__main__":
    dimensions = [1, 2, 3, 4, 3]
    mcm = MatrixChainMultiplication(dimensions)
    print("Result = " + str(mcm.memoized()))
