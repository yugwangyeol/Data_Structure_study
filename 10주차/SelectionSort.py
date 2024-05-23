def printStep(A,idx):
    print('     step %d: '%idx, end='')
    print(A)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        #printStep(A,i+1)

def inserttionSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        printStep(A,i)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    #data = [5,5, 3, 8, 4, 2, 9, 1, 6, 7]
    L = list(data)
    print("Original Data   : ", L)
    selectionSort(L)
    print("Selection Sorted Data: ", L)

    L = list(data)
    print("Original Data   : ", L)
    inserttionSort(L)
    print("Insertion Sorted Data: ", L)