"""from collections import deque
list=[1,1,2]
#print(bank)
list.popleft()
#print(bank)
list.popleft()
print(list)
bank.popleft()
if not bank:
    print("No person left")"""

queue = []

# Adding elements to the queue
queue.append(1)
queue.append(1)
queue.append(2)

#print("Initial queue")
#print(queue)

# Removing elements from the queue
#print("\nElements dequeued from queue")
print(queue.pop())
#print(queue.pop())
#print(queue.pop())