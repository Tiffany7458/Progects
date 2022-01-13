import random
import time
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
ETON_BLUE = (135, 187, 162)
RAD_RED = (255, 56, 100)
BLK_CHOCOLATE = (25, 17, 2)
BGCOLOUR = WHITE

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "Collecting Blocks"

class Player(pygame.sprite.Sprite):
    """Describes a player object
      A subclass of pygame.sprite.Sprite
      Attributes:
          image: Surface that is the visual
              representation of our Block
          rect: numerical representation of
              our Block [x, y, width, height]
      """
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("./images/mario.png")
        self.image = pygame.transform.scale(self.image, (42, 43))
        self.rect = self.image.get_rect()
        self.hp = 250

class Block(pygame.sprite.Sprite):
    """Describes a block object
    A subclass of pygame.sprite,Sprite

    Attributes:
        image: Surface that is the visual
            representation of our Block
        rect: numerical representation of
            our Block [x, y, width, height]
        """

    def __init__(self, colour: tuple, width: int, height: int) -> None:
        """
        Arguments:
        :param colour: 3-tuple (r, g, b)
        :param width: width in pixels
        :param height: height in pixels
        """
        # Call the superclass constructor
        super().__init__()

        # Create the image of the block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        # Based on the image, create a Rect for the block
        self.rect = self.image.get_rect()

class Enemy(pygame.sprite.Sprite):
    """The enemy sprites
       Attributes:
           image: Surface that is the visual representation
           rect: Rect (x, y, width, height)
           x_vel: x velocity
           y_vel: y velocity
       """
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/enemy.png")
        self.image = pygame.transform.scale(self.image, (91, 109))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (
            random.randrange(SCREEN_WIDTH),
            random.randrange(SCREEN_HEIGHT)
        )
        self.x_vel = random.choice([-4, -3, 3, 4])
        self.y_vel = random.choice([-4, -3, 3, 4])

    def update(self) -> None:
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.left < 0:
            self.rect.x = 0
            self.x_vel = -self.x_vel
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.x_vel = -self.x_vel
        if self.rect.y < 0:
            self.rect.y = 0
            self.y_vel = -self.y_vel
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.y_vel = -self.y_vel

def main(block_collided) -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()
    num_blocks = 100
    nun_enemies = 10
    score = 0
    time_start = time.time()
    time_invincible = 5
    game_state = "running"
    endgame_cooldown = 5
    time_ended = 0.0
    endgame_messages = {
        "win": "Congratulations, you won!"
        "lose": "Sorry, they got you. Play again!",
    }
    font = pygame.font.SysFont("Arial", 25)
    pygame.mouse.set_visible(False)

    all_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    for i in range(num_blocks):
        block = Block(BLACK, 20, 15)
        block.rect.x = random.randrange(SCREEN_WIDTH - block.rect.width)
        block.rect.y = random.randrange(SCREEN_HEIGHT - block.rect.height)
        block_sprites.add(block)
        all_sprites.add(block)

    for i in range(nun_enemies):
        enemy = Enemy()
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)

    player = Player()
    all_sprites.add(player)
    pygame.mouse.set_visible(True)
    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # End-game listener
        # WIN CONDITION - Collect 100 blocks
        if score == num_blocks:
            game_state = "won"
            if time_ended == 0:
                time_ended = time.time()
            if time.time() - time_ended >= endgame_cooldown:
                done = True

        if player.hp_remaining() <= 0:
            done = True



        # ----------- CHANGE ENVIRONMENT
        mouse_pos = pygame.mouse.get_pos()
        player.rect.x = mouse_pos[0] - player.rect.width / 2
        player.rect.y = mouse_pos[1] - player.rect.height / 2
        all_sprites.update()
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites, False)

        if time.time() - time_start > time_invincible:
            for enemy in enemies_collided:
                player.hp -= 1

            # Check all collisions between player and the blocks
            blocks_collided = pygame.sprite.spritecollide(player, block_sprites, True)

            for block in block_collided:
                score += 1
                print(f"Score: {score}")
        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        all_sprites.draw(screen)
        pygame.draw.rect(screen, BLUE, [480, 5, 115, 20])
        life_remaining = 215 - int(215 * player.hp_remaining() / 100)
        pygame.draw.rect(screen, GREEN, [580, 5, 215, 20])

        if game_state == "won":
            screen.blit(
                font.render(endgame_messages["wim"], True, BLACK),
                (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            )
        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()
