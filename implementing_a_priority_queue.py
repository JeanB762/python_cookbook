import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[2]

q = PriorityQueue()
q.push(('foo'), 1)
q.push(('bar'), 5)
q.push(('spam'), 4)
q.push(('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())