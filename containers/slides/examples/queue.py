import collections

q = collections.deque()
q.append(0)
q.append(1)
q.append(2)
q.append(3)
q.append(4)

while q:
    print(q.popleft())
