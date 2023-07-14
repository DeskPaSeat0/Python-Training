def binarySearch(data, bot, top, number):

    if top >= bot:
        mid = (top + bot) // 2

        if data[mid] == number:
            return mid
        elif data[mid] > number:
            return binarySearch(data, bot, mid-1, number)
        else:
            return binarySearch(data, mid+1, top, number)
    else:
        return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chosen = int(input("Enter number to search: "))

print(binarySearch(data, 0, len(data)-1, chosen))