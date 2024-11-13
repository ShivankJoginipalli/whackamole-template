import pygame
import random

def main():
    try:
        red = (255, 0, 0)
        Sqsize = 32
        xran = 0
        yran = 0
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

                    if (xran,yran) == (event.pos[0]//32, event.pos[1]//32):

                        xran = random.randrange(0,20)
                        yran = random.randrange(0,16)
            screen.fill("light green")
            for row in range(16):  # 16 rows
                for col in range(20):  # 20 columns

                    x = col * Sqsize
                    y = row * Sqsize

                    pygame.draw.rect(screen, red, (x, y, Sqsize, Sqsize), 1)

            screen.blit(mole_image, mole_image.get_rect(topleft=(xran * 32, yran * 32)))
            if pygame.mouse.get_pressed() == (xran, yran):
                print("clicked the mole")
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
