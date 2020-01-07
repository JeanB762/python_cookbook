from collections import deque


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)

print(q)

q.append(4)

print(q)

q.append(5)

print(q)

q.append(6)

print(q)
print('#################################################################################')
print('#################################################################################')
print('#################################################################################')

# More generally, a deque can be used whenever you need a simple queue structure.
# If you don’t give it a maximum size, you get an unbounded queue that lets you 
# append and pop items on either end.

deq = deque()

deq.append(1)
deq.append(2)
deq.append(3)
deq.append(4)


print('Deque: ', deq)
print('retirando da direita:', deq.pop())
print('Deque: ', deq)
deq.appendleft(4)
print('Deque: ', deq)
print('retirando da direita:', deq.pop())
deq.append(12)
print('Reirando da esquerda: ', deq.popleft())
print('Deque: ', deq)

#Adding or popping items from either end of a queue has O(1) complexity.
# This is unlike a list where inserting or removing items from the front of the list is O(N).