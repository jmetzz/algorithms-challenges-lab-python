from typing import Tuple

from challenges.problems.leetcode import ListNode


class AddTwoNumbers:
    @classmethod
    def solve(cls, l1: ListNode, l2: ListNode) -> ListNode:
        value, carry = cls._sum(l1.val, l2.val, 0)
        output = ListNode(value)
        current = output
        p = l1.next
        q = l2.next
        while p is not None and q is not None:
            value, carry = cls._sum(p.val, q.val, carry)
            current.next = ListNode(value)
            current, p, q = cls._advance(current, p, q)
        carry, current = cls._add_carry_to_rest_of_the_list(carry, current, p)
        carry, current = cls._add_carry_to_rest_of_the_list(carry, current, q)
        if carry > 0:
            current.next = ListNode(carry)
        return output

    @classmethod
    def _add_carry_to_rest_of_the_list(cls, carry, current, p):
        while p is not None:
            value, carry = cls._sum(p.val, 0, carry)
            current.next = ListNode(value)
            current = current.next
            p = p.next
        return carry, current

    @classmethod
    def _advance(cls, current, p, q):
        current = current.next
        p = p.next
        q = q.next
        return current, p, q

    @staticmethod
    def _sum(v1: int, v2: int, carry: int) -> Tuple:
        value = v1 + v2 + carry
        c = 0
        if value > 9:
            c = value // 10
            value = value % 10
        return value, c


if __name__ == '__main__':
    l1 = ListNode.build_from([5, 4, 3, 6])
    l2 = ListNode.build_from([5, 6, 4])
    l3 = AddTwoNumbers.solve(l2, l1)
    output = l3.to_array()
    print(output)
