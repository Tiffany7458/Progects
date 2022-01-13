# Pygame Boilerplate
# Author:
# 2021 Version

import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 100)
BGCOLOUR = (160, 205, 150)

SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 800
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "DVD Screen Saver"

class Dvdimage:
    """Represents a Dvdimage on screen

    Attributes:
        x, y: coordinates of top-left corner
        width: width of image in px
        height: height of image in px
        x-vel: x velocity in px/sec
        y-vel: y velocity in px/sec
        """

    def __init__(self):
        self.x, self.y = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.width = 313
        self.height = 138
        self.img = pygame.image.load("./images/dvd-logo-png-15.png")
        self.colour = RED
        self.x_vel = 5
        self.y_vel = 3

    def rect(self) ->pygame.rect:
        """Returns a pygame.rect that represents the dvd_image"""
        return [self.x, self.y, self.width, self.height]

    def update(self) -> None:
        """Updates the Dvdimage with every tick"""
        # Update the x-coordinate
        self.x += self.x_vel
        # If Dvdimage is too far to the left
        if self.x < 0:
            # Keep the object inside the canvas
            self.x = 0
            # Set the velocity to the negative
            self.x_vel = -self.x_vel
        # If Dvdimage is too far to the right
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
            self.x_vel = -self.x_vel

        self.y += self.y_vel
        if self.y < 0:
            self.y = 0
            self.y_vel = -self.y_vel
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.y_vel = -self.y_vel

def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    dvd_image = Dvdimage()

    bg_image = pygame.image.load('./images/sea.jpg')
    bg_image = pygame.transform.scale(bg_image, (1000, 800))
    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT
        dvd_image.update()

        # ----------- DRAW THE ENVIRONMENT
        screen.blit(bg_image, (0, 0))

        screen.blit(dvd_image.img, (dvd_image.x, dvd_image.y))

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(200)


if __name__ == "__main__":
    main()

