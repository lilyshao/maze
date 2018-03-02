hline = "__" #2*_
vline = "|"

class Grid:

	def __init__(self, width, height):
		self.grid = [" " + hline] * width + ["\n"]
		for row in range(height):
			for col in range(width):
				self.grid += [ vline+hline ]
			self.grid += [vline +"\n"]
		self.w = width

	def remove_wall(self, edge): # replace wall-"|"or"__ with ""
		a, b = edge
		row, col = a//self.w, a%self.w
		# idx: location of the wall in self.grid
		if abs(a-b) == self.w: # if it's a horizontal wall:
			idx = (row+1)*(self.w+1)+col
			# replace vline+hline with vline
			self.grid[idx] = vline + "  "
		else: # it's a vertical wall
			idx = (row+1)*(self.w+1)+col+1
			# replace vline+hline with hline
			self.grid[idx] = " " + hline

	def print_grid(self):
		print("".join(self.grid))
