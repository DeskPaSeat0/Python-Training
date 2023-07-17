def rev_string(text):
    string_queue = []

    for ch in text:
        string_queue.append(ch)

    res_string = ""

    while len(string_queue) >= 1:
        letter = string_queue.pop()
        res_string = res_string + letter

    return res_string

print(rev_string("Apple"))