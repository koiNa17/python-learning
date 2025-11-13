def filter_even(matrix):
    even_numbers = []
    for row in matrix:
        for n in row:
            if n % 2 == 0:
                even_numbers.append(n)
    return even_numbers

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(filter_even(matrix))