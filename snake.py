import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
changed_direction = False


class Snake:
    def __init__(self, surface):
        self.screen = surface
        self.flickering_animation = False
        self.extension_req = False
        self.snake_length = 10
        self.GO_FORWARD = 20
        self.GO_UP = 0
        self.snake_data = []
        self.start_move_x, self.start_move_y = 300, 300
        self.creation()

    def creation(self):
        snake_x, snake_y = self.start_move_x, self.start_move_y

        for x in range(self.snake_length):
            self.body_development(snake_x, snake_y)
            snake_x -= 20

    def movement(self):
        # Snake Head
        global changed_direction
        changed_direction = False
        if not self.flickering_animation:
            last_head_x = self.snake_data[0].x
            last_head_y = self.snake_data[0].y
            self.snake_data[0].move_ip(self.GO_FORWARD, self.GO_UP)
        pygame.draw.rect(self.screen, RED, self.snake_data[0])
        # Snake Body
        for _ in range(1, len(self.snake_data)):
            if not self.flickering_animation:
                last_body_x = self.snake_data[_].x
                last_body_y = self.snake_data[_].y
                self.snake_data[_].x = last_head_x
                self.snake_data[_].y = last_head_y
                last_head_x = last_body_x
                last_head_y = last_body_y

            # TAIL SECTION
            if _ == len(self.snake_data) - 1:
                if not self.flickering_animation:
                    # Store the part before tail data
                    follow_up_x = self.snake_data[_ - 1].x
                    follow_up_y = self.snake_data[_ - 1].y
                    # Tail Follow Mechanism Was a Big Headache
                    if self.snake_data[_].x < follow_up_x:
                        self.snake_data[_].x += 8
                    elif self.snake_data[_].x > follow_up_x:
                        self.snake_data[_].x -= 8
                    elif self.snake_data[_].y < follow_up_y:
                        self.snake_data[_].y += 8
                    elif self.snake_data[_].y > follow_up_y:
                        self.snake_data[_].y -= 8
                pygame.draw.rect(self.screen, WHITE, self.snake_data[_], border_radius=10)
            else:
                pygame.draw.rect(self.screen, WHITE, self.snake_data[_])

    def direction(self, key):
        global changed_direction
        # GO UP
        if not changed_direction:
            if key == 1073741906 and self.GO_UP != 20:
                self.GO_FORWARD = 0
                self.GO_UP = -20
                changed_direction = True
            # GO DOWN
            elif key == 1073741905 and self.GO_UP != -20:
                self.GO_FORWARD = 0
                self.GO_UP = 20
                changed_direction = True
            # GO LEFT
            elif key == 1073741904 and self.GO_FORWARD != 20:
                self.GO_FORWARD = -20
                self.GO_UP = 0
                changed_direction = True
            # GO RIGHT
            elif key == 1073741903 and self.GO_FORWARD != -20:
                self.GO_FORWARD = 20
                self.GO_UP = 0
                changed_direction = True

    def extend(self):
        self.extension_req = True

        self.body_development(self.snake_data[0].x,
                              self.snake_data[0].y)

    def body_development(self, snake_x, snake_y):
        SNAKE = pygame.Rect(snake_x, snake_y, 20, 20)
        if self.extension_req:
            self.snake_data.insert(1, SNAKE)
        else:
            self.snake_data.append(SNAKE)


if __name__ == '__main__':
    def draw_window():
        screen.fill(BLACK)


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    snake = Snake(screen)
    game_on = True
    while game_on:
        clock.tick(10)
        for Event in pygame.event.get():
            if Event.type == pygame.KEYDOWN:
                snake.direction(Event.key)
            if Event.type == pygame.QUIT:
                game_is_on = False
                quit()
        draw_window()
        snake.movement()
        pygame.display.update()
