import os
import sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')


def load_image(name, colorkey=None):
    fullname = name  # os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('images/enemy1.gif', -1)
        self.x_dist, self.y_dist = 0, 5
        self.pos = (10.0, 10.0)
        self.rect.center = self.pos
        self.health = 100

    def update(self):
        pass


class Raptor(pygame.sprite.Sprite):

    images = {'left': 'images/plane_turning_right_1.gif',
              'right': 'images/plane_turning_left_1.gif',
              'straight': 'images/plane.gif'}

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(self.images['straight'], -1)
        self.rect.center = 55, 100
        self.x_dist, self.y_dist = 5, 5

    def update(self, event):
        x_move = 0
        y_move = 0


class RaptorMain:

    def __init__(self, width=440, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.score = 0

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.raptor_sprites.draw(self.screen)

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Score: %d" % self.score, 1, (255, 0, 0))
            textpos = text.get_rect(centerx=self.width/2)
            self.screen.blit(text, textpos)

        pygame.display.flip()

    def update_scene(self):
        pass

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                self.raptor.update(event)

    def main_loop(self):
        pygame.key.set_repeat(500, 30)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        self.load_sprites()

        while 1:
            self.handle_keys()
            self.update_scene()
            self.draw()

    def load_sprites(self):
        self.raptor = Raptor()
        self.raptor_sprites = pygame.sprite.RenderPlain((self.raptor))


if __name__ == "__main__":
    main_window = RaptorMain()
    main_window.main_loop()
