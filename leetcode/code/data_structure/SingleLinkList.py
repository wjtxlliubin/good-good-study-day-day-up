class Node():
    def __init__(self, item):
        self.data = item
        self.next = None


class SingleLinkList():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count

    def items(self):
        current = self._head
        while current is not None:
            yield current.data
            # 指针下移
            current = current.next

    def add(self, item):
        self._head = Node(item)

    def append(self, item):
        if self.is_empty():
            self.add(item)
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = Node(item)

    def insert(self, index, item):
        '''
        插入元素
        :param index:
        :param item:
        :return:
        '''
        if index<=0 :
            self.add(item)
        elif index > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            current = self._head
            pre = None
            while current is not None and count!=index:
                pre = current
                current = current.next
                count += 1
            pre.next = Node(item)
            pre.next.next = current

    def remove(self, item):
        current = self._head
        pre = None
        while current is not None:
            # 找到指定元素
            if current.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = current.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = current.next
                return True
            else:
                # 继续按链表后移节点
                pre = current
                current = current.next

    def find(self, item):
        return item in self.items()

if __name__ == '__main__':

    singlelinklist = SingleLinkList()
    singlelinklist.add(0)
    singlelinklist.append(1)
    singlelinklist.append(3)
    singlelinklist.insert(2,2)
    # print(singlelinklist.length())
    for i in singlelinklist.items():
        print(i)


