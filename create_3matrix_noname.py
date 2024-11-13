import pandas as pd
import numpy as np

input_path = 'length.csv'
output_path = 'matrix_length.csv'

data = pd.read_csv(input_path)
nodes = pd.concat([data['start_node'], data['end_node']]).unique()
node_to_index = {node: idx for idx, node in enumerate(nodes)}

n = len(nodes)
adjacency_matrix = np.zeros((n, n))

for _, row in data.iterrows():
    start_idx = node_to_index[row['start_node']]
    end_idx = node_to_index[row['end_node']]
    adjacency_matrix[start_idx, end_idx] = row['length']
    adjacency_matrix[end_idx, start_idx] = row['length']

adjacency_df = pd.DataFrame(adjacency_matrix, index=nodes, columns=nodes)

adjacency_df.to_csv(output_path)