from queue import Queue
import numpy as np
def breadth_first(graph, start=0):
	"""
	prints the order in which vertices are travserved by BFS algotrithm
	"""
	queue = Queue()
	queue.put(start)

	visited = np.zeros(graph.num_vertices)

	while not queue.empty():
		vertex = queue.get()

		if visited[vertex] == 1:
			continue

		print("Visit: ", vertex)
		visited[vertex] = 1

		for v in graph.get_adjacent_vertices(vertex):
			if visited[v] != 1:
				queue.put(v)