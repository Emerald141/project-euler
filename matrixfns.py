def matrixmult(mat1, mat2):
    result = [ [0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
    for row in range(len(result)):
        for col in range(len(result[0])):
            for i in range(len(mat2[0])):
                result[row][col] += mat1[row][i] * mat2[i][col]
    return result

def rref(matrix, printing=False): #Assuming nonempty input
    height = len(matrix)
    width = len(matrix[0])
    toprow = 0
    leftcol = 0
    if printing:
        show(matrix)
    while True:
        #Step 1: Find first column that isn't all 0's
        pivotrow, pivotcol = -1, -1
        for col in range(leftcol, width):
            for row in range(toprow, height):
                if matrix[row][col] != 0:
                    pivotrow, pivotcol = row, col
                    break
            else:
                continue
            break
        if pivotrow == -1: break #all done
        #If pivot is not in top row, move it there
        if pivotrow != toprow:
            matrix[pivotrow], matrix[toprow] = matrix[toprow], matrix[pivotrow]
            if printing:
                print("Swap R", pivotrow + 1, " and R", toprow + 1, sep='')
                show(matrix)
        #Step 2: Divide first row by pivot
        divisor = matrix[toprow][pivotcol]
        for col in range(width):
            matrix[toprow][col] /= divisor
        if printing:
            print("R", toprow + 1, " / ", snip(divisor), sep='')
            show(matrix)
        #Step 3: Add multiples of pivot row to other rows
        for row in range(height):
            if row == toprow:
                continue
            multiplier = -1 * matrix[row][pivotcol]
            for col in range(pivotcol, width):
                matrix[row][col] += multiplier * matrix[toprow][col]
            if printing:
                print("R", row + 1, " + ", snip(multiplier), " R", toprow + 1, sep='')
        #Step 4: Repeat
        if printing:
            show(matrix)
        toprow += 1
        leftcol = pivotcol + 1
    return matrix

def show(matrix):
    for row in matrix:
        for entry in row:
            print(snip(entry), end = '\t')
        print()
    print()

def snip(decimal):
    output = decimal * 1000 // 1 / 1000
    if output % 1 == 0:
        return int(output)
    return output

def solve(matrix):
    rref(matrix)
    result = []
    for row in matrix:
        result.append(row[-1])
    return result
