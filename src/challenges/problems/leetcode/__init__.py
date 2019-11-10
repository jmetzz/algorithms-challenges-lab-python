class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None

    def to_array(self):
        output = [self.val]
        node = self.next
        while node:
            output.append(node.val)
            node = node.next
        return output

    @staticmethod
    def build_from(elements):
        if len(elements) < 1:
            return None
        head = ListNode(elements[0])
        current = head
        for i in range(1, len(elements)):
            current.next = ListNode(elements[i])
            current = current.next
        return head
