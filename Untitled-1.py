#импорт
from pygame import *
from random import randint
game = True
okno = display.set_mode((640,480))
fon = transform.scale(image.load("images.jpg"), (640, 480))
#
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (55, 55))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
     def reset(self):
         okno.blit(self.image, (self.rect.x, self.rect.y))
class GameSprite2(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (10, 155))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
     def reset(self):
         okno.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite2):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
class Player2(GameSprite2):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
ss = GameSprite("unnamed.png",320,240,3)
pp = Player("Без названия.png",10,20,6)
pp2 = Player2("Без названия.png",580,20,6)
dx=1
dy=0
while game:

    if sprite.collide_rect(ss, pp2):
        dx*=-1 
        dy= randint(-5,5)
    if sprite.collide_rect(ss, pp):
        dx*=-1 
        dy= randint(-5,5)
    ss.rect.x+=dx
    ss.rect.y-=dy
    if ss.rect.y < 0:
        dy *= -1
    if ss.rect.y > 430:
        dy *= -1
    for e in event.get():
            if e.type == QUIT:
                game = False
    okno.blit(fon,(0, 0))
    ss.reset()
    ss.update()
    pp.reset()
    pp.update()
    pp2.reset()
    pp2.update()
    display.update()
    if ss.rect.x > 640:
        game = False
    if ss.rect.x < 0:
        game = False