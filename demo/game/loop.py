from typing import Tuple

from demo.game.state import GameState


def loop(dimension: Tuple[int, int], state: GameState):
    import pygame
    pygame.init()

    display = pygame.display.set_mode(dimension)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill("white")
        positions = state.get_particle_positions()
        for pos in positions:
            pygame.draw.circle(display, "red", pos, 30.)

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()
