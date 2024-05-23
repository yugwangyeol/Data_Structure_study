def find_min_max(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)):
        if A[i] < min:
            min = A[i]
        if A[i] > max:
            max = A[i]
    return min, max

data = [3, 5, 2, 1, 7, 9, 8, 4, 6]
x,y = find_min_max(data)

if __name__ == "__main__":
    print("(min,max) = ", (x,y))