array = [1,2,3,4,5]
target = 2

def rotate_away(arr,num):
    stack = []

    try:
        num_index = arr.index(num)
    except ValueError:
        return 'TARGET NOT IN LIST'

    while num_index >= 1:
        num_index-=1
        stack.append(arr[num_index])
        arr.pop(num_index)
    
    stack.reverse()

    [arr.append(val) for val in stack]
    return arr


print(rotate_away(array,target))