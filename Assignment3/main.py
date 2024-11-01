def count_sort(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Create a count array to store frequencies
    count = [0] * (max_val - min_val + 1)

    # Count the frequencies of elements
    for num in arr:
        count[num - min_val] += 1

    # Modify the count array to store cumulative frequencies
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create an output array
    output = [0] * len(arr)

    # Place the elements in the output array based on count
    for num in arr:
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Example usage:
arr =  [2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2]

sorted_arr = count_sort(arr)
print(sorted_arr)


