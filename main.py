import pygame
import random
import math
from constants import *
from point import Point
from triangle import Triangle

screen = None
timer = None

sphere = None
light = None
direction = None
player = None

segments = 100
rings = 100

def generate_sphere():
    global segments, rings
    vertices = []
    triangles = []

    for ring in range(rings + 1):
        theta = ring * math.pi / rings
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)

        for segment in range(segments + 1):
            phi = segment * 2 * math.pi / segments
            x = RADIUS * sin_theta * math.cos(phi)
            y = RADIUS * cos_theta
            z = RADIUS * sin_theta * math.sin(phi)
            vertices.append(Point(x + sphere.x, y + sphere.y, z + sphere.z))

    for ring in range(rings):
        for segment in range(segments):
            first = (ring * (segments + 1)) + segment
            second = first + segments + 1

            triangles.append(Triangle(vertices[first], vertices[second], vertices[first+1]))
            triangles.append(Triangle(vertices[second], vertices[second+1], vertices[first+1]))

    return triangles

def draw():
    global screen, player, direction
    screen.fill(BACKGROUND_COLOR)

    direction = Point(sphere.x - light.x, sphere.y - light.y, sphere.z - light.z)
    direction.normalize()

    triangles = generate_sphere()
    for t in triangles:
        n = t.normal()
        if n.z >= 0:
            continue
        
        dot = Point.dot(direction, n)
        if dot >= 0:
            continue

        brightness = abs(dot) * 255
        color = (brightness, brightness, brightness)
        points = [(t.A.x, t.A.y), (t.B.x, t.B.y), (t.C.x, t.C.y)]
        pygame.draw.polygon(screen, color, points)

def main():
    global player, screen, timer, light, sphere, segments, rings

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sphere Render")
    timer = pygame.time.Clock()

    sphere = Point(WIDTH/2, HEIGHT/2, 500)
    player = Point(WIDTH/2, HEIGHT/2, 0)
    x, y = pygame.mouse.get_pos()
    light = Point(x, y, 0)

    change = False
    run = True
    while run:
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    run = False
                    break
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    change = True
                    segments += 1
                    rings += 1
                elif event.button == 5:  # Scroll down
                    change = True
                    segments -= 1
                    rings -= 1
                    if segments < MIN_SEGMENTS:
                        segments = MIN_SEGMENTS
                    if rings < MIN_RINGS:
                        rings = MIN_RINGS

            # Detect mouse movement
            if event.type == pygame.MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                y = -y + HEIGHT
                x = WIDTH - x
                light = Point(x, y, 0)
                change = True

        if change:
            draw()
            pygame.display.flip()

        change = False
    
    pygame.quit()

if __name__ == '__main__':
    main()
