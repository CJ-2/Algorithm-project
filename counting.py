def counting_sort(data):

    # Find the maximum value in the data
    max_v = max(data)
    

    # Create a count array to store the frequency of each value
    count_array = [0] * (max_v[0] + 1)
    for value in data:
        count_array[value[0]] += 1

    # Calculate the cumulative sum of the count array
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    # Create a new list to store the sorted data
    sorted_data = [0] * len(data)

    # Place each element in its correct position based on the count array
    for value in reversed(data):
        sorted_data[count_array[value[0]] - 1] = value
        count_array[value[0]] -= 1

    return sorted_data
