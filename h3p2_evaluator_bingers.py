import sys
import time
from random import randint
import pprint

from h3p2_recursive_bingers import MatrixChainMultiplication as recursive_class
from h3p2_dp_bingers import MatrixChainMultiplication as dp_class
from h3p2_memoized_bingers import MatrixChainMultiplication as memoized_class


if __name__ == "__main__":
    n = int(sys.argv[1])
    timings = {}

    timings[n] = {}
    dimensions = []
    for matrix_sizes in range(n):
        dimensions.append(randint(1, 100))

    # recursive
    recursive_instance = recursive_class(dimensions)
    print("Recursive(1, " + str(n-1) + "), len = " + str(len(dimensions)))
    start = time.time()
    m = recursive_instance.recursive(1, n-1)
    end = time.time()
    run_time = end - start
    timings[n]["recursive"] = run_time
    recursive_instance = None

    # dp
    dp_instance = dp_class(dimensions)
    print("DP()")
    start = time.time()
    m = dp_instance.dp()
    end = time.time()
    run_time = end - start
    timings[n]["dp"] = run_time
    dp_instance = None

    # recursive
    memoized_instance = memoized_class(dimensions)
    print("Memoized(1, " + str(n-1) + ")")
    start = time.time()
    m = memoized_instance.memoized(1, n-1)
    end = time.time()
    run_time = end - start
    timings[n]["memoized"] = run_time
    memoized_instance = None

    pprint.pprint(timings)


    