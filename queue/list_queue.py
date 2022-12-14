"""
내장 리스트로 구현한 큐
내장 리스트의 단점인 공간 제약이 있다.

삽입, 삭제, 접근 모두 O(1)
"""


class Queue:
    def __init__(self):
        self.__queue = []

    # 큐의 끝에 원소 추가
    def enqueue(self, x):
        self.__queue.append(x)

    # 큐의 첫 원소를 삭제한 후 원소 리턴
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty list")
        return self.__queue.pop(0)

    ## 큐 초기화
    def dequeueAll(self):
        self.__queue.clear()

    # 큐의 첫 원소를 알려줌
    def front(self):
        if self.isEmpty():
            raise IndexError("queue index out of range")
        else:
            return self.__queue[0]

    def isEmpty(self) -> bool:
        return not bool(self.__queue)

    def __str__(self):
        res = ""
        for element in self.__queue:
            res += f"{element}, "

        return f"queue([{res[:-2]}])"


if __name__ == "__main__":
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    print(a.front())
    a.dequeue()
    print(a)
