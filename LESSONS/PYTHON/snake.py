

import pygame
import sys
import random
import time
pygame.init()
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10
WHITE = (255, 255, 255)
GREEN = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Snake Game")
clock = pygame.time.Clock()
class Snake:
	
	
	
	def __init__(self):
		self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
		self.length = 1
		self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
		self.color = GREEN
		self.score = 0
		self.game_over = False
		
	def get_head_position(self):
		return self.positions[0]
		
	def turn(self, point):
		if (point[0] * -1, point[1] * -1) == self.direction:
		
			return
			
		else:
			self.direction = point
			
		
	def move(self):
		if self.game_over:
		
			return
			
		head = self.get_head_position()
		x, y = self.direction
		new_x = (head[0] + x) % GRID_WIDTH
		new_y = (head[1] + y) % GRID_HEIGHT
		new_position = (new_x, new_y)
		if new_position in self.positions[1:]:
		
			self.game_over = True
			return
			
		self.positions.insert(0, new_position)
		if len(self.positions) > self.length:
		
			self.positions.pop()
			
		
	def reset(self):
		self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
		self.length = 1
		self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
		self.score = 0
		self.game_over = False
		
	def draw(self, surface):
		for i, position in enumerate(self.positions):
			rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
			if i == 0:
			
				pygame.draw.rect(surface, DARK_GREEN, rect)
				
			else:
				pygame.draw.rect(surface, self.color, rect)
				
			pygame.draw.rect(surface, DARK_GREEN, rect, 1)
			
		
		
		
class Food:
	
	
	
	def __init__(self):
		self.position = (0, 0)
		self.color = RED
		self.randomize_position()
		
	def randomize_position(self):
		self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
		
	def draw(self, surface):
		rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
		pygame.draw.rect(surface, self.color, rect)
		pygame.draw.rect(surface, WHITE, rect, 1)
		
		
def draw_grid(surface):
	for y in range(0, HEIGHT, GRID_SIZE):
		for x in range(0, WIDTH, GRID_SIZE):
			rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
			pygame.draw.rect(surface, WHITE, rect, 1)
			
		
		
	
	
def main():
	snake = Snake()
	food = Food()
	font = pygame.font.Font(None, 36)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
			
				pygame.quit()
				sys.exit()
				
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
				
					snake.turn(UP)
					
				elif event.key == pygame.K_DOWN:
					snake.turn(DOWN)
					
				elif event.key == pygame.K_LEFT:
					snake.turn(LEFT)
					
				elif event.key == pygame.K_RIGHT:
					snake.turn(RIGHT)
					
				elif event.key == pygame.K_r and snake.game_over:
					snake.reset()
					food.randomize_position()
					
				
			
		
		if not snake.game_over:
		
			snake.move()
			
		if snake.get_head_position() == food.position:
		
			snake.length += 1
			snake.score += 1
			food.randomize_position()
			while food.position in snake.positions:
				food.randomize_position()
				
			
			
		screen.fill(BLACK)
		draw_grid(screen)
		snake.draw(screen)
		food.draw(screen)
		score_text = font.render(f"Score: {snake.score}", True, WHITE)
		screen.blit(score_text, (10, 10))
		if snake.game_over:
		
			game_over_text = font.render("GAME OVER! Press R to restart", True, WHITE)
			text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
			screen.blit(game_over_text, text_rect)
			
		pygame.display.flip()
		clock.tick(FPS)
		
	
	
if __name__ == "__main__":

	main()
	

#  Export  Date: 05:43:36 PM - 10:Apr:2025.

