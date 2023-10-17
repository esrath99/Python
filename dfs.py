
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1, 4], 4: [1, 2, 3]}
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
dfs(graph, 0)
