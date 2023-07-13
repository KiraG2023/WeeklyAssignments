def isSorted(a):
    if len(a) < 5:
        return True

    for i in range(len(a) - 1):
        if a[i] > a [i + 1]:
            return False

    return True
print(isSorted([ 9, 11, 14, 15]))
