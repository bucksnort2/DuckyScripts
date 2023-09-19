try:
    import pygame
except:
    import os
    try:
        os.system("py -m pip install pygame") 
    except:
        os.system("python -m pip install pygame")
    import pygame   
import random
import sys  # Import sys module for exit handling

pygame.init()

infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Prank!")

font = pygame.font.SysFont("Arial", 64)

running = True  # Flag to control the main loop

while running:  # Main game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop when the window is closed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Exit the loop when the ESC key is pressed

    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    text = font.render(":-) RUBBER DUCKS WILL TAKE OVER THE OCEANS! (-: )", True, text_color)

    x_offset = random.randint(-50, 50)
    y_offset = random.randint(-50, 50)
    text_rect = text.get_rect()
    text_rect.center = (screen_width//2 + x_offset, screen_height//2 + y_offset)

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()  # Clean up pygame
sys.exit()  # Exit the script
