import pygame
import random
import time

pygame.init()

screenWidth = 1200

target_fps = 400

screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))
ball_pos = pygame.Vector2(600, 400)
ball_size = 20
pos_or_neg = (1, -1)
ball_speed_y = 0
ball_speed_x = -0.8
print(ball_speed_y)
run = True
prev_time = time.time()
dt = 0
racket_size = (15, 100)

start = False

# this is the game loop

player_pos = pygame.Vector2(10, 360)

enemy_pos = pygame.Vector2(screenWidth - 25, player_pos.y)

enemy_rect = pygame.Rect(enemy_pos, racket_size)

rect = pygame.Rect(player_pos, racket_size)

while run:

    screen.fill((0, 0, 0))

    key = pygame.key.get_pressed()

    # in this if is the game after the start screen

    while start:

        collider_pos = pygame.Vector2(ball_pos.x - ball_size / 2, ball_pos.y - ball_size / 2)

        now = time.time()

        dt = prev_time * -1 - now * -1

        prev_time = now

        screen.fill((0, 0, 0))

        player = pygame.draw.rect(screen, (0, 0, 255), rect)

        ball_collider = pygame.Rect((collider_pos), (ball_size / 4, ball_size / 4))

        pygame.draw.rect(screen, (0, 255, 0), ball_collider)

        ball = pygame.draw.circle(screen, (255, 0, 0), ball_pos, ball_size)

        enemy = pygame.draw.rect(screen, (0, 255, 0), enemy_rect)

        if enemy_pos.y >= screenHeight - racket_size[1]:
            enemy_pos.y = screenHeight - racket_size[1]

        if enemy_pos.y <= 0:
            enemy_pos.y = 0

        if ball_pos == (600, 400):
            ball_speed_y = random.random() * random.choice(pos_or_neg)

            print(ball_speed_y)

        if ball_pos.y > enemy_pos.y + racket_size[1] / 2:
            enemy_pos.y += 370 * dt

            enemy_rect.topleft = enemy_pos

        if ball_pos.y < enemy_pos.y + racket_size[1] / 2:
            enemy_pos.y -= 370 * dt

            enemy_rect.topleft = enemy_pos

        ball_pos.x += ball_speed_x

        ball_pos.y += ball_speed_y

        if ball_pos.x <= 0 + ball_size:
            ball_pos.y = 400

            ball_pos.x = 600

        if ball_pos.x >= screenWidth - ball_size:
            ball_pos.y = 400

            ball_pos.x = 600

        if ball_pos.y <= 0 + ball_size:
            ball_pos.y = ball_size

            ball_speed_y = -1 * ball_speed_y

        if ball_pos.y >= screenHeight - ball_size:
            ball_pos.y = screenHeight - ball_size

            ball_speed_y = -1 * ball_speed_y

        if ball_collider.colliderect(player):
            ball_speed_x = -1 * ball_speed_x

            ball_pos.x = player_pos.x + 26

        if ball_collider.colliderect(enemy):
            ball_speed_x = -1 * ball_speed_x

            ball_pos.x = enemy_pos.x - 26

            print("collided")

        key2 = pygame.key.get_pressed()

        if key2[pygame.K_w]:
            player_pos.y -= 1 * dt * target_fps

        if key2[pygame.K_s]:
            player_pos.y += 1 * dt * target_fps

        if player_pos.y <= 0:
            player_pos.y = 0

        if player_pos.y >= screenHeight - rect.height:
            player_pos.y = screenHeight - rect.height

        rect.topleft = player_pos

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = False

                run = False

            if key2[pygame.K_SPACE]:
                start = False

        pygame.display.update()

    # this is the event handler

    for event in pygame.event.get():

        if key[pygame.K_BACKSPACE]:
            start = True

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()