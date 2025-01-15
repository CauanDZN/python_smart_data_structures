def heapsort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

unsorted_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Array antes de ordenar:", unsorted_array)

sorted_array = heapsort(unsorted_array[:])
print("Array após ordenar:", sorted_array)
