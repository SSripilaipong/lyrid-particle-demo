def loop():
    import pygame
    pygame.init()

    display = pygame.display.set_mode((1_200, 760))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((255, 255, 255))

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()
