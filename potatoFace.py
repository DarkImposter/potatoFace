import pygame
from random import randint, choice, shuffle, uniform
pygame.init()
width = 1000
height = 700
s = pygame.display.set_mode((width,height))
progress = True
potatoHeight =  105
potatoWidth = 105
x = (width/2)
y = (height/2)
startX = (width/2)
startY = (height/2)

print("ok ok ok")

class base_sprite(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        if type(image) == pygame.Surface:
            self.image = image
        else:
            self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bullet(base_sprite):
    BULLETSPRITES = [pygame.image.load("bullet.png")];
    def __init__(self,x,y):
        randBulletImage = self.getRandBullet()
        super().__init__(x,y,randBulletImage)
    def getRandBullet(self):
        return choice(Bullet.BULLETSPRITES)

potatoFacei = pygame.image.load("potatoFace.png")
startButtoni = pygame.image.load("startButton.png")
back = pygame.image.load("back.png")
bulleti = pygame.image.load("bullet.png")
dan1i = pygame.image.load("dan1.png")
dan2i = pygame.image.load("dan2.png")
dan3i = pygame.image.load("dan3.png")
dan4i = pygame.image.load("dan4.png")
dan5i = pygame.image.load("dan5.png")
dan6i = pygame.image.load("dan6.png")
dan7i = pygame.image.load("dan7.png")
dan8i = pygame.image.load("dan8.png")
# bullet0 = base_sprite(image = bulleti, xk = x, yk = y)

potatoFace = base_sprite(image = potatoFacei, x = x, y = y)
startButton = base_sprite(image = startButtoni, x = (startX-200), y = (startY-100))
dan1 = base_sprite(image = dan1i, x = randint(0,(1000-104)), y = 0)
dan2 = base_sprite(image = dan2i, x = randint(0,(1000-105)), y = 0)
dan3 = base_sprite(image = dan3i, x = randint(0,(1000-105)), y = 0)
dan4 = base_sprite(image = dan4i, x = randint(0,(1000-105)), y = 0)
dan5 = base_sprite(image = dan5i, x = randint(0,(1000-105)), y = 0)
dan6 = base_sprite(image = dan6i, x = randint(0,(1000-105)), y = 0)
dan7 = base_sprite(image = dan7i, x = randint(0,(1000-105)), y = 0)
dan8 = base_sprite(image = dan8i, x = randint(0,(1000-105)), y = 0)
danials = [dan1, dan2, dan3, dan4, dan5, dan6, dan7]

home = pygame.sprite.Group()
badGuys = pygame.sprite.Group()
fire = pygame.sprite.Group()

points = 0
running = False
start = True
xmin = False
xplus = False
ymin = False
yplus = False

while start:


    home.add(startButton)
    home.draw(s)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    start = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startButton.rect.collidepoint(event.pos):
                        print("harrison")
                        running = True
                        start = False
                        home.remove(startButton)
    home.draw(s)
    pygame.display.update()
    pygame.display.flip()
while running:
    home.add(potatoFace)
    home.draw(s)
    fire.draw(s)
    badGuys.draw(s)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    start = True
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_LEFT):
                                xmin = True
                        if (event.key == pygame.K_RIGHT):
                                xplus = True
                        if (event.key == pygame.K_UP):
                                ymin = True
                        if (event.key == pygame.K_DOWN):
                                yplus = True
                        if (event.key == pygame.K_z):
                            if len(fire) < 15:
                                    num = len(fire)
                                    fire.add(Bullet((potatoFace.rect.x+55),potatoFace.rect.y+35))




                if event.type == pygame.KEYUP:
                        if (event.key == pygame.K_LEFT):
                                xmin = False
                        if (event.key == pygame.K_RIGHT):
                                xplus = False
                        if (event.key == pygame.K_UP):
                                ymin = False
                        if (event.key == pygame.K_DOWN):
                                yplus = False

    #enemies
    thisDan = danials[randint(0,(len(danials)-1))]
    if len(badGuys) < 4 and randint(1,70) == 4:
        badGuys.add(thisDan)
    for i in badGuys:
        i.rect.y += 5
        if i.rect.y > 610:
            running = False
            start = True
        col = pygame.sprite.spritecollide(i, fire, dokill = True)
        if col:
            badGuys.remove(i)
            points += 1
            i.rect.y = 0
            i.rect.x = randint(0,(1000-105))
            print("you have "+str(points)+" points!")




    if xmin:
            potatoFace.rect.x -= 10
            if potatoFace.rect.x <= -10:
                    potatoFace.rect.x = -10
    if xplus:
            potatoFace.rect.x += 10
            if potatoFace.rect.x >=  (width-(potatoWidth - 10)):
                    potatoFace.rect.x = (width - (potatoWidth - 10))
    if ymin:
            potatoFace.rect.y -= 10
            if potatoFace.rect.y <= 0:
                    potatoFace.rect.y = 0
    if yplus:
            potatoFace.rect.y += 10
            if potatoFace.rect.y >= ((height)-(potatoHeight)):
                    potatoFace.rect.y = ((height) - (potatoHeight))
    if len(fire) > 0:
        for i in fire:
                i.rect.y -= 5
                if i.rect.y <= (0 - 16):
                    fire.remove(i)

    s.blit(back, (0,0))
    home.draw(s)
    badGuys.draw(s)
    fire.draw(s)
    pygame.display.update()
    pygame.display.flip()
