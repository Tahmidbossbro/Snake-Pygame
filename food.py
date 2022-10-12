import pygame
from random import randint

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class Food:
    def __init__(self, surface, snake):
        self.snake = snake
        self.food = None
        self.screen = surface
        self.food_radius = 10
        self.food_location_x, self.food_location_y = 0, 0
        self.i = 1
        self.cook()

    def cook(self):
        self.food_location_x, self.food_location_y = (randint(1, 28) * 20, randint(1, 28) * 20)

        for _ in self.snake.snake_data:

            if (self.food_location_x, self.food_location_y) == (_.x, _.y):
                self.cook()
            else:
                self.food = pygame.Rect(self.food_location_x, self.food_location_y, 20, 20)

    def put_food(self):
        pygame.draw.rect(surface=self.screen, color=YELLOW,
                         rect=self.food,
                         border_radius=self.food_radius)


# if __name__ == '__main__':
#     def draw_window():
#         screen.fill(BLACK)
#
#
#     clock = pygame.time.Clock()
#     screen = pygame.display.set_mode((600, 600))
#     game_on = True
#     food = Food(screen)
#
#     while game_on:
#         clock.tick(10)
#
#         for Event in pygame.event.get():
#             if Event.type == pygame.QUIT:
#                 game_is_on = False
#                 quit()
#         draw_window()
#         # food.put_food()
#         food.special_food()
#         pygame.display.update()
