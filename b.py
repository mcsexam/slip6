from collections import deque

def bfs_undirected(graph, start_node, goal_node):
    if start_node == goal_node:
        return [start_node]
    
    queue = deque([start_node])
    visited = {start_node}
    parent_map = {start_node: None}
    
    print(f"Starting BFS from {start_node} to {goal_node} on UNDIRECTED graph...")
    
    while queue:
        current_node = queue.popleft()
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent_map[neighbor] = current_node
                
                if neighbor == goal_node:
                    path = []
                    node = goal_node
                    while node is not None:
                        path.append(node)
                        node = parent_map.get(node)
                    return path[::-1]  
                
                queue.append(neighbor)
    
    return "Goal node not reachable"

GRAPH_UNDIRECTED = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5, 7, 8],
    7: [6, 8],
    8: [6, 7]
}

start_node = 1
goal_node = 8

if __name__ == "__main__":
    shortest_path = bfs_undirected(GRAPH_UNDIRECTED, start_node, goal_node)
    print("Shortest Path:")
    print(shortest_path)
