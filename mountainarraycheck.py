array = [1,2,3,2,1]

def is_mountain_array(arr):
    # Check 1 - Array must be greater than 3
    if len(arr) < 3:
        return False

    i = 0
    n = len(arr)

    # Check 2 - Numbers must continuously rise until the peak
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
        print(i)

    # Check 3 - Peak cannot be at the start or end
    if i == 0 or i == n - 1:
        return False

    # Check 4 - Numbers must continuously fall from the peak
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
        print(i)

    return i == n - 1

print(is_mountain_array(array))