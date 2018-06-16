import math
from math import tau

import pygame
import pygame.gfxdraw

GRID_COLOR = (0xee, 0xee, 0xee)
TIMER_POS = (20, 20)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.animations = []
        self.timer = None

    def init(self):
        self.draw_grid(40, 40)
        self.timer = Timer(self.screen, 180, TIMER_POS)
        self.timer.init()

    def draw_grid(self, cell_width, cell_height):
        width = self.screen.get_width()
        height = self.screen.get_height()
        for w in range(0, width, cell_width):
            pygame.draw.line(self.screen, GRID_COLOR, (w, 0), (w, height), 2)
        for h in range(0, height, cell_height):
            pygame.draw.line(self.screen, GRID_COLOR, (0, h), (width, h), 2)

    def run(self, frame):
        self.handle_keys(frame)
        self.timer.update(frame)
        # self.update_animations(frame)
        pygame.display.update()

    def handle_keys(self, frame):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print("Hey, you pressed the key, '0'!")
                if event.key == pygame.K_1:
                    print("Doing whatever")


class Timer:
    def __init__(self, screen, duration, position, radius=15):
        self.screen = screen
        self.duration = duration
        self.position = position
        self.radius = radius
        self.frame = None  # drawn outline of timer
        self.filled = None  # drawn filled pie of timer
        self.font = None

    def init(self):
        self.frame = pygame.draw.circle(self.screen, (0, 0, 0), self.position, self.radius)
        self.filled = pygame.draw.polygon(self.screen, (0, 255, 0), self.get_polypts(0))
        self.font = pygame.font.SysFont("Arial", 24)

    def update(self, frame):
        # timer should complete one revolution every DURATION frames
        pygame.draw.circle(self.screen, (0, 0, 0), self.position, self.radius)
        pygame.draw.polygon(self.screen, (0, 255, 0), self.get_polypts(frame))

        text = self.font.render(f"Frame {frame}", True, (0, 0, 0), (255, 255, 255))
        self.screen.blit(text, (self.position[0] + 25, self.position[1]))

    def get_polypts(self, frame):
        pts = [self.position]
        numvert = frame % self.duration
        end = -((frame % self.duration / self.duration) * tau)
        for r in range(numvert + 1):
            rad = (end / (numvert + 1)) * r
            dx = math.cos(rad) * (self.radius - 2)
            dy = math.sin(rad) * (self.radius - 2)
            pts.append((self.position[0] + dy, self.position[1] - dx))  # reverse to rot by 90
        pts.append(self.position)
        return pts
