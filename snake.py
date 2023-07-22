import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        self.body.insert(0, new_head)

    def grow(self):
        tail_x, tail_y = self.body[-1]
        dx, dy = self.direction
        new_tail = ((tail_x - dx) % GRID_WIDTH, (tail_y - dy) % GRID_HEIGHT)
        self.body.append(new_tail)

    def check_collision(self):
        return len(self.body) != len(set(self.body))

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self):
        for segment in self.body:
            x, y = segment
            pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        x, y = self.position
        pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        snake.move()
        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.randomize_position()

        if snake.check_collision():
            pygame.quit()
            return

        screen.fill(BLACK)
        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)  # Adjust the speed of the game

if __name__ == "__main__":
    main()

    