import math

def recursive(dims, dim1, dim2):
    if dim1 == dim2:
        return 0
    result = math.inf
    for i in range(dim1, dim2):
        sum_of_pieces = recursive(dims, dim1, i) + recursive(dims, i+1, dim2) + (dims[dim1-1] * dims[i] * dims[dim2])
        if sum_of_pieces < result:
            result = sum_of_pieces
    return result

if __name__ == "__main__":
    dimensions = [1, 2, 3, 4, 3]
    print("Result = " + str(recursive(dimensions, 1, len(dimensions) - 1)))
