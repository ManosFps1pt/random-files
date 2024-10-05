import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

v2 = pygame.Vector2

pos = v2(100, 100)

while True:
    clock.tick(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("#000000")
    mouse_pos = v2(pygame.mouse.get_pos())
    pos.move_towards_ip(mouse_pos, 800)
    pygame.draw.circle(screen, "#aa0000", pos,  30)

    pygame.display.update()
    clock.tick(60)
