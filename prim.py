import random
from grid import Grid

def gen_maze(w, h):
	grid = Grid(w, h)
	edge_list = []
	nodes = list(range(w*h))
	in_maze = [0]*len(nodes)

	start_node = random.choice(nodes)
	in_maze[start_node] = 1
	edge_list += get_walls(start_node, nodes, w, h)
	while edge_list:
		random.shuffle(edge_list)
		wall = edge_list.pop()
		v1, v2 = wall
		# If only one of the two cells that the wall divides is visited:
		val1, val2 = in_maze[v1], in_maze[v2]
		if (val1, val2) in [(0,1), (1, 0)]:
			# Make the wall a passage: remove wall in grid
			grid.remove_wall(wall)
			if val1 == 0:
				unvisited = v1
			else: unvisited = v2
			# mark the unvisited cell as part of the maze
			in_maze[unvisited] = 1
			# Add the neighboring walls of the cell to the wall list.
			edge_list += get_walls(unvisited, nodes, w, h)
	grid.print_grid()

def get_walls(node, nodes, w, h):
	# #row, col = node//w, node%w
	left_sides = [ i*w for i in range(1, h-1) ]
	right_sides = [ i*w+w-1 for i in range(1, h-1) ]
	top_sides = [ x for x in range(1, w-1) ]
	bottom_sides = [ w*(h-1) + x for x in range(1, w-1)]
	# middle = [the rest]
	if node == 0: #top left corner
		return [(0,1), (0, w)]
	elif node == w-1: #top right corner
		return [(w-2, w-1), (w-1, 2*w-1)]
	elif node == nodes[-1]-w+1: #bottom left
		val = nodes[-1]-w+1
		return [(val, val+1), (val-w, val)]
	elif node == nodes[-1]: #bottom right
		return [(nodes[-1]-1, nodes[-1]), (nodes[-1]-w, nodes[-1])]
	elif node in left_sides:
		return [(node-w, node), (node, node+1), (node, node+w)]
	elif node in right_sides:
		return [(node-w, node), (node-1, node), (node, node+w)]
	elif node in top_sides:
		return [(node-1, node), (node, node+1), (node, node+w)]
	elif node in bottom_sides:
		return [(node-1, node), (node, node+1), (node-w, node)]
	else: # in middle
		return [(node-1, node), (node, node+1), (node-w, node), (node, node+w)]

if __name__ == '__main__':
	gen_maze(20, 16)
