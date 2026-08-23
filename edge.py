# Define the edges of the graph

edges = [
    (1, 2), (1, 5), (2, 3), (3, 1),
    (4, 5), (4, 7), (5, 1), (5, 4),
    (5, 8), (6, 4), (6, 8), (7, 6),
    (8, 5), (8, 9), (9, 6), (9, 10),
    (10, 9)
]


# Adjacency List form of the graph

AList = {}

for i in range(1, 11):
    AList[i] = []

for (i, j) in edges:
    AList[i].append(j)


print("Adjacency List Structure:")
print(AList)

print("-" * 50)