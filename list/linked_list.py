"""
단순 연결 리스트 (Basic)

각각의 원소가 노드들로 구성된다.
각 노드는 다음 노드를 가리키는 필드를 가진다.
내장 리스트와 다르게 공간의 제약이 없음
이전 노드에 대한 정보가 없으므로 append 연산에 O(n)의 시간이 걸린다.

접근 - O(n)
검색 - O(n)
삭제 - O(n)
맨앞에 원소 추가(insert(0)) - O(1)
그 밖의 원소 추가 - O(n)
"""


class Node:
    def __init__(self, new_item, next_node: "Node"):
        self.item = new_item
        self.next = next_node


class List:
    def __init__(self):
        self.__head = Node("dummy", None)  # head에  가짜노드
        self.__cnt = 0  # 노드의 개수

    # i번째 인덱스에 원소 삽입
    def insert(self, i: int, new_item):
        if i >= 0 and i <= self.__cnt:  # Item이 3개 있으면 0,1,2,3 까지 허용
            prev = self.__get_node(i - 1)
            new_node = Node(new_item, prev.next)
            prev.next = new_node
            self.__cnt += 1
        else:
            raise IndexError("list index out of range")

    # 리스트 끝에 원소 삽입
    def append(self, new_item):
        prev = self.__get_node(self.__cnt - 1)
        new_node = Node(new_item, prev.next)
        prev.next = new_node
        self.__cnt += 1

    # 매개변수가 없거나 -1이면 맨 끝 원소 삭제 & 반환
    # 매개변수가 주어지면 해당 인덱스 원소 삭제 & 반환
    def pop(self, *args) -> Node:
        if self.is_empty():  # 리스트가 비었는지 확인
            raise IndexError("pop from empty list")
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:  # 매개변수가 없거나 -1이면 맨 끝 원소 삭제 & 반환
            i = self.__cnt - 1
        if i >= 0 and i < self.__cnt:
            prev = self.__get_node(i - 1)
            target = prev.next
            prev.next = target.next
            self.__cnt -= 1
            return target.item
        else:
            raise IndexError("list assignment index out of range")

    # 가장 먼저 나오는 x 삭제
    def remove(self, x):
        (prev, target) = self.__find_node(x)
        if target != None:
            prev.next = target.next
            self.__cnt -= 1
        else:
            raise ValueError(f"list.remove(x): {x} not in list")

    # i 번째 원소 알려주기
    def get(self, i: int):
        if self.is_empty():
            return None
        if i >= 0 and i < self.__cnt:
            return self.__get_node(i).item

    def index(self, x) -> int:
        node = self.__head.next  # 0번 노드
        for i in range(self.__cnt):
            if node.item == x:
                return i
            else:
                node = node.next

        return -1  # 없으면 -1 반환

    def is_empty(self) -> bool:
        return self.__cnt == 0

    def size(self) -> int:
        return self.__cnt

    def clear(self):
        self.__head == Node("dummy", None)
        self.__cnt = 0

    def count(self, x) -> int:
        res = 0
        node = self.__head.next
        for _ in range(self.__cnt):
            if node.item == x:
                res += 1
            node = node.next

        return res

    def extend(self, arr: "List"):
        for i in range(arr.size()):
            self.append(arr.get(i))

    def copy(self):
        res = List()
        for i in range(self.__cnt):
            res.append(self.get(i))
        return res

    def reverse(self):
        a = List()
        for i in range(self.__cnt):
            a.insert(0, self.get(i))
        self.clear()
        for i in range(a.size()):
            self.append(a.get(i))

    def sort(self) -> None:
        a = []
        for i in range(self.__cnt):
            a.append(self.get(i))
        a.sort()
        self.clear()
        for i in range(len(a)):
            self.append(a[i])

    def __get_node(self, i: int) -> Node:
        node = self.__head
        for _ in range(i + 1):
            node = node.next
        return node

    def __find_node(self, x):
        prev = self.__head  # 가짜 헤드
        target = prev.next  # 0번 노드
        while target != None:
            if target.item == x:
                return (prev, target)
            else:
                prev, target = target, target.next
        return (None, None)

    def __str__(self):
        res = ""
        node = self.__head.next
        for _ in range(self.__cnt):
            res += f"{node.item}, "
            node = node.next

        return f"[{res[:-2]}]"


if __name__ == "__main__":

    a = List()
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(3)
    a.append(3)

    print(a.pop())
    print(a)
