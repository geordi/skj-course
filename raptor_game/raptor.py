import os
import sys
import pygame
from pygame.locals import *

DIR_UP = 1
DIR_DOWN = -1

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')


def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('images/bullet.gif', -1)
        self.direction = direction
        self.rect.center = pos
        self.damage = 10

    def update(self):
        if self.direction == DIR_DOWN:
            move_y = 1
        elif self.direction == DIR_UP:
            move_y = -1

        self.rect.move_ip(0, move_y)

        _, b_y = self.rect.center
        if b_y <= 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('images/enemy1.gif', -1)
        self.pos = pos
        self.rect.center = self.pos
        self.health = 100
        self.score_for_kill = 10

    def update(self):
        pos_x, pos_y = self.pos
        pos_y += 0.1
        self.pos = (pos_x, pos_y,)
        self.rect.center = (round(pos_x), round(pos_y))


class Raptor(pygame.sprite.Sprite):

    images = {'left': 'images/plane_turning_right_1.gif',
              'right': 'images/plane_turning_left_1.gif',
              'straight': 'images/plane.gif'}

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(self.images['straight'], -1)
        self.rect.center = pos
        self.x_dist, self.y_dist = 5, 5

    def update(self, event):
        move_x = 0
        move_y = 0

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                move_x = self.x_dist
                center = self.rect.center
                self.image, self.rect = load_image(self.images['right'], -1)
                self.rect.center = center
            elif event.key == K_LEFT:
                move_x = -self.x_dist
                center = self.rect.center
                self.image, self.rect = load_image(self.images['left'], -1)
                self.rect.center = center
            elif event.key == K_UP:
                move_y = -self.y_dist
            elif event.key == K_DOWN:
                move_y = self.y_dist
        elif event.type == KEYUP:
            center = self.rect.center
            self.image, self.rect = load_image(self.images['straight'], -1)
            self.rect.center = center

        self.rect.move_ip(move_x, move_y)

    def create_bullet(self):
        bullet = Bullet(self.rect.center, DIR_UP)
        return bullet


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
        self.enemy_sprites.draw(self.screen)
        if self.bullet_sprites is not None:
            self.bullet_sprites.draw(self.screen)

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render('Score: {}'.format(self.score), 1, (255, 0, 0))
            textpos = text.get_rect(centerx=self.width/2)
            self.screen.blit(text, textpos)

        pygame.display.flip()

    def update_scene(self):
        self.enemy.update()
        self.bullet_sprites.update()

        for bullet in self.bullet_sprites:
            lst_cols = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False)

            for col_obj in lst_cols:
                col_obj.health -= bullet.damage
                if col_obj.health <= 0:
                    col_obj.kill()
                    self.score += col_obj.score_for_kill

            if lst_cols != []:
                bullet.kill()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN or event.type == KEYUP:
                self.raptor.update(event)

                if event.key == K_SPACE:
                    self.bullet_sprites.add(self.raptor.create_bullet())

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
        self.raptor = Raptor((self.width/2, self.height - 20,))
        self.raptor_sprites = pygame.sprite.RenderPlain((self.raptor))
        self.enemy = Enemy((20.0, 10.0,))
        self.enemy_sprites = pygame.sprite.RenderPlain((self.enemy))
        self.bullet_sprites = pygame.sprite.RenderPlain()


if __name__ == '__main__':
    main_window = RaptorMain()
    main_window.main_loop()
