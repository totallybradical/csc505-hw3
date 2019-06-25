# To utilize the recursive MatrixChainMultiplication
# instantiate the class with the single parameter of
# a list of matrix dimensions.  Then call the recursive
# function with (1, len(dimensions) - 1).
#
# (See __main__ section for example)

import sys
import math

# Source logic from Chapter 15 of MIT Press
# Introduction to Algorithms

class MatrixChainMultiplication:
    p = []
    MAX = None

    def __init__(self, dimensions):
        self.p = dimensions
        # (Adapt for Python2 or Python3)
        if (sys.version_info > (3, 0)):
            # Python3
            self.MAX = math.inf
        else:
            # Python2
            self.MAX = float("inf")

    def recursive(self, i, j):
        if i == j:
            return 0
            
        # Set m to a very large number, then work backwards
        # to find the smallest number of multiplications
        m = self.MAX

        for k in range(i, j):
            q = self.recursive(i, k) + self.recursive(k+1, j) + (self.p[i-1] * self.p[k] * self.p[j])
            if q < m:
                m = q
        return m

if __name__ == "__main__":
    dimensions = [1, 2, 3, 4, 3]
    mcm = MatrixChainMultiplication(dimensions)
    n = len(dimensions) - 1
    print("Result = " + str(mcm.recursive(1, n)))
