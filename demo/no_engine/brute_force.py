import math
import random
import time
from collections import deque
from typing import Tuple, List

VectorType = List[float]


def run_no_engine_brute_force(dimension: Tuple[int, int], n_particles: int, radius: float):
    radius2 = radius ** 2
    radius_ceil = math.ceil(radius)

    import pygame
    pygame.init()

    # noinspection PyTypeChecker
    font = pygame.font.SysFont(None, 24)

    random.seed(99123)
    positions: List[VectorType] = [
        [random.randint(radius_ceil, dimension[0] - radius_ceil),
         random.randint(radius_ceil, dimension[1] - radius_ceil)]
        for _ in range(n_particles)]
    velocities: List[VectorType] = [[random.random() * radius - radius / 2, random.random() * radius - radius / 2]
                                    for _ in range(n_particles)]
    screen = pygame.display.set_mode(dimension)
    pygame.event.set_allowed([pygame.QUIT])
    clock = pygame.time.Clock()
    timestamps = deque()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        timestamps.append(time.time())
        for i in range(len(positions)):
            if positions[i][0] <= radius:
                positions[i][0] = radius
                velocities[i][0] = -velocities[i][0]
            if positions[i][1] <= radius:
                positions[i][1] = radius
                velocities[i][1] = -velocities[i][1]
            if dimension[0] - radius <= positions[i][0]:
                positions[i][0] = dimension[0] - radius
                velocities[i][0] = -velocities[i][0]
            if dimension[1] - radius <= positions[i][1]:
                positions[i][1] = dimension[1] - radius
                velocities[i][1] = -velocities[i][1]
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]

        for i, (x, y) in enumerate(positions):
            for j, (p, q) in enumerate(positions[i + 1:], i + 1):
                dx, dy = p - x, q - y
                if abs(dx) > 2 * radius and abs(dy) > 2 * radius:
                    continue
                dist2 = dx ** 2 + dy ** 2
                if dist2 > 4 * radius2:
                    continue

                dist = dist2 ** 0.5
                move_dist = radius - dist / 2
                p_cos, p_sin = dx / dist, dy / dist
                mx, my = p_cos * move_dist, p_sin * move_dist
                positions[i][0] -= mx
                positions[i][1] -= my
                positions[j][0] += mx
                positions[j][1] += my

                dist2 = 4 * radius2
                dx, dy = positions[j][0] - positions[i][0], positions[j][1] - positions[i][1]
                dvx, dvy = velocities[j][0] - velocities[i][0], velocities[j][1] - velocities[i][1]
                # dv = (dvx ** 2 + dvy ** 2) ** 0.5
                # v_cos, v_sin = dvx / dv, dvy / dv
                # v_mul = (dvx * dx + dvy * dy) / dist2
                velocities[i][0] += (dvx * dx + dvy * dy) / dist2 * dx
                velocities[i][1] += (dvx * dx + dvy * dy) / dist2 * dy
                velocities[j][0] -= (dvx * dx + dvy * dy) / dist2 * dx
                velocities[j][1] -= (dvx * dx + dvy * dy) / dist2 * dy

        n_timestamps = len(timestamps)
        if n_timestamps > 30:
            timestamps.popleft()

        screen.fill("white")
        for pos in positions:
            pygame.draw.circle(screen, "red", pos, radius=radius)

        ups = (n_timestamps - 1) / (timestamps[-1] - timestamps[0]) if n_timestamps > 1 else 0.
        img = font.render(f"{ups:.1f} UPS", True, "blue")
        rect = img.get_rect()
        screen.blit(img, (dimension[0] - rect.w - 20, 20))

        clock.tick(15)
        pygame.display.flip()

    pygame.quit()
