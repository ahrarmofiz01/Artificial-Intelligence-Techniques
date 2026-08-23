import numpy as np

# Define the edges of the graph
edges = [
    (1, 2), (1, 5), (2, 3), (3, 1),
    (4, 5), (4, 7), (5, 1), (5, 4),
    (5, 8), (6, 4), (6, 8), (7, 6),
    (8, 5), (8, 9), (9, 6), (9, 10),
    (10, 9)
]

# Adjacency Matrix form of the graph
AMat = np.zeros(shape=(11, 11))

for (i, j) in edges:
    AMat[i, j] = 1

print("Adjacency Matrix Structure:")
print(AMat)

print("-" * 50)