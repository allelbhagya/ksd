import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ROAD_WIDTH = 100
LANE_WIDTH = 10
CAR_SIZE = (40, 20)
CAR_SPEED = 3

class Road:
    def __init__(self, x, y, length, width, direction):
        self.rect = pygame.Rect(x, y, length, width)
        self.direction = direction

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

        if self.direction == 'horizontal':
            lane_start = self.rect.top + LANE_WIDTH // 2
            lane_end = self.rect.bottom - LANE_WIDTH // 2
            for y in range(lane_start, lane_end, LANE_WIDTH * 2):
                pygame.draw.rect(screen, WHITE, (self.rect.centerx - 2, y, 4, LANE_WIDTH))
        elif self.direction == 'vertical':
            lane_start = self.rect.left + LANE_WIDTH // 2
            lane_end = self.rect.right - LANE_WIDTH // 2
            for x in range(lane_start, lane_end, LANE_WIDTH * 2):
                pygame.draw.rect(screen, WHITE, (x, self.rect.centery - 2, LANE_WIDTH, 4))

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, start_road):
        super().__init__()
        self.image = pygame.image.load('car.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, CAR_SIZE) 
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = speed
        self.start_road = start_road
        self.rotate_car()

    def rotate_car(self):
        if self.direction == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == 'up':
            self.image = pygame.transform.rotate(self.image, -90)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.image, 90)
    def move(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Junction Traffic Simulation")
clock = pygame.time.Clock()

vertical_road = Road(WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, HEIGHT, 'vertical')
horizontal_road = Road(0, HEIGHT // 2 - ROAD_WIDTH // 2, WIDTH, ROAD_WIDTH, 'horizontal')

cars = pygame.sprite.Group()

counter_right = 0
counter_left = 0
counter_up = 0
counter_down = 0

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < WIDTH // 3:
                counter_right += 1
                cars.add(Car(mouse_x, mouse_y, 'right', CAR_SPEED, 1))
            elif mouse_x > WIDTH // 3 * 2:
                counter_left += 1
                cars.add(Car(mouse_x, mouse_y, 'left', CAR_SPEED, 3))
            elif mouse_y < HEIGHT // 3:
                counter_down += 1
                cars.add(Car(mouse_x, mouse_y, 'down', CAR_SPEED, 2))
            elif mouse_y > HEIGHT // 3 * 2:
                counter_up += 1
                cars.add(Car(mouse_x, mouse_y, 'up', CAR_SPEED, 4))

    for car in cars:
        car.move()

    vertical_road.draw(screen)
    horizontal_road.draw(screen)
    cars.draw(screen)

    font = pygame.font.Font(None, 36)
    text_right = font.render(f"Left: {counter_right}", True, BLACK)
    text_left = font.render(f"Right: {counter_left}", True, BLACK)
    text_up = font.render(f"Bottom: {counter_up}", True, BLACK)
    text_down = font.render(f"Top: {counter_down}", True, BLACK)
    screen.blit(text_right, (WIDTH - 150, 10))
    screen.blit(text_left, (WIDTH - 150, 50))
    screen.blit(text_up, (WIDTH - 150, 90))
    screen.blit(text_down, (WIDTH - 150, 130))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
