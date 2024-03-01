import sys
from collections import deque


def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque()
    for u in graph:
        if in_degree[u] == 0:
            queue.append(u)

    sorted_list = []
    while queue:
        u = queue.popleft()
        sorted_list.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return sorted_list


def shortest_path(graph, start, end):
    top_sorted = topological_sort(graph)
    distances = {v: sys.maxsize for v in graph}
    paths = {v: [] for v in graph}
    distances[start] = 0
    for u in top_sorted:
        for v in graph[u]:
            new_dist = distances[u] + graph[u][v]
            if new_dist < distances[v]:
                distances[v] = new_dist
                paths[v] = paths[u] + [u]

    return distances[end], paths[end] + [end]


graph = {
    'x_1': {'x_2': 8, 'x_3': 12, 'x_6': 14},
    'x_2': {'x_4': 1, 'x_5': 4},
    'x_3': {'x_5': 19},
    'x_4': {'x_6': 16, 'x_3': 13},
    'x_5': {},
    'x_6': {'x_5': 15}
}
start = 'x_1'
end = 'x_5'
distance, path = shortest_path(graph, start, end)
print(f"Кратчайший путь от вершины {start} до вершины {end}: {path} (расстояние: {distance})")
