def insertion_sort(A):
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        print(f"j: {j}, cur: {cur}")
        while j>0 and A[j-1] > cur:
            print(f"A: {A}")
            A[j] = A[j-1]
            j -= 1
            print(f"A: {A}, j {j}")
        A[j] = cur
    print(A)
insertion_sort([2,3423,1,323,54])