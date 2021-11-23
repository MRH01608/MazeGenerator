import pygame, sys

class Node:
	def __init__(self, row, col, size):
		self.m_row = row
		self.m_col = col
		self.m_size = size
		self.m_walls = {} # key is north, sotu, east and west, value is adjacent node(s)

	def connections(self):
		m_list = []
		for key,value in self.m_walls.items():
			if value != None:
				m_list.append(key)
		return m_list

	def draw(self, sceen):
		pass

class Maze:
	def __init__(self, num_rows, num_cols, node_size):
		self.m_num_rows = num_rows
		self.m_num_cols = num_cols
		self.m_node_size = node_size
		self.m_nodes = [ [Node(i, j, self.m_node_size) for j in range(self.m_num_cols)] for i in range(self.m_num_rows)]

	def connect_nodes_default(self):
		for node in self.iter_node():
			for node in self.iter_node():
				node.m_walls["north"]= self.get_node(node.m_row-1, node.m_col)
				node.m_walls["south"]= self.get_node(node.m_row+1, node.m_col)
				node.m_walls["west"]= self.get_node(node.m_row, node.m_col-1)
				node.m_walls["east"]= self.get_node(node.m_row, node.m_col+1)

	def draw(self, screen):
		self.draw_outer_boundary(screen)
		for node in self.iter_node():
			node.draw(screen)

	def draw_outer_boundary(self, screen):
		#define corners
		topleft = (self.m_node_size, self.m_node_size)
		topright = (self.m_node_size + self.m_node_size*self.m_num_cols, self.m_node_size)
		bottomleft = (self.m_node_size, self.m_node_size + self.m_node_size*self.m_num_rows)
		bottomright = (self.m_node_size + self.m_node_size*self.m_num_cols, self.m_node_size + self.m_node_size*self.m_num_rows)
		pygame.draw.line(screen, (0,4,212), topleft, topright, 5)
		pygame.draw.line(screen, (0,4,212), topleft, bottomleft, 5)
		pygame.draw.line(screen, (0,4,212), bottomleft, bottomright, 5)
		pygame.draw.line(screen, (0,4,212), bottomright, topright, 5)

	def iter_node(self):
		for i in range(self.m_num_rows):
			for j in range(self.m_num_cols):
				yield self.m_nodes[i][j]

	def get_node(self, row, col):
		if row >= 0 and row < self.m_num_rows \
				and col >= 0 and col < self.m_num_cols:
			return self.m_nodes[row][col]
		else:
			return None

	def printme(self):
		for node in self.iter_node():
			print(node.m_row, node.m_col, node.connections())

def main():
	pygame.init()
	screen = pygame.display.set_mode((600,600), 0, 32)
	screen.fill((115, 114, 110))

	num_rows = 6
	num_cols = 6
	node_size = 30
	maze = Maze(num_rows, num_cols, node_size)
	maze.connect_nodes_default() #connecting means to make walls?
	#maze.printme()
	maze.draw(screen)

	running = True
	held_down = False
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				held_down = True
			elif event.type == pygame.MOUSEBUTTONUP:
				held_down = False
			elif event.type == pygame.MOUSEMOTION:
				if held_down:
					pygame.draw.circle(screen, (235, 233, 228), event.pos, 5, 0)
		pygame.display.update()

	pygame.quit()
	sys.exit()

#client code
main()