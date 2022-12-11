import pygame
import random

FRAME_RATE = 60
PLAYER_SPEED = 2
clock = pygame.time.Clock()
RESOLUTION_X = 500
RESOLUTION_Y = 300

def generate_map(width, height):
    # Create an empty map
    map = []
    for i in range(height):
        map.append([])
        for j in range(width):
            map[i].append(0)

    # Add random obstacles to the map
    for i in range(height):
        for j in range(width):
            if random.random() < 0.1:
                map[i][j] = 1

    # Return the generated map
    return map

# Define the Player class
class Player:
    def __init__(self, x, y):
        # Initialize the player's position
        self.x = x
        self.y = y

        # Load the player's image
        self.image = pygame.image.load("assets/images/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

    def handle_keys(self):
        # Get the keys that are currently being pressed
        keys = pygame.key.get_pressed()

        # Move the player based on the keys
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED

    def draw(self, screen):
        # Draw the player's image on the screen
        screen.blit(self.image, (self.x, self.y))

player = Player(10, 10)
def main():

    # Initialize Pygame and set up the window
    pygame.init()
    screen = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))
    pygame.display.set_caption("My Game")

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Load game assets (e.g. images, sounds)

    # Initialize game variables and objects

    # Main game loop
    running = True
    while running:
        # Handle events (keyboard input, mouse clicks, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

         # Update game objects and variables
        player.handle_keys()
        # Render the game (draw to the screen)
        screen.fill(BLACK)
        player.draw(screen)
        # Draw game objects here
        pygame.display.flip()
        clock.tick(FRAME_RATE)


    # Clean up and exit
    pygame.quit()   

main()
