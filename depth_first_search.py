from adjacency_matrix_graph import AdjacencyMatrixGraph
import numpy as np

def depth_first(graph, start=0):
	"""
	prints the order in which vertices are travserved by DFS algorithm
	"""
	stack = []
	# queue.put(start)
	stack.append(start)
	
	visited = np.zeros(graph.num_vertices)

	while len(stack) != 0 :
		vertex = stack.pop()

		if visited[vertex] == 1:
			continue

		print("Visit: ", vertex)
		visited[vertex] = 1

		for v in graph.get_adjacent_vertices(vertex):
			if visited[v] != 1:
				stack.append(v)
