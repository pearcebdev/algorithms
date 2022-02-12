def binary_array_search(A, target):
    lo = 0
    hi = len(A) - 1

    while lo <= hi:
        # find midpoint
        mid = (lo + hi) // 2
        # If target smaller, look left
        if target < A[mid]:
            hi = mid-1
        # else look right
        elif target > A[mid]:
            lo = mid+1
        else:
            # Found target
            return True

    return False


def binary_array_search_location(A, target):
    lo = 0
    hi = len(A) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target < A[mid]:
            hi = mid-1
        elif target > A[mid]:
            lo = mid+1
        else:
            return mid

    return -(lo+1)


def binary_array_search_single(A, target):
    lo = 0
    hi = len(A) - 1

    while lo <= hi:
        # find midpoint
        mid = (lo + hi) // 2
        # Calc diff between target and midpoint value
        diff = target - A[mid]
        # If diff smaller, look left
        if diff < 0:
            hi = mid-1
        elif diff > 0:
            lo = mid+1
        else:
            return mid

    return False
