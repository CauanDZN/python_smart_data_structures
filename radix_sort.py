def radix_sort(arr):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1
    while not max_length:
        max_length = True
        buckets = [[] for _ in range(RADIX)]
        for i in arr:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr

unsorted_array = [170, 45, 75, 90, 802, 24, 2, 66]
print("Array antes de ordenar:", unsorted_array)
sorted_array = radix_sort(unsorted_array)
print("Array após ordenar:", sorted_array)