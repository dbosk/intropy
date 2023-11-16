import collections

q = collections.deque()
q.append(1)
q.append(2)
q.append(3)
print(f"q = {q}")

while q:
    print(f"q.popleft() = {q.popleft()}")
    print(f"q = {q}")
