import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class Border:
    def __init__(self, snake, surface, food):
        self.food = food
        self.screen = surface
        self.snake = snake
        self.data = snake.snake_data
        self.left = 0
        self.right = 600
        self.top = 0
        self.bottom = 600

    def transporter(self):
        # LEFT and RIGHT
        if self.data[0].x >= self.right:
            self.data[0].x = self.left

        elif self.data[0].x <= self.left - 20:
            self.data[0].x = self.right - 20

        # UP and DOWN
        elif self.data[0].y <= self.top - 20:
            self.data[0].y = self.bottom - 20

        elif self.data[0].y >= self.bottom:
            self.data[0].y = self.top

    def snake_border(self):
        for _ in self.data[3:]:
            if not self.snake.flickering_animation:
                if self.snake.GO_UP == 0 and self.snake.GO_FORWARD == 20:
                    if (self.data[0].x, self.data[0].y) == (_.x - 20, _.y):
                        self.flickering_animation()

                elif self.snake.GO_UP == 0 and self.snake.GO_FORWARD == -20:
                    if (self.data[0].x, self.data[0].y) == (_.x + 20, _.y):
                        self.flickering_animation()

                elif self.snake.GO_UP == 20 and self.snake.GO_FORWARD == 0:
                    if (self.data[0].x, self.data[0].y) == (_.x, _.y - 20):
                        self.flickering_animation()

                elif self.snake.GO_UP == -20 and self.snake.GO_FORWARD == 0:
                    if (self.data[0].x, self.data[0].y) == (_.x, _.y + 20):
                        self.flickering_animation()

    def flickering_animation(self):
        for x in range(5):
            self.snake.flickering_animation = True
            self.screen.fill(BLACK)
            self.food.put_food()
            pygame.display.flip()
            pygame.time.delay(150)
            self.snake.movement()
            self.food.put_food()
            pygame.display.flip()
            pygame.time.delay(150)
        pygame.time.delay(200)


if __name__ == '__main__':

    def draw_window():
        screen.fill(BLACK)


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    game_on = True
    while game_on:
        clock.tick(10)

        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                game_is_on = False
                quit()
        draw_window()
        pygame.display.update()
