import random

# Define constants for the map size and tile types
MAP_WIDTH = 10
MAP_HEIGHT = 10
TILE_GRASS = 0
TILE_WATER = 1
TILE_TREE = 2

# Create an empty map
map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

def generate_map():
    # Generate the map

    # Fill the map with grass
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            map[y][x] = TILE_GRASS

    # Add some water tiles
    for _ in range(10):
        x = random.randrange(MAP_WIDTH)
        y = random.randrange(MAP_HEIGHT)
        map[y][x] = TILE_WATER

    # Add some tree tiles
    for _ in range(10):
        x = random.randrange(MAP_WIDTH)
        y = random.randrange(MAP_HEIGHT)
        map[y][x] = TILE_TREE
