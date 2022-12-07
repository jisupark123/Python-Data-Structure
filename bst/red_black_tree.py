from __future__ import annotations
from collections.abc import Iterator

"""
Red-Black Tree

특징

- 이진 탐색 트리(BST)의 한 종류
- 스스로 균형을 잡는 트리


속성(삽입이나 삭제가 끝난 후 별도의 작업을 통해 유지해야 하는 특징들)

1. 모든 노드는 Red 혹은 Black
2. 루트는 Black
3. 모든 nil노드는 Black (값이 있는 모든 노드는 자식 노드를 가지고 있음(nil))
4. Red가 연속으로 존재할 수 없다. (Red 노드 자식은 무조건 Black이다.)
5. 임의의 노드x에서의 black height은 모두 같다.
black height -> 노드x에서 임의의 자손 nil 노드까지 내려가는 경로에서의 black 수 (nil 노드는 Black으로 간주함)

삽입/삭제 시 주로 속성 4,5번을 위반하며 이것을 해결하려고 구조를 바꾸다보면 자연스럽게 트리의 균형이 잡히게 된다.

--------------------------------------------------------------------------------------------------

삽입(Insert)

삽입되는 노드의 색깔은 무조건 Red다.
만약 삽입된 Red 노드가 루트 노드라면 -> 블랙으로 바꾼다. (속성 2)
만약 삽입된 Red 노드의 부모 노드가 Black이라면 -> 끝
만약 삽입된 Red 노드의 부모 노드도 Red라면 -> Double Red(Restructuring/Recoloring 으로 해결)
Double Red를 해결하는 방법은 현재 insert된 노드의 Uncle Node(부모의 형제)의 색깔에 따라 달라진다.

만약 Uncle Node의 색깔이 Black 혹은 nil이라면 -> Restructuring
만약 Uncle Node의 색깔이 Red라면 -> Recoloring

--------------------------------------------------------------------------------------------------

Restructuring

# Case 1 (할아버지까지의 경로가 직진일 때)
삽입된 Red 노드가 부모의 왼쪽 자녀 && Red 부모도 할아버지의 왼쪽 자녀라면 (오른쪽, 오른쪽 자녀라면)
-> 부모와 할아버지의 색을 바꾼 후 할아버지 기준으로 오른쪽으로 회전한다. (왼쪽으로 회전한다)

# Case 2 (할아버지까지의 경로가 꺽여있을 때)
삽입된 Red 노드가 부모의 오른쪽 자녀 && Red 부모는 할아버지의 왼쪽 자녀라면 (왼쪽, 오른쪽 자녀라면)
-> 부모의 기준으로 왼쪽으로 회전한 뒤 Case 1의 방식으로 해결한다. (오른쪽으로 회전한다)

Restructuring의 시간복잡도

다른 서브트리에 영향을 끼치지 않기 때문에 한번의 Restructuring이면 끝난다.
(Double Red를 해결하기 전과 해결 한 후의 Black 노드의 개수에 변화가 없기 때문에)
또한, Restructuring자체의 시간복잡도는 O(1)에 끝나지만
Restructuring은 어떤 노드를 insertion한 뒤 일어나므로 총 수행시간은 O(logN)이다.
지금 현재 노드가 들어갈 위치를 먼저 찾아야 하기 때문이다.

--------------------------------------------------------------------------------------------------

Recoloring

1. Insert된 노드의 부모 노드, 그 형제 노드(Insert된 노드의 Uncle Node)를 Black으로 만든다.
2. Insert된 노드의 Grand Parant를 Red로 만든다.
3. if Grand Parant가 루트 노드였다면 -> Grand Parant를 Black으로 만든다.
4. elif Grand Parant의 부모가 Red라면 -> 다시 Restructuring or Recoloring


Recoloring의 시간복잡도

Recoloring으로 Red-Black Tree의 특징 4번
(루트 노드에서 임의의 리프노드에 이르는 경로에서 만나는 Black 노드의 수는 모두 같다.)의 규칙이 깨지진 않는다. 
하지만 Recoloring이 끝난 뒤 운이 안 좋으면 루트 노드까지 propagation될 수 있다.

즉 Insert하는데 걸리는 시간 O(logN) + Root까지 propagation 되면 걸리는 시간 O(logN) = O(logN)


따라서 Restructuring, Recoloring 모두 O(logN)
따라서 삽입(Insert)의 성능은 O(logN)


--------------------------------------------------------------------------------------------------

삭제(Delete)

주요 용어
successor -> 해당 노드보다 값이 큰 노드들 중에서 가장 값이 작은 노드
predecessor -> 해당 노드보다 값이 작은 노드들 중에서 가장 값이 큰 노드

0. 삭제 전의 트리는 RB트리 속성을 만족한 상태이다
1. 삭제 방식은 일반적인 BST와 동일하다
2. 삭제 후 RB트리 속성 위반 여부를 확인 -> 삭재되는 색을 통해 속성 위반 여부를 판단한다.
-- 삭제되는 노드의 자녀가 없거나 하나라면 삭제되는 색은 삭제되는 노드의 색
-- 삭제되는 노드의 자녀가 둘이라면 삭제되는 색은 삭제되는 노드의 successor의 색 (successor은 삭제되는 노드의 색을 물려받는다)
3. RB트리 속성을 위반했다면 재조정한다
-- 삭제되는 색이 Red라면 어떠한 속성도 위반하지 않는다
-- 삭제되는 색이 Black이라면 속성 2,3,4번을 위반할 수 있다 
-> 5번 속성은 거의 모든 상황에서 위반한다 (임의의 노드x에서의 black height은 모두 같다.)(RB트리에서의 삭제의 핵심)

# 삭제되는 색이 Black && 속성 2번(루트는 Black)을 위반했을 때 
루트를 Black으로 바꿔준다

# 삭제되는 색이 Black && 속성 5번(임의의 노드x에서의 black height은 모두 같다)을 위반했을 때 
1. 속성 5번을 만족시키기 위해 삭제된 색의 위치를 대체한 노드에 extra black을 부여한다 (삭제된 색의 위치는 삭제되는 노드 or 삭제되는 노드의 successor)
-> 경로에서 black 수를 카운트할 때 extra black은 하나의 black으로 카운트된다
-> extra black이 부여된 red 노드를 red-and-black 이라고 함
-> extra black이 부여된 black 노드를 doubly black 이라고 함 (nil 포함)
-> extra black을 부여받은 노드는 red-and-black or doubly black 이 된다

2. # red-and-black 해결하기
- red-and-black을 black으로 바꾸면 해결된다
-> 속성 4,5번을 동시에 해결한다

3. # doubly black 해결하기 
(extra black을 어떻게 없앨 것인지가 관건)
(doubly black의 형제의 색과 그 형제의 자녀들에 색에 따라 4가지 Case로 구분된다)

Case 1 -> doubly black의 오른쪽 형제가 Black && 그 형제의 오른쪽 자녀가 Red일 때 
-- 1. 오른쪽 형제는 부모의 색으로 바꾼다                                       
-- 2. 오른쪽 형제의 오른쪽 자녀는 Black으로 바꾼다
-- 3. 부모를 Black으로 바꾼 후에 부모를 기준으로 왼쪽으로 회전한다 
-- (오른쪽, 왼쪽을 바꿔도 성립한다)

Case 2 -> doubly black의 오른쪽 형제가 Black && 그 형제의 왼쪽 자녀가 Red && 그 형제 오른쪽 자녀가 Black일 때
-- (doubly black의 오른쪽 자녀를 red가 되게 만들어서 Case1의 방법을 통해 해결한다)
-- 1. doubly black의 오른쪽 형제와 그 형제의 왼쪽 Red 자녀의 색을 바꾼다
-- 2. doubly black의 오른쪽 형제를 기준으로 오른쪽 회전한다 (이제 형제의 오른쪽 자녀가 Red가 되었다)
-- 3. Case 1을 적용해서 해결한다
-- (오른쪽, 왼쪽을 바꿔도 성립한다)

Case 3 -> doubly black의 형제가 Black && 그 형제의 두 자녀 모두 Black일 때
-- (doubly black과 그 형제의 black을 모아서 부모에게 전달 -> 부모가 extra black을 해결하도록 위임한다)
-- 1. doubly black은 Black이 된다
-- 2. doubly black의 형제는 Red가 된다 (black을 부모에게 넘겼기 때문에)
-- 3. extra black(1개)을 전달받은 부모가 red-and-black이면 Black으로 바꾸고 끝
-- 4. 만약 extra black(1개)을 전달받은 부모가 doubly black이면 부모부터 Case 1~4중 하나로 해결한다(재귀적)

Case 4 -> doubly black의 형제가 Red일 때
-- (doubly black의 형제를 Black으로 만든 후에 Case 1~3 중 하나로 해결한다)
-- 1. doubly black의 부모와 형제의 색을 바꾼다
-- 2. 부모를 기준으로 왼쪽으로 회전한다
-- 3. doubly black을 기준으로 Case 1~3 중 하나로 해결한다
-- (오른쪽, 왼쪽을 바꿔도 성립한다)


Delete의 시간복잡도
노드를 찾는데 걸리는 시간 O(logN) + 5번 속성을 유지하는데 걸리는 시간 O(logN) = O(logN)

--------------------------------------------------------------------------------------------------

Red-Black Tree의 성능

검색, 삽입, 삭제 모두 O(logN)의 시간에 일어나는 효율적인 자료구조

---------------------------------------------------------------------------------------------------

AVL 트리와의 비교

삽입, 삭제 성능이 AVL트리보다 빠르고 검색 성능이 AVL트리보다 느리다 (AVL 트리가 균형을 더 철저하게 잡기 때문)
하지만 검색 성능은 거의 차이가 나지 않고 삽입/삭제를 할 일이 많기 때문에 웬만하면 Red-Black 트리를 사용한다.

---------------------------------------------------------------------------------------------------

Red-Black Tree의 응용 사례

linux kernel 내부
Java의 TreeMap
c++ std::map 구현, etc 등등
"""


# class Node:
#     def __init__(self, item):
#         self.RED = 1
#         self.BLACK = 2
#         self.item = item
#         self.color = self.RED

#         self.left = None
#         self.rigth = None
#         self.parent = None

#     def __str__(self):
#         return self.key


# class RedBlackTree:
#     def __init__(self):
#         self.__root = None

"""
python/black : true
flake8 : passed
"""


class RedBlackTree:
    def __init__(
        self,
        label: int | None = None,
        color: int = 0,
        parent: RedBlackTree | None = None,
        left: RedBlackTree | None = None,
        right: RedBlackTree | None = None,
    ) -> None:
        """Initialize a new Red-Black Tree node with the given values:
        label: The value associated with this node
        color: 0 if black, 1 if red
        parent: The parent to this node
        left: This node's left child
        right: This node's right child
        """
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    # Here are functions which are specific to red-black trees

    def rotate_left(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the left and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).
        """
        parent = self.parent
        right = self.right
        if right is None:
            return self
        self.right = right.left
        if self.right:
            self.right.parent = self
        self.parent = right
        right.left = self
        if parent is not None:
            if parent.left == self:
                parent.left = right
            else:
                parent.right = right
        right.parent = parent
        return right

    def rotate_right(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the right and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).
        """
        if self.left is None:
            return self
        parent = self.parent
        left = self.left
        self.left = left.right
        if self.left:
            self.left.parent = self
        self.parent = left
        left.right = self
        if parent is not None:
            if parent.right is self:
                parent.right = left
            else:
                parent.left = left
        left.parent = parent
        return left

    def insert(self, label: int) -> RedBlackTree:
        """Inserts label into the subtree rooted at self, performs any
        rotations necessary to maintain balance, and then returns the
        new root to this subtree (likely self).
        This is guaranteed to run in O(log(n)) time.
        """
        if self.label is None:
            # Only possible with an empty tree
            self.label = label
            return self
        if self.label == label:
            return self
        elif self.label > label:
            if self.left:
                self.left.insert(label)
            else:
                self.left = RedBlackTree(label, 1, self)
                self.left._insert_repair()
        else:
            if self.right:
                self.right.insert(label)
            else:
                self.right = RedBlackTree(label, 1, self)
                self.right._insert_repair()
        return self.parent or self

    def _insert_repair(self) -> None:
        """Repair the coloring from inserting into a tree."""
        if self.parent is None:
            # This node is the root, so it just needs to be black
            self.color = 0
        elif color(self.parent) == 0:
            # If the parent is black, then it just needs to be red
            self.color = 1
        else:
            uncle = self.parent.sibling
            if color(uncle) == 0:
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    if self.right:
                        self.right._insert_repair()
                elif self.is_right() and self.parent.is_left():
                    self.parent.rotate_left()
                    if self.left:
                        self.left._insert_repair()
                elif self.is_left():
                    if self.grandparent:
                        self.grandparent.rotate_right()
                        self.parent.color = 0
                    if self.parent.right:
                        self.parent.right.color = 1
                else:
                    if self.grandparent:
                        self.grandparent.rotate_left()
                        self.parent.color = 0
                    if self.parent.left:
                        self.parent.left.color = 1
            else:
                self.parent.color = 0
                if uncle and self.grandparent:
                    uncle.color = 0
                    self.grandparent.color = 1
                    self.grandparent._insert_repair()

    def remove(self, label: int) -> RedBlackTree:
        """Remove label from this tree."""
        if self.label == label:
            if self.left and self.right:
                # It's easier to balance a node with at most one child,
                # so we replace this node with the greatest one less than
                # it and remove that.
                value = self.left.get_max()
                if value is not None:
                    self.label = value
                    self.left.remove(value)
            else:
                # This node has at most one non-None child, so we don't
                # need to replace
                child = self.left or self.right
                if self.color == 1:
                    # This node is red, and its child is black
                    # The only way this happens to a node with one child
                    # is if both children are None leaves.
                    # We can just remove this node and call it a day.
                    if self.parent:
                        if self.is_left():
                            self.parent.left = None
                        else:
                            self.parent.right = None
                else:
                    # The node is black
                    if child is None:
                        # This node and its child are black
                        if self.parent is None:
                            # The tree is now empty
                            return RedBlackTree(None)
                        else:
                            self._remove_repair()
                            if self.is_left():
                                self.parent.left = None
                            else:
                                self.parent.right = None
                            self.parent = None
                    else:
                        # This node is black and its child is red
                        # Move the child node here and make it black
                        self.label = child.label
                        self.left = child.left
                        self.right = child.right
                        if self.left:
                            self.left.parent = self
                        if self.right:
                            self.right.parent = self
        elif self.label is not None and self.label > label:
            if self.left:
                self.left.remove(label)
        else:
            if self.right:
                self.right.remove(label)
        return self.parent or self

    def _remove_repair(self) -> None:
        """Repair the coloring of the tree that may have been messed up."""
        if (
            self.parent is None
            or self.sibling is None
            or self.parent.sibling is None
            or self.grandparent is None
        ):
            return
        if color(self.sibling) == 1:
            self.sibling.color = 0
            self.parent.color = 1
            if self.is_left():
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
        if (
            color(self.parent) == 0
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent._remove_repair()
            return
        if (
            color(self.parent) == 1
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent.color = 0
            return
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 0
            and color(self.sibling.left) == 1
        ):
            self.sibling.rotate_right()
            self.sibling.color = 0
            if self.sibling.right:
                self.sibling.right.color = 1
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
            and color(self.sibling.left) == 0
        ):
            self.sibling.rotate_left()
            self.sibling.color = 0
            if self.sibling.left:
                self.sibling.left.color = 1
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
        ):
            self.parent.rotate_left()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.left) == 1
        ):
            self.parent.rotate_right()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0

    def check_color_properties(self) -> bool:
        """Check the coloring of the tree, and return True iff the tree
        is colored in a way which matches these five properties:
        (wording stolen from wikipedia article)
         1. Each node is either red or black.
         2. The root node is black.
         3. All leaves are black.
         4. If a node is red, then both its children are black.
         5. Every path from any node to all of its descendent NIL nodes
            has the same number of black nodes.
        This function runs in O(n) time, because properties 4 and 5 take
        that long to check.
        """
        # I assume property 1 to hold because there is nothing that can
        # make the color be anything other than 0 or 1.
        # Property 2
        if self.color:
            # The root was red
            print("Property 2")
            return False
        # Property 3 does not need to be checked, because None is assumed
        # to be black and is all the leaves.
        # Property 4
        if not self.check_coloring():
            print("Property 4")
            return False
        # Property 5
        if self.black_height() is None:
            print("Property 5")
            return False
        # All properties were met
        return True

    def check_coloring(self) -> bool:
        """A helper function to recursively check Property 4 of a
        Red-Black Tree. See check_color_properties for more info.
        """
        if self.color == 1:
            if color(self.left) == 1 or color(self.right) == 1:
                return False
        if self.left and not self.left.check_coloring():
            return False
        if self.right and not self.right.check_coloring():
            return False
        return True

    def black_height(self) -> int | None:
        """Returns the number of black nodes from this node to the
        leaves of the tree, or None if there isn't one such value (the
        tree is color incorrectly).
        """
        if self is None or self.left is None or self.right is None:
            # If we're already at a leaf, there is no path
            return 1
        left = RedBlackTree.black_height(self.left)
        right = RedBlackTree.black_height(self.right)
        if left is None or right is None:
            # There are issues with coloring below children nodes
            return None
        if left != right:
            # The two children have unequal depths
            return None
        # Return the black depth of children, plus one if this node is
        # black
        return left + (1 - self.color)

    # Here are functions which are general to all binary search trees

    def __contains__(self, label: int) -> bool:
        """Search through the tree for label, returning True iff it is
        found somewhere in the tree.
        Guaranteed to run in O(log(n)) time.
        """
        return self.search(label) is not None

    def search(self, label: int) -> RedBlackTree | None:
        """Search through the tree for label, returning its node if
        it's found, and None otherwise.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self
        elif self.label is not None and label > self.label:
            if self.right is None:
                return None
            else:
                return self.right.search(label)
        else:
            if self.left is None:
                return None
            else:
                return self.left.search(label)

    def floor(self, label: int) -> int | None:
        """Returns the largest element in this tree which is at most label.
        This method is guaranteed to run in O(log(n)) time."""
        if self.label == label:
            return self.label
        elif self.label is not None and self.label > label:
            if self.left:
                return self.left.floor(label)
            else:
                return None
        else:
            if self.right:
                attempt = self.right.floor(label)
                if attempt is not None:
                    return attempt
            return self.label

    def ceil(self, label: int) -> int | None:
        """Returns the smallest element in this tree which is at least label.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.label == label:
            return self.label
        elif self.label is not None and self.label < label:
            if self.right:
                return self.right.ceil(label)
            else:
                return None
        else:
            if self.left:
                attempt = self.left.ceil(label)
                if attempt is not None:
                    return attempt
            return self.label

    def get_max(self) -> int | None:
        """Returns the largest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.right:
            # Go as far right as possible
            return self.right.get_max()
        else:
            return self.label

    def get_min(self) -> int | None:
        """Returns the smallest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        if self.left:
            # Go as far left as possible
            return self.left.get_min()
        else:
            return self.label

    @property
    def grandparent(self) -> RedBlackTree | None:
        """Get the current node's grandparent, or None if it doesn't exist."""
        if self.parent is None:
            return None
        else:
            return self.parent.parent

    @property
    def sibling(self) -> RedBlackTree | None:
        """Get the current node's sibling, or None if it doesn't exist."""
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left

    def is_left(self) -> bool:
        """Returns true iff this node is the left child of its parent."""
        if self.parent is None:
            return False
        return self.parent.left is self.parent.left is self

    def is_right(self) -> bool:
        """Returns true iff this node is the right child of its parent."""
        if self.parent is None:
            return False
        return self.parent.right is self

    def __bool__(self) -> bool:
        return True

    def __len__(self) -> int:
        """
        Return the number of nodes in this tree.
        """
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        return ln

    def preorder_traverse(self) -> Iterator[int | None]:
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()

    def inorder_traverse(self) -> Iterator[int | None]:
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()

    def postorder_traverse(self) -> Iterator[int | None]:
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label

    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return f"'{self.label} {(self.color and 'red') or 'blk'}'"
        return pformat(
            {
                f"{self.label} {(self.color and 'red') or 'blk'}": (
                    self.left,
                    self.right,
                )
            },
            indent=1,
        )

    def __eq__(self, other: object) -> bool:
        """Test if two trees are equal."""
        if not isinstance(other, RedBlackTree):
            return NotImplemented
        if self.label == other.label:
            return self.left == other.left and self.right == other.right
        else:
            return False


def color(node: RedBlackTree | None) -> int:
    """Returns the color of a node, allowing for None leaves."""
    if node is None:
        return 0
    else:
        return node.color


if __name__ == "__main__":
    a = RedBlackTree(0)
    a = a.insert(-16)
    a.insert(16)
    a.insert(8)
    a.insert(24)
    a.insert(20)
    a.insert(22)

    print(list(a.inorder_traverse()))
