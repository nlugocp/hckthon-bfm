import pygame, time, random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True

#test image
test_image = pygame.image.load("pixel.png")
test_image = pygame.transform.scale(test_image, (25, 25))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("brown")

    #box where gameplay will occur
    pygame.draw.line(screen, (255, 255, 255), (100, 50), (900, 50)) #top line
    pygame.draw.line(screen, (255, 255, 255), (100, 450), (900, 450)) #bottom line
    pygame.draw.line(screen, (255, 255, 255), (100, 50), (100, 450)) # elft line
    pygame.draw.line(screen, (255, 255, 255), (900, 50), (900, 450)) #right line

    # RENDER YOUR GAME HERE
    screen.blit(test_image, (750, 250))


    # flip() the display to put your work on screen
    pygame.display.flip()



    clock.tick(60)  # limits FPS to 60

pygame.quit() 
