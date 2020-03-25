import numpy as np
from graph import Graph
class AdjacencyMatrixGraph(Graph):
	def __init__(self, num_vertices, directed=False):
		"""
		calls abstract class Graph's contructor to
		sets value for num_vertices and directed
		"""
		super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)

		self.matrix = np.zeros((num_vertices, num_vertices)) 

	def set_graph(self,graph):
		"""
			Sets the matrix from already existing graph
		"""
		self.matrix = graph

	def add_edge(self, v1, v2, weight=1):
		"""
		connects two vertices
		"""
		if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
			raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

		if weight < 1:
			raise ValueError("An edge cannot have weight < 1")	

		self.matrix[v1][v2] = weight
		if self.directed == False:
			self.matrix[v2][v1] = weight

	def get_adjacent_vertices(self, v):
		if v < 0 or v >= self.num_vertices:
			raise ValueError("Cannot access vertex %d" % v)

		adjacent_vertices = []
		for i in range(self.num_vertices):
			if self.matrix[v][i] > 0:
				adjacent_vertices.append(i)

		return adjacent_vertices		

	def get_indegree(self, v):
		"""
		returns list of indegree vertices
		"""
		if v < 0 or v >= self.num_vertices:
			raise ValueError("Cannot access vertex %d" % v)

		indegree = 0
		for i in range(self.num_vertices):
			if self.matrix[i][v] > 0:
				indegree = indegree + 1	
		
		return indegree	

	def get_edge_weight(self, v1, v2):
		"""
		returns wieght of edges between two vertices
		"""
		return self.matrix[v1][v2]

	def display(self):
		"""
		prints the whole graph
		"""
		for i in range(self.num_vertices):
			for v in self.get_adjacent_vertices(i):
				print(i, "-->", v)