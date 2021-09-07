from builtins import range
def is_palindrome(head):
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.__next__, head
    while fast and fast.__next__:
        fast = fast.next.__next__
        slow = slow.__next__
    second = slow.__next__
    slow.next = None  # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.__next__
        second.next = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.__next__
        head = head.__next__
    return True


def is_palindrome_stack(head):
    if not head or not head.__next__:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.__next__:
        fast, slow = fast.next.__next__, slow.__next__

    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.__next__:
        slow = slow.__next__
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.__next__

    return True


def is_palindrome_dict(head):
    if not head or not head.__next__:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in list(d.keys()):
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.__next__
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in list(d.values()):
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
