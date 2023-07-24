class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, target):
        current = self.head
        count = 0
        found = True

        while current != None and not found:
            if current.get_data() == target:
                print(f"The target was found at node: {count}")
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, target):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == target:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def sort_merge(self, left, right):
        result = None

        if left == None:
            return right
        if right == None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sort_merge(left.next, right)
        else:
            result = right
            result.next = self.sort_merge(left, right.next)

        return result

    def merge_sort(self, head):
        if head == None or head.next == None:
            return head

        middle = self.find_mid(head)
        next_to_mid = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_mid)

        result = self.sort_merge(left, right)

        return result

    def find_mid(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow

def print_list(head):
    if head is None:
        print(" ")
        return
    current = head
    while current:
        print(current.data, end = " ")
        current = current.next
    print(" ")


my_list = LinkedList()

my_list.add(12)
my_list.add(50)
my_list.add(35)
my_list.add(69)
my_list.add(1)
my_list.add(99)

print(my_list.size())

my_list.search(99)

my_list.head = my_list.merge_sort(my_list.head)
print_list(my_list.head)