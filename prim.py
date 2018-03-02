'''
Start with a grid full of walls.
Pick a cell, mark it as part of the maze (?visited). Add the walls of the cell to the wall list.
While there are walls in the list:
Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
Make the wall a passage and mark the unvisited cell as part of the maze.
Add the neighboring walls of the cell to the wall list.
Remove the wall from the list.

wall_list: same as edge_list in Kruskal
nodes? list(range(w*h))
bool list - in_maze, index as node id
'''

from kruskal import build_edge_list

def gen_maze(w, h):
	edge_list = build_edge_list(w, h)
	nodes = list(range(w*h))
	visited = [0]*len(nodes)

if __name__ == '__main__':
	gen_maze(5, 3)
