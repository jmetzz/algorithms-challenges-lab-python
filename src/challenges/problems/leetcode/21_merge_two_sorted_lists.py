from typing import List

from challenges.problems.leetcode import ListNode


class MergeTwoOrderedLists:
    def solve(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None
        elif l1 and l2:
            p = l1
            q = l2
            if p.val <= q.val:
                value = p.val
                p = p.next
            else:
                value = q.val
                q = q.next
            head = ListNode(value)
            current = head
            while p and q:
                if p.val <= q.val:
                    value = p.val
                    p = p.next
                else:
                    value = q.val
                    q = q.next
                current.next = ListNode(value)
                current = current.next
        elif l1:
            p = l1
            head = ListNode(p.val)
            current = head
            p = p.next
            q = None
        else:
            q = l2
            head = ListNode(q.val)
            current = head
            q = q.next
            p = None
        while p:
            current.next = ListNode(p.val)
            current = current.next
            p = p.next
        while q:
            current.next = ListNode(q.val)
            current = current.next
            q = q.next
        return head


if __name__ == '__main__':
    l1 = ListNode.build_from([1, 2, 4])
    l2 = ListNode.build_from([1, 3, 4, 5])
    l3 = MergeTwoOrderedLists().solve(l1, l2)
    output = l3.to_array() if l3 else []
    print(output)
