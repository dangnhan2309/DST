import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag & Drop in Pygame")

# Load image (replace with your own asset)
object_img = pygame.image.load("D.png")  # Ensure this file exists
object_rect = object_img.get_rect(topleft=(100, 100))

dragging = False

# Main loop
running = True
while running:
    screen.fill((30, 30, 30))  # Background color
    screen.blit(object_img, object_rect.topleft)  # Draw object

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect Mouse Click (Start Drag)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if object_rect.collidepoint(event.pos):
                dragging = True
                offset_x, offset_y = event.pos[0] - object_rect.x, event.pos[1] - object_rect.y

        # Detect Mouse Movement (Dragging)
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                object_rect.x = event.pos[0] - offset_x
                object_rect.y = event.pos[1] - offset_y

        # Detect Mouse Release (Drop)
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    pygame.display.update()

pygame.quit()
