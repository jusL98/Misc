array = [1,3,2,3,4,5,6,6,6]

def next_greater_element(arr):
    stack = []
    nge = {}
    for i in range(len(arr)):
        while stack and arr[i] > stack[-1]:
            nge[stack.pop()] = arr[i]
        stack.append(arr[i])
    while stack:
        nge[stack.pop()] = -1
    return nge

nge = next_greater_element(array)

for key, value in nge.items():
    print(f'{key} -> {value}')