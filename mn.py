


import numpy as np
import heapq
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random


def generate_adj_matrix(num_nodes, num_edges):
    adj_matrix = np.zeros((num_nodes, num_nodes))
    edges_added = 0
    while edges_added < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and adj_matrix[u, v] == 0:
            adj_matrix[u, v] = random.randint(1, 10)  
            edges_added += 1
    df_adj_matrix = pd.DataFrame(adj_matrix)
    return df_adj_matrix

num_nodes = 10  # Số đỉnh
num_edges =  20 # Số cạnh

adj_matrix = generate_adj_matrix(num_nodes, num_edges)
print("Ma trận kề ngẫu nhiên:")
print(adj_matrix)

def dijkstra(cost_matrix, capacity_matrix, source, sink, parent):
    num_nodes = len(cost_matrix)
    distances = [float('inf')] * num_nodes
    distances[source] = 0
    parent[source] = -1
    priority_queue = [(0, source)]  

    while priority_queue:
        dist_u, u = heapq.heappop(priority_queue)
        if dist_u > distances[u]:
            continue

        for v in range(num_nodes):
            if capacity_matrix[u][v] > 0 and distances[v] > distances[u] + cost_matrix[u][v]:
                distances[v] = distances[u] + cost_matrix[u][v]
                parent[v] = u
                heapq.heappush(priority_queue, (distances[v], v))

    return distances[sink] != float('inf')

def get_path(parent, sink):
    path = []
    v = sink
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path

def get_path(parent, sink):
    path = []
    v = sink
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path

def min_cost_max_flow(cost_matrix, capacity_matrix, source, sink):
    num_nodes = len(cost_matrix)
    parent = [-1] * num_nodes
    max_flow = 0
    min_cost = 0
    paths = [] 
    
    while dijkstra(cost_matrix, capacity_matrix, source, sink, parent):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity_matrix[u][v])
            v = parent[v]

        v = sink
        path = [] 
        while v != source:
            u = parent[v]
            capacity_matrix[u][v] -= path_flow
            capacity_matrix[v][u] += path_flow
            min_cost += path_flow * cost_matrix[u][v]
            path.append((u, v))  
            v = parent[v]
        
        max_flow += path_flow
        paths.append((get_path(parent, sink), path_flow))  

    return max_flow, min_cost, paths

capacity_matrix = [ 
    [ 0, 3, 1, 0, 3 ], 
    [ 0, 0, 2, 0, 0 ], 
    [ 0, 0, 0, 1, 6 ], 
    [ 0, 0, 0, 0, 2 ],
    [ 0, 0, 0, 0, 0 ] ]

cost_matrix = [ 
    [ 0, 3, 0, 0, 2 ], 
    [ 0, 0, 0, 3, 0 ], 
    [ 0, 0, 0, 0, 0 ], 
    [ 0, 0, 0, 0, 1 ],
    [ 0, 0, 0, 0, 0 ] ]

G = nx.DiGraph()
for i in range(len(cost_matrix)):
    for j in range(len(cost_matrix[i])):
        if capacity_matrix[i][j] > 0:
            edge_label = f"cost: {cost_matrix[i][j]}, cap: {capacity_matrix[i][j]}"
            G.add_edge(i, j, label=edge_label, cost=cost_matrix[i][j], capacity=capacity_matrix[i][j])

source, sink = 0, 5
max_flow, min_cost, paths = min_cost_max_flow(cost_matrix, capacity_matrix, source, sink)

print("Luồng cực đại:", max_flow)
print("Chi phí tối thiểu:", min_cost)
print("Các đường đi ngắn nhất và luồng của từng đường đi:")

for path, flow in paths:
    print("Đường đi:", " -> ".join(map(str, path)), "| Luồng:", flow)





