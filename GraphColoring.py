def prim_kruskal_algorithm(graph, start_node):
    visited = set()
    result = []

    edges = [(0, start_node, None)]

    while edges:
        current_weight, current_vertex, previous_vertex = min(edges, key=lambda x: x[0])
        edges.remove((current_weight, current_vertex, previous_vertex))

        if current_vertex not in visited:
            visited.add(current_vertex)
            if previous_vertex is not None:
                result.append((previous_vertex, current_vertex, current_weight))

            for neighbor, weight in graph[current_vertex].items():
                if neighbor not in visited:
                    edges.append((weight, neighbor, current_vertex))

    return result


graph = {
    'x_1': {'x_2': 8, 'x_3': 12, 'x_6': 14},
    'x_2': {'x_1': 8, 'x_4': 1, 'x_5': 4},
    'x_3': {'x_1': 12, 'x_4': 13, 'x_5': 19},
    'x_4': {'x_2': 1, 'x_6': 16, 'x_3': 13},
    'x_5': {'x_2': 4, 'x_3': 19, 'x_6': 15},
    'x_6': {'x_5': 15, 'x_1': 14, 'x_4': 16}
}

resulting_tree = prim_kruskal_algorithm(graph, 'x_1')
print(resulting_tree)