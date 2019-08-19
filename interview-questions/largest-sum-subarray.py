def max_subarray(arr):
    max_ending = max_current = arr[0]

    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)

    return max_current

print(max_subarray([-4, -2, -3, -4, 5])) # 5

print(max_subarray([4, -5, -1, 0, -2, 20, -4, -3, -2, 8, -1, 10, -1, -1])) # 28