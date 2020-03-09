def count_positives_sum_negatives(arr):
    a = [0, 0]
    for i in arr:
        if i > 0:
            a[0] = a[0] + 1
        if i < 0:
            a[1] = a[1] + int(i)
    if len(arr) == 0:
        a = []
    return a
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(arr))