from typing import Tuple

from demo.game.state import GameStateManager


def loop(dimension: Tuple[int, int], state: GameStateManager):
    import pygame
    pygame.init()
    # noinspection PyTypeChecker
    font = pygame.font.SysFont(None, 24)

    screen = pygame.display.set_mode(dimension)
    pygame.event.set_allowed([pygame.QUIT])
    clock = pygame.time.Clock()

    running = True
    while running:
        current_state = state.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        for pos in current_state.positions:
            pygame.draw.circle(screen, "red", pos, 1.)

        img = font.render(f"{current_state.ups:.1f} UPS", True, "blue")
        rect = img.get_rect()
        screen.blit(img, (dimension[0] - rect.w - 20, 20))

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()
