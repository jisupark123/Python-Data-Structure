"""
이진 탐색 트리 (Basic)


특징

1. 각 노드는 킷값을 하나씩 갖는다. 각 노드의 킷값은 모두 다르다.
2. 최상위 레벨에 루트 노드가 있고, 각 노드는 최대 2개의 자식 노드를 갖는다.
3. 임의 노드의 킷값은 자신의 왼쪽 아래에 있는 모든 노드의 킷값보다 크고, 오른쪽 아래에 있는 모든 노드의 킷값보다 작다.

--------------------------------------------------------------------------------------------------

검색(Search)

1. if 검색하는 값이 노드와 같다면 해당 노드 리턴
2. elif 검색하는 값이 None이면 None 리턴 (존재하지 않음)
3. elif 노드가 검색하는 값보다 크다면 왼쪽 자식 탐색(재귀)
4. else 오른쪽 자식 탐색(재귀)

시간복잡도 -> 평균 (logn), 최악(트리의 균형이 맞지 않을 때) O(n)

--------------------------------------------------------------------------------------------------

삽입(Insert)

원소 x를 이진 검색 트리에 삽입하려면 우선 이진 검색 트리에 x를 킷값으로 가진 노드가 없어야 한다.
원소 x를 삽입할 자리를 찾는 것은 실패하는 검색을 한 번 수행하는 것과 같다. (검색 시 None이 나오면 그곳에 삽입하면 된다.)

1. 검색 알고리즘으로 None값이 나올 때까지 검색 (만약 같은 값이 존재한다면 연산 종료)
2. None이 나온 자리에 x삽입

시간복잡도 -> 검색 알고리즘과 거의 같으므로 평균 (logn), 최악(트리의 균형이 맞지 않을 때) O(n)

--------------------------------------------------------------------------------------------------

삭제

1. 검색 알고리즘으로 삭제할 x값의 노드 위치 확인(만약 None이 나오면 삭제할 값이 없으므로 연산 종료)
2. if 삭제할 노드가 리프(마지막) 노드라면 -> 그냥 삭제하면 끝
3. elif 삭제할 노드의 자식이 하나뿐이라면 -> 삭제 후 삭제된 노드의 부모노드가 삭제된 노드의 자식노드를 가리키게 하면 끝
4. elif 삭제할 노드의 자식이 둘이라면 -> 왼쪽 서브트리에서 가장 큰 값 or 오른쪽 서브트리에서 가장 작은 값 중 하나가 삭제할 노드를 대체함

시간복잡도 -> 검색하는 시간 + case4에서 노드를 탐색하는 시간 평균(logn) or 최악 O(n) -> 평균 O(logn), 최악 O(n)

--------------------------------------------------------------------------------------------------

이진 검색 트리의 성능

삽입, 검색, 삭제 모두 평균(log n)의 시간복잡도를 가진다.
하지만 트리의 균형이 맞지 않으면 최악의 경우 검색에 O(n)의 시간이 소요될 수 있다.
"""


class Node:
    def __init__(self, new_item, left, right):
        self.item = new_item
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.__root = None
        self.__count = 0

    ## 같은 함수가 여러개인 이유
    ## 사용자는 매개변수로 찾고 싶은 값만 넣으면 된다.
    ## 하지만 재귀함수를 구현하려면 부모의 정보를 매개변수로 받아야 한다.

    # 검색
    def search(self, x) -> Node:
        return self.__search_item(self.__root, x)

    def __search_item(self, node: Node, x) -> Node:
        if node == None:
            return None
        elif x == node.item:
            return node
        elif x < node.item:
            return self.__search_item(node.left, x)
        else:
            return self.__search_item(node.right, x)

    # 삽입
    def insert(self, new_item):
        self.__root = self.__insert_item(self.__root, new_item)

    def __insert_item(self, node: Node, new_item) -> Node:
        if node == None:
            node = Node(new_item, None, None)
            self.__count += 1
        elif new_item < node.item:
            node.left = self.__insert_item(node.left, new_item)  # 왼쪽 가지
        elif new_item > node.item:
            node.right = self.__insert_item(node.right, new_item)  # 오른쪽 가지
        else:  # 중복되는 값 (x == node.item)
            print(f"{node.item}은(는) 중복되는 키이므로 insert 연산을 수행할 수 없습니다")
        return node

    # 삭제
    def delete(self, x):
        pre_cnt = self.__count
        self.__root = self.__delete_item(self.__root, x)
        if pre_cnt == self.__count:  # 이전 노드 개수랑 연산 후 노드 개수가 같으면
            print(f"{x}은(는) 존재하지 않는 키입니다!")

    def __delete_item(self, node: Node, x) -> Node:
        if node == None:  # item not found
            return None
        elif x == node.item:  # item found
            node = self.__delete_node(node)
            self.__count -= 1
        elif x < node.item:
            node.left = self.__delete_item(node.left, x)
        else:
            node.right = self.__delete_item(node.right, x)
        return node

    def __delete_node(self, node: Node) -> Node:
        if node.left == None and node.right == None:  # case 1(자식이 없음)
            return None
        elif node.left == None:  # case 2(오른쪽 자식만 있으면)
            return node.right
        elif node.right == None:  # case 2(왼쪽 자식만 있으면)
            return node.left
        else:  # case 3(두 자식 다 있으면)
            (item, r_node) = self.__delete_min_item(node.right)
            node.item = item
            node.right = r_node
            return node

    def __delete_min_item(self, node: Node) -> tuple:
        if node.left == None:  # 최솟값 노드를 찾음
            return (node.item, node.right)
        else:
            (item, r_node) = self.__delete_min_item(node.left)
            node.left = r_node
            return (item, node)

    # 빈 트리인지 확인
    def isEmpty(self) -> bool:
        return self.__root == None

    # 트리의 내용을 없앰
    def clear(self):
        self.__root = None

    # root를 반환
    def get_root(self):
        return self.__root

    # 노드의 개수를 반환
    def count(self):
        return self.__count


# 전위순회
def pre_order(node: Node):
    if node != None:
        print(node.item)
        pre_order(node.left)
        pre_order(node.right)


# 중위순회
def in_order(node: Node):
    if node != None:
        in_order(node.left)
        print(node.item)
        in_order(node.right)


# 후위순회
def post_order(node: Node):
    if node != None:
        post_order(node.left)
        post_order(node.right)
        print(node.item)


if __name__ == "__main__":
    tree = Tree()
    tree.insert(55)
    tree.insert(15)
    tree.insert(60)
    tree.insert(8)
    tree.insert(3)
    tree.insert(28)
    tree.insert(18)
    tree.insert(45)
    tree.insert(48)
    tree.insert(50)
    tree.insert(41)
    tree.insert(30)
    tree.insert(38)
    tree.insert(33)
    tree.insert(32)
    tree.insert(36)
    print(tree.count())
    tree.insert(36)
    print(tree.count())

    in_order(tree.get_root())

    # tree.delete(28)
    # print()
    # in_order(tree.get_root())
