from pygame import image


# Screen
WINDOW_WIDTH, WINDOW_HEIGHT = 900, 430

# Character menu
CHARACTER_MENU_X, CHARACTER_MENU_Y = 0, 0
CHARACTER_MENU_WIDTH, CHARACTER_MENU_HEIGHT = 50, WINDOW_HEIGHT
CHARACTER_WIDTH = CHARACTER_HEIGHT = CHARACTER_MENU_WIDTH

# health
HEALTH_WIDTH, HEALTH_HEIGHT = 400, 30
HEALTH_Y, HEALTH1_X, HEALTH2_X = CHARACTER_MENU_Y, CHARACTER_MENU_WIDTH, CHARACTER_MENU_WIDTH * 2 + HEALTH_WIDTH

# partition
PARTITION_X, PARTITION_Y =  CHARACTER_MENU_WIDTH + HEALTH_WIDTH, CHARACTER_MENU_Y
PARTITION_WIDTH, PARTITION_HEIGHT = CHARACTER_MENU_WIDTH, CHARACTER_MENU_HEIGHT

# maps
MAP_Y, MAP1_X, MAP2_X = HEALTH_HEIGHT, CHARACTER_MENU_WIDTH, CHARACTER_MENU_WIDTH + HEALTH_WIDTH + PARTITION_WIDTH
MAP_WIDTH = MAP_HEIGHT = HEALTH_WIDTH

# wave
WAVE_X, WAVE_Y = CHARACTER_MENU_WIDTH + MAP_WIDTH, CHARACTER_MENU_Y

# money
MONEY_X, MONEY_Y = WAVE_X, HEALTH_HEIGHT

# tile
TILE_WIDTH, TILE_HEIGHT = 20, 40

# images
PARTITION_IMAGE = CHARACTER_MENU_IMAGE = image.load('Draw/images/Partition.png')
VICTORY_IMAGE = image.load('Draw/images/victory.png')
DEFEAT_IMAGE = image.load('Draw/images/defeat.png')
