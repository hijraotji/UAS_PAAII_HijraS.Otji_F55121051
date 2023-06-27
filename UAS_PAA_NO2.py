import time
import networkx as nx

def tsp(graph, start):
    visited = [start]
    path = []
    current = start

    while len(visited) < len(graph.nodes):
        next_node = None
        min_distance = float('inf')
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                distance = graph[current][neighbor]['weight']
                if distance < min_distance:
                    min_distance = distance
                    next_node = neighbor
        if next_node is None:
            return None
        visited.append(next_node)
        path.append((current, next_node))
        current = next_node

    path.append((current, start))
    return path

def dijkstra(graph, start, end):
    shortest_path = nx.dijkstra_path(graph, start, end)
    path_length = nx.dijkstra_path_length(graph, start, end)
    return shortest_path, path_length

# Graph yang diberikan
graph = nx.Graph()
graph.add_edge('A', 'C', weight=10)
graph.add_edge('A', 'B', weight=12)
graph.add_edge('A', 'G', weight=12)
graph.add_edge('C', 'B', weight=8)
graph.add_edge('C', 'D', weight=11)
graph.add_edge('C', 'E', weight=3)
graph.add_edge('C', 'G', weight=9)
graph.add_edge('B', 'D', weight=12)
graph.add_edge('G', 'E', weight=7)
graph.add_edge('G', 'F', weight=9)
graph.add_edge('D', 'E', weight=11)
graph.add_edge('D', 'F', weight=10)
graph.add_edge('E', 'F', weight=6)

print("Graph:")
print(graph.edges(data=True))
print('-' * 30)

choice = input("Pilih metode perhitungan shortest path (TSP/Dijkstra): ")
print('-' * 30)

if choice == "TSP":
    start_time = time.time()
    path = tsp(graph, 'A')
    end_time = time.time()
    if path is None:
        print("Tidak ada solusi.")
    else:
        print("Shortest Path TSP:")
        for edge in path:
            print(f"{edge[0]} -> {edge[1]}")
else:
    start_node = input("Masukkan node awal: ")
    end_node = input("Masukkan node akhir: ")
    print('-' * 30)
    start_time = time.time()
    shortest_path, path_length = dijkstra(graph, start_node, end_node)
    end_time = time.time()
    if shortest_path is None:
        print("Tidak ada rute yang dapat diambil.")
    else:
        print(f"Shortest Path Dijkstra dari {start_node} ke {end_node}:")
        for i in range(len(shortest_path) - 1):
            print(f"{shortest_path[i]} -> ", end="")
        print(shortest_path[-1])
        print(f"Panjang path: {path_length}")

execution_time = end_time - start_time
print(f"\nWaktu komputasi perhitungan shortest path: {execution_time} detik")
print('-' * 30)

# Analisis algoritma
n = len(graph.nodes)
worst_case_tsp = (n-1) * n // 2
worst_case_dijkstra = n * (n-1)
best_case_tsp = n - 1
best_case_dijkstra = n - 1
average_case_tsp = (worst_case_tsp + best_case_tsp) // 2
average_case_dijkstra = (worst_case_dijkstra + best_case_dijkstra) // 2

print("Analysis Algorithm:")
print("TSP:")
print(f"Worst case: {worst_case_tsp} perbandingan")
print(f"Best case: {best_case_tsp} perbandingan")
print(f"Average case: {average_case_tsp} perbandingan")
print('-' * 30)
print("Dijkstra:")
print(f"Worst case: {worst_case_dijkstra} perbandingan")
print(f"Best case: {best_case_dijkstra} perbandingan")
print(f"Average case: {average_case_dijkstra} perbandingan")
print('-' * 30)
