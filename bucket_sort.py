def bucket_sort(arr):
    max_val = max(arr)
    size = max_val / len(arr)
    buckets = [[] for _ in range(len(arr))]
    for i in arr:
        index = int(i / size)
        if index != len(arr):
            buckets[index].append(i)
        else:
            buckets[len(arr) - 1].append(i)
    for bucket in buckets:
        bucket.sort()
    return [i for bucket in buckets for i in bucket]

arr = [42, 32, 33, 52, 37, 47, 51]
print("Original array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
