import pygame
import random
import os


# TODO  collect images, resize if needed, fill screen as best as possible


# set up assets (art, sound, ect)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
pic = '1g3ccn556nl31.jpg'


class Picture(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(game_folder, pic)).convert()
        # self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        print(self.image.get_size())

        
fps = 30
WIDTH, HEIGHT = 1024, 768
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# image = pygame.transform.scale(image, (1024, 768))

all_sprites = pygame.sprite.Group()
picture = Picture()
all_sprites.add(picture)

clock = pygame.time.Clock()
running= True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
