import sys

import pygame
from snake import Snake
from food import Food
from border import Border
from scoreboard import ScoreBoard

FPS = 10
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("                                                              Snake By Tahmid Newaz")


def draw_window():
    screen.fill(BLACK)


def main():
    snake = Snake(screen)
    food = Food(screen, snake)
    border = Border(snake, screen, food)
    scoreboard = ScoreBoard(screen, snake)
    clock = pygame.time.Clock()
    game_is_on = True
    while game_is_on:
        clock.tick(FPS)
        for Event in pygame.event.get():
            if Event.type == pygame.KEYDOWN:
                snake.direction(Event.key)
                if Event.key == pygame.K_r:
                    main()
            if Event.type == pygame.QUIT:
                sys.exit()
        if snake.snake_data[0].colliderect(food.food):
            food.cook()
            snake.extend()
            scoreboard.score += 1
        border.snake_border()
        border.transporter()
        draw_window()
        snake.movement()
        food.put_food()
        scoreboard.show_score()
        pygame.display.update()


main()
