from collections import Counter
import random
from grid import Grid

class UnionFind:
	def __init__(self, n): #O(n)
		''' make_union_find: creates one set for each vertex v ∈ S,
		the name of set is the name of the vertex
		'''
		# self.my_set = { set(x) for x in given_set } #set comprehension
		self.set_names = list(range(n))
		self.n = n # total number of nodes
		# represent nodes by index of set_names

	def find(self, x): #O(1)
		''' Return name of set containing x '''
		return self.set_names[x]

	def union(self, x, y): #O(n)
		''' Replace sets X and Y of partition with Z = X ∪ Y:
		- X ∪ Y gets the name of whichever set X or Y is larger (ties are broken arbitrarily)
		- changes the names of each of the elements in the smaller set
		'''
		x_rep = self.find(x)
		y_rep = self.find(y)
		assert x_rep != y_rep, "union operation takes two elements from distinct sets"

		if self.set_size(x_rep) > self.set_size(y_rep):
			self.change_name(y_rep, x_rep) # change name in of set of y_rep into x_rep
		else:
			self.change_name(x_rep, y_rep)

	def change_name(self, set_name, new_name):
		for idx in self.nodes_in_set(set_name):
			self.set_names[idx] = new_name

	def nodes_in_set(self, set_name):
		return [ idx for idx in range(self.n) if self.set_names[idx] == set_name ]

	def set_size(self, set_name):
		return Counter(self.set_names).get(set_name) #Counter creates a dict

def build_edge_list(w, h):
	# edge: (node1, node2); node index = w*row + col
	edge_list = []
	for i in range(h):
		for j in range(w-1):
			edge_list.append( (i*w+j, i*w+j+1) )
	for i in range(h-1):
		for j in range(w):
			edge_list.append( (i*w+j, i*w+j+w) )
	return edge_list

def gen_maze(w, h):
	# initialize
	grid = Grid(w, h)
	nodes = UnionFind(w*h)
	edge_list = build_edge_list(w, h)

	# run Kruskal's Algorithm
	random.shuffle(edge_list)
	while edge_list:
		e = edge_list.pop()
		v1, v2 = e
		if nodes.find(v1) != nodes.find(v2):
			grid.remove_wall(e)
			nodes.union(v1, v2)
		random.shuffle(edge_list) #can comment this out if input size is big
	grid.print_grid()

if __name__=="__main__":
	gen_maze(20, 16)
