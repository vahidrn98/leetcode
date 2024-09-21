
def hashSort(arr):
    # create a 2D array with size of arr
    maxi = max(arr)
    hash_table = [[] for _ in range(maxi+1)]

    # insert each element in the array into the corresponding bucket
    for num in arr:
        hash_table[num].append(num)
    
    # sort the elements in each bucket
    sorted_arr = []
    for bucket in hash_table:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# test the function

arr = [5, 2, 8, 1, 3, 6, 4, 7]
sorted_arr = hashSort(arr)
print(sorted_arr)
