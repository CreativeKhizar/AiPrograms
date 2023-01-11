def bfs(graph,root):
    visited = set()
    queue = [root]
    while queue:
        print(queue)
        vertex = queue.pop(0)
        print(vertex)
        print(queue)
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in  visited:
                queue.append(i)
    print(visited)
if __name__=="__main__":
    graph={0:[1,2,3],
           1:[0,2],
           2:[0,1,4],
           3:[0],
           4:[2]}
    bfs(graph,0)
