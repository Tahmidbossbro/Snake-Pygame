import pygame
from snake import Snake

pygame.font.init()
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class ScoreBoard:
    def __init__(self, surface, snake_1):
        self.screen = surface
        self.snake = snake_1
        self.score = 0
        try:
            with open("score.txt", "r") as file:
                self.high_score = file.read()
        except FileNotFoundError:
            self.high_score = 0
        self.font = pygame.font.SysFont('Times New Roman', 40)

    def show_score(self):
        if not self.snake.flickering_animation:
            self.screen.blit(self.font.render(f"{self.score}",
                                              False, RED), (0, 0))

        else:
            if self.score > int(self.high_score):
                self.high_score = self.score

                with open("score.txt", "w+") as file:
                    file.write(str(self.score))
            self.screen.blit(self.font.render(f"Final Score: {self.score}"
                                              f"  (Press R to Restart)", False, RED), (0, 0))
            self.screen.blit(self.font.render(f"High Score: {self.high_score}",
                                              False, RED), (0, 50))


if __name__ == '__main__':

    def draw_window():
        screen.fill(BLACK)


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 600))
    snake = Snake(screen)
    scoreboard = ScoreBoard(screen, snake)
    game_on = True
    while game_on:
        clock.tick(10)

        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                game_is_on = False
                quit()
        draw_window()
        scoreboard.show_score()
        pygame.display.update()
