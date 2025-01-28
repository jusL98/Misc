list = [3,1,2,3,2,1]


def is_mountain_array(list):
    check_list = list.copy()
    check_list.pop(0)

    for index, num in enumerate(check_list):
        num1 = list[index]
        num2 = num

        if num1 < num2:
            print("up")

        elif num1 == num2:
            print("same")

        elif num1 > num2:
            print("down")

        print(f"Num1: {num1}")
        print(f"Num2: {num2}")
        print()
        

#print(list)
is_mountain_array(list)

"""if len(array) >= 3:
    print(True)
else:
    print(False)"""