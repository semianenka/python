matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

a = [
    [1, 2, 3],
    [3, 2, 1],
    [4, 5, 6]
]

b = [
    [1, 2, 3],
    [3, 2, 1],
    [4, 5, 6]
]


def transpose(matrix_):
    return list(map(list, zip(*matrix_)))


def clockwise_90(matrix_):
    return [i[::-1] for i in transpose(matrix_)]


def multiply(matrix1, matrix2):
    new_matrix = []
    transposed = transpose(matrix2)

    def get_item(row_, col_):
        return sum([row_[i] * col_[i] for i in range(len(row_))])

    for row in range(len(matrix1)):
        new_matrix.append([])
        for col in range(len(transposed)):
            new_matrix[row].append(get_item(matrix1[row], transposed[col]))

    return new_matrix


print(f'Transpose a matrix:\n{transpose(matrix)}')
print(f'Turn a matrix on 90 degrees clockwise:\n{clockwise_90(matrix)}')
print(f'Multiply matrixes:\n{multiply(a, b)}')
