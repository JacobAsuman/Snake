import pygame
import random

pygame.init()
window_height = 600
window_width = 600
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
font_style = pygame.font.SysFont(None, 30)


def my_Snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(SCREEN, blue, (i[0], i[1], snake_block, snake_block))


def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    SCREEN.blit(mesg, [5, 100])


def score_message(score):
    sc = font_style.render("Score: " + str(score), True, white)
    SCREEN.blit(sc, [0, 0])


def main():
    pygame.init()
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((window_width, window_height))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(black)
    x = window_width / 2
    y = window_height / 2
    snake_speed = 15
    snake_block = 15
    food_block = 12
    xVel = 0
    yVel = 0
    snake_List = []
    snake_Length = 1
    game_over = False
    game_close = False
    food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    score = 0

    while not game_over:
        while game_close:
            SCREEN.fill(white)
            message("You Lost - Press Q-Quit or R-Play Again!", blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xVel = -snake_speed
                    yVel = 0
                if event.key == pygame.K_RIGHT:
                    xVel = snake_speed
                    yVel = 0
                if event.key == pygame.K_UP:
                    xVel = 0
                    yVel = -snake_speed
                if event.key == pygame.K_DOWN:
                    xVel = 0
                    yVel = snake_speed
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_close = True

        x += xVel
        y += yVel
        SCREEN.fill(black)
        pygame.draw.rect(SCREEN, white, [food_x, food_y, food_block, food_block])
        pygame.draw.rect(SCREEN, blue, [x, y, snake_block, snake_block])
        score_message(score)
        snake_Head = [int(x), int(y)]
        snake_List.append(snake_Head)
        if len(snake_List) > snake_Length:
            del snake_List[0]

        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close = True
        my_Snake(snake_block, snake_List)
        pygame.display.update()

        if food_x - food_block <= x <= food_x + food_block and food_y - food_block <= y <= food_y + food_block:  # checks collision of area of food block
            food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            snake_Length += 1
            score += 1

        CLOCK.tick(snake_speed)


main()
