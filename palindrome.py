from collections import deque

def palindrome_checker(stringnum):
    char_deque = deque()

    for ch in str(stringnum):
        char_deque.append(ch)

    still_equal = True

    while len(char_deque) > 1 and still_equal:
        first = char_deque.popleft()
        last = char_deque.pop()

        if first != last:
            still_equal = False

    return still_equal

print(palindrome_checker("12321"))