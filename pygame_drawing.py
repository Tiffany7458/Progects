import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE = "Pygame Drawing"
def main() -> None:
    """Driver of the python script"""
    # create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    # create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    # ---- main loop
    while not  done:
        # ---- event listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ---- change environment

        # ---- draw the environment
        screen.fill(WHITE) # fill with bgcolor
        # update the screen
        pygame.display.flip()
        # ---- clock tick
        clock.tick(75)

if __name__ == "__main__":
    main()