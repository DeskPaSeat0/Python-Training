def linearSearch(number, data):
    for x in range(0, len(data)-1):
        if data[x] == number:
            return x
    
    return -1

data = [32, 18, 24, 9, 64, 128, 69, 18, 4, 3]

chosen = int(input("Enter number to search: "))

print(linearSearch(chosen, data))