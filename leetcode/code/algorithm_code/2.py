'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        flag = 0
        while flag>0 or l1 or l2:
            sum = flag
            sum += l1.val if l1 else 0
            sum += l2.val if l2 else 0
            flag = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return head.next


if __name__ == '__main__':
    def creat(num):
        List = [ListNode(int(i)) for i in str(num)[::-1]]
        for i in range(len(List)-1):
            List[i].next = List[i+1]
        return List[0]

    node1 = creat(123)
    node2 = creat(123)

    node = Solution().addTwoNumbers(node1,node2)
    while node:
        print(node.val)
        node=node.next