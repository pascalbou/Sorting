# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    while arrA and arrB:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
        else:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])

    while arrA:
        merged_arr.append(arrA[0])
        arrA.remove(arrA[0])

    while arrB:
        merged_arr.append(arrB[0])
        arrB.remove(arrB[0])      

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    n = len(arr) - 1
    if n == 1:
        return arr

    arrayOne = [n for n in arr[:int(n/2)]]
    arrayTwo = [n for n in arr[int(n/2+1):]]

    arrayOne = merge_sort(arrayOne)
    arrayTwo = merge_sort(arrayTwo)

    arr = merge(arrayOne, arrayTwo)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
