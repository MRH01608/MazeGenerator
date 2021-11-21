import pygame, sys

class Node:
	def __init__(self, row, col, size):
		self.m_row = row
		self.m_col = col
		self.m_size = size
		self.m_walls = {} # key is north, sotu, east and west, value is adjacent node(s)

class Maze:
	def __init__(self, num_rows, num_cols, node_size):
		self.m_num_rows = num_rows
		self.m_num_cols = num_cols
		self.m_node_size = node_size
		self.m_nodes = [ [Node(i, j, self.m_node_size) for j in range(self.m_num_cols)] for i in range(self.m_num_rows)]

def main():
	pygame.init()
	screen = pygame.display.set_mode((900,900), 0, 32)
	screen.fill((115, 114, 110))

	num_rows = 3
	num_cols = 3
	node_size = 30
	maze = Maze(num_rows, num_cols, node_size)

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