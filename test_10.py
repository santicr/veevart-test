def merge(A, lo, mid, hi):
    l1 = mid - lo + 1
    l2 = hi - mid

    l = [A[lo + i] for i in range(l1)]
    r = [A[mid + 1 + i] for i in range(l2)]

    i, j, k = 0, 0, lo
    while i < l1 and j < l2:
        if l[i] <= r[j]:
            A[k] = l[i]
            i += 1
        else:
            A[k] = r[j]
            j += 1
        k += 1

    while i < l1:
        A[k] = l[i]
        k += 1
        i += 1

    while j < l2:
        A[k] = r[j]
        k += 1
        j += 1
        
def sort(A, lo, hi):
    if lo < hi:
        mid = (lo + hi) // 2
        sort(A, lo, mid)
        sort(A, mid + 1, hi)
        merge(A, lo, mid, hi)

def main():
    A = [1, 0, 9, 23, -2]
    sort(A, 0, len(A) - 1)
    print(A)

main()