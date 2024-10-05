import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
joysticks: list[pygame.joystick.Joystick] = [pygame.joystick.Joystick(j) for j in range(pygame.joystick.get_count())]

x1, y1 = 0, 0
x2, y2 = 0, 0
win_size: tuple[int, int] = pygame.display.get_window_size()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joysticks.append(pygame.joystick.Joystick(event.device_index))
        if event.type == pygame.QUIT:
            run = False

    x1 = joysticks[0].get_axis(0)
    y1 = joysticks[0].get_axis(1)
    x2 = joysticks[0].get_axis(2)
    y2 = joysticks[0].get_axis(3)
    rt = (joysticks[0].get_axis(4) + 1.0) / 2
    lt = (joysticks[0].get_axis(5) + 1.0) / 2
    if abs(x1) < .05:
        x1 = 0
    if abs(y1) < .05:
        y1 = 0
    if abs(x2) < .05:
        x2 = 0
    if abs(y2) < .05:
        y2 = 0
    # print(f"{x1}\t{y1}\t{x2}\t{y2}\t{rt}\t{lt}")

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(int(x1 * (win_size[0] / 2) + win_size[0] / 2),
                                                      int(y1 * (win_size[1] / 2) + win_size[1] / 2), 10, 10))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(int(x2 * (win_size[0] / 2) + win_size[0] / 2),
                                                      int(y2 * (win_size[1] / 2) + win_size[1] / 2), 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 5, rt * win_size[0], 10))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 20, lt * win_size[0], 10))
    pygame.display.update()
    clock.tick()
    pygame.display.set_caption(f"{round(clock.get_fps())}")
