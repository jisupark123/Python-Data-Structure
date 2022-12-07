# data-structure

# 파이썬을 이용한 자료구조

# 🧩 목차

**리스트 (List)**

1. 파이썬 내장 리스트
2. 단순 연결 리스트
3. 원형 연결 리스트
4. 이중 연결 리스트

**스택 (Stack)**

1. 내장 리스트 스택 (내장 리스트 사용)
2. 연결 리스트 스택 (단순 연결 리스트 사용)

**큐 (Queue)**

1. 내장 리스트 큐 (내장 리스트 사용)
2. 연결 리스트 큐 (원형 연결 리스트 사용)
3. 양방향 큐(이중 연결 리스트 사용)

**힙 (Heap)**

1. 최대 힙
2. 최소 힙

**이진 탐색 트리 (Binary Search Tree)**

1. 기본 이진 탐색 트리
2. AVL 탐색 트리

</br>

# 🧩 리스트 (List)

</br>

### 리스트(List)의 특징

- 여러 자료가 일직선으로 연결된 선형 자료구조
- Stack, Queue, Tree, Graph 등과 같은 다른 자료구조 구현에 활용되는 기초 자료구조

</br>

## 📌 파이썬 내장 리스트

### 특징

- 파이썬에 기본으로 내장되어있는 리스트

### 장점

- 사용이 간편하다.

### 단점

- 공간이 한정되어 있는 자료구조로 리스트가 커지거나 줄어들수록 시스템 내부에서 리스트의 크기를 계속 변경해줘야 한다.
- 메모리 주소의 순서를 사용하기 때문에 접근할 때 O(1)의 속도를 보여준다.

### 소요시간

- 접근 - O(1)
- 검색 - O(n) (정렬 시 O(log<sub>n</sub>))
- 삭제 - O(n)

[코드](https://github.com/jisupark123/data-structure/blob/main/list/ArrayList/lst.py)

</br>
</br>

## 📌 단순 연결 리스트

### 특징

- 각각의 원소가 노드들로 구성된다.
- 각 노드는 다음 노드를 가리키는 필드를 가진다.
- 삭제 연산 자체는 O(1)이지만 접근에 O(n)이 걸린다. 따라서 삭제도 O(n)이다.

### 장점

- 내장 리스트와 다르게 공간의 제약이 없다.

### 단점

- 이전 노드에 대한 정보가 없으므로 append() 연산에 O(n)의 시간이 걸린다.
  (다음 노드 대신 이전 노드를 저장하면 insert(0) 연산에 취약해진다)

### 소요시간

- 접근 - O(n)
- 검색 - O(n)
- 삭제 - O(n)
- 맨앞에 원소 추가(insert(0)) - O(1)
- 그 밖의 원소 추가 - O(n)

[코드](https://github.com/jisupark123/data-structure/tree/main/list/LinkedListBasic)

</br>
</br>

## 📌 원형 연결 리스트

### 특징

- 단순 연결 리스트보다 발전된 자료구조
- 마지막 원소가 처음 원소를 가리킨다.

### 장점

- 리스트의 처음과 끝에 대한 정보를 가지고 있으므로 append(), insert(0) 연산 모두 강점을 보인다.
- 따라서 extend(), copy(), reverse() 연산에 부담이 줄어든다.

### 소요시간

- 접근 - O(n)
- 검색 - O(n)
- 삭제 - O(n)
- 맨앞, 맨끝에 원소 추가(insert(0), append) - O(1)
- 그 밖의 원소 추가 - O(n)

[코드](https://github.com/jisupark123/data-structure/tree/main/list/CircularLinkedList)

</br>
</br>

## 📌 이중 연결 리스트

### 특징

- 이전 노드, 다음 노드를 가리키는 필드를 모두 가지는 자료구조
- 다양한 알고리즘에 유용하게 쓰인다.

### 장점

- 양방향 순회가 가능하다.
- 따라서 접근할 때의 소요시간을 최대 2배 단축할 수 있다.

### 단점

- 이전의 노드를 저장할 메모리 공간이 하나 더 필요하다.

### 소요시간

- 접근 - O(n)
- 검색 - O(n)
- 삭제 - O(n)
- 맨앞, 맨끝에 원소 추가(insert(0), append) - O(1)
- 그 밖의 원소 추가 - O(n)

[코드](https://github.com/jisupark123/data-structure/tree/main/list/DoublyLinkedList)

</br>
</br>

# 🧩 스택 (Stack)

</br>

### 스택(Stack)의 특징

- 가장 마지막에 삽입된 자료가 가장 먼저 삭제되는 **후입선출** 자료구조
- top으로 정한 곳을 통해서만 접근할 수 있다.
- 웹 브라우저의 방문 기록, 실행 취소(undo) 등에 쓰인다.

</br>

## 📌 배열 스택

### 특징

- 파이썬의 내장 리스트로 구현한 스택

### 장점

- 없다

### 단점

- 내장 리스트의 단점인 공간 제약을 피할 수 없다.

### 소요시간

- 삽입, 삭제, 접근 모두 O(1)

[코드](https://github.com/jisupark123/data-structure/tree/main/stack/ListStack)

</br>
</br>

## 📌 연결 리스트 스택

### 특징

- 단순 연결리스트로 구현한 스택
- 스택 연산은 단순 연결리스트로 충분하다. (굳이 원형 연결 리스트 사용할 필요 X)

### 장점

> 연결 리스트를 사용했기 때문에 공간의 제약에서 자유롭다.

### 소요시간

- 삽입, 삭제, 접근 모두 O(1)

[코드](https://github.com/jisupark123/data-structure/tree/main/stack/LinkedStack)

</br>
</br>

# 🧩 큐 (Queue)

</br>

### 큐(Queue)의 특징

- 가장 먼저 삽입된 자료가 가장 먼저 삭제되는 **선입선출** 자료구조
- 은행창구 번호표 대기, 프린터 출력, 선착순 프로그램 등에 쓰인다.

</br>

## 📌 배열 큐

### 특징

- 파이썬의 내장 리스트로 구현한 큐

### 장점

- 없다

### 단점

- 내장 리스트의 단점인 공간 제약을 피할 수 없다.

### 소요시간

- 삽입, 삭제, 접근 모두 O(1)

[코드](https://github.com/jisupark123/data-structure/tree/main/queue/ListQueue)

</br>
</br>

## 📌 연결 리스트 큐

### 특징

- 원형 연결 리스트를 이용한 큐
- 원형 연결리스트는 맨 앞과 맨 끝에 원소를 삽입할 때 O(1)의 효율을 보인다.
  -> 큐에 적합한 자료구조

### 장점

- 연결 리스트를 사용했기 때문에 공간의 제약에서 자유롭다.

### 소요시간

- 삽입, 삭제, 접근 모두 O(1)

[코드](https://github.com/jisupark123/data-structure/tree/main/queue/LinkedQueue)

</br>
</br>

## 📌 양방향 큐 (deque)

### 특징

- 양방향에서 요소를 추가하고 제거할 수 있다.
- 이중 연결리스트로 구현한다.

### 장점

- 일반적인 큐보다 다양한 곳에서 사용할 수 있다.

### 단점

- 이중 연결 리스트를 사용했기 때문에 메모리 공간을 더 차지한다.

### 소요시간

- 삽입, 삭제, 접근 모두 O(1)

[코드](https://github.com/jisupark123/data-structure/tree/main/queue/Deque)

</br>
</br>

# 🧩 힙 (Heap)

</br>

### 힙(Heap)의 특징

- 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조
  (우선순위 큐란 우선순위의 개념을 큐에 도입한 자료구조이며 힙으로 구현하는 것이 가장 효율적이다)
- 여러 개의 값들 중에서 최댓값이나 최솟값을 빠르게 찾아내도록 만들어졌다.
- 부모 노드의 키 값이 자식 노드의 키 값보다 항상 크거나(작거나) 같은 완전 이진 트리다.
- 우선순위 큐는 시뮬레이션 시스템, 운영체제에서의 작업 스케줄링 등에 쓰인다.

</br>

## 📌 최대 힙

### 특징

- 가장 큰 값을 가진 노드가 우선순위를 갖는다.
- 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같다.

### 소요시간

- 힙 생성 - O(n)
- 삽입 - O(log<sub>n</sub>)
- 삭제 - O(log<sub>n</sub>)
- 접근 - O(n)

[코드](https://github.com/jisupark123/data-structure/blob/main/heap/maxHeap.py)

</br>
</br>

## 📌 최소 힙

### 특징

- 가장 작은 값을 가진 노드가 우선순위를 갖는다.
- 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같다.

### 소요시간

- 힙 생성 - O(n)
- 삽입 - O(log<sub>n</sub>)
- 삭제 - O(log<sub>n</sub>)
- 접근 - O(n)

[코드](https://github.com/jisupark123/data-structure/blob/main/heap/minHeap.py)

</br>
</br>

# 🧩 이진 탐색 트리 (Binary Search Tree)

</br>

### 이진 탐색 트리 (Binary Search Tree)의 특징

- 항상 정렬된 상태를 유지하는 이진 트리로 탐색 연산에 강점을 가진 자료구조
  (탐색할 때 이진 탐색 알고리즘을 사용할 수 있다)
- 각 노드는 키를 가지며 서로 중복되지 않는다.
- 각 노드의 왼쪽 자식 노드의 키는 오른쪽 자식 노드의 키보다 작다.

</br>

## 📌 기본 이진 탐색 트리

### 특징

- 기본적인 이진 탐색 트리
- 균형을 잡아주는 연산이 없기 때문에 트리의 균형이 무너지면 최악의 경우 탐색 연산에 O(n)의 시간이 소요된다.

### 소요시간

- 삽입, 검색, 삭제 모두 O(log<sub>n</sub>)
- 균형이 무너질 시 검색에 O(n)

[코드](https://github.com/jisupark123/data-structure/tree/main/BST/BinarySearchTree)

</br>
</br>

## 📌 AVL 탐색 트리

### 특징

- AVL 검색 트리는 Basic 이진 검색 트리의 단점을 보완한 자료구조다.
- 삽입, 삭제 연산 시 트리의 균형을 체크, 만약 이상이 있으면 잡아주는 연산을 추가로 수행한다.
- 균형이 깨지는 조건 - 임의의 노드의 왼쪽 자식의 개수가 오른쪽 자식과 2이상 차이날 때
- 균형을 잡는 연산에 시간이 더 소요되긴 하지만 그럼에도 O(log<sub>n</sub>)의 시간복잡도를 유지한다.

### 소요시간

- 삽입, 삭제, 접근 모두 O(log<sub>n</sub>)

[코드](https://github.com/jisupark123/data-structure/tree/main/BST/AvlTree)

</br>
</br>
