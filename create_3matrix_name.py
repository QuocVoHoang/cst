import pandas as pd

matrix_bike_path = 'matrix_length.csv'
locations_path = 'locations200.csv'

matrix_bike = pd.read_csv(matrix_bike_path, index_col=0)
locations = pd.read_csv(locations_path)

locations['node_id'] = locations['node_id'].astype(str)

node_to_location = dict(zip(locations['node_id'], locations['location']))

matrix_bike.index = [node_to_location.get(str(node), node) for node in matrix_bike.index]
matrix_bike.columns = [node_to_location.get(str(node), node) for node in matrix_bike.columns]

final_matrix_bike_path = 'final_matrix_length.csv'
matrix_bike.to_csv(final_matrix_bike_path)