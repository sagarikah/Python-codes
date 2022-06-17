# Binary Search using Recursion




def binary_search(list, low, high, item):

    if low <= high:
        mid = (low + high)//2

        if list[mid] == item:
            print(item, " is at position ", mid+1)
            return

        elif list[mid] > item:
            binary_search(list, low, mid-1, item)

        else:
            binary_search(list, mid+1, high, item)

    else:
        print(item, " not found")
        return 



list = [10,12,15,18,20,22,28,35]
size = len(list) - 1

binary_search(list, 0, size, 350)
