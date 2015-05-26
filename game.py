__author__ = "ben"

import pygame
size = 800, 600

class Shuttle(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("1.png")
        self.x = 270
        self.y = 400
        self.rect = self.image.get_rect()
class Player(pygame.sprite.Sprite): #changes the image and can be moved. Use if you want.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = 1
        self.image = pygame.image.load("1.png").convert()
        self.rect = self.image.get_rect()
        self.state = 1
        self.no = 0
        self.x = 0
    def update(self, pressed):
        self.no = self.no + 1
        if self.no <= 2:
            self.state = 1
        elif self.no <= 4:
            self.state = 2
        elif self.no <= 6:
            self.state = 3
        else:
            self.no = 0
        if pygame.K_w in pressed:
            print("w is pressed")
        if pygame.K_s in pressed:
            print("s is pressed")
        if pygame.K_a in pressed:
            print("a is pressed")
        if pygame.K_d in pressed:
            print("d is pressed")
        self.x = self.rect.x
        self.image = pygame.image.load(str(self.state) + ".png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x + 1


pygame.init()

screen = pygame.display.set_mode(size)
bg = pygame.image.load("placeholder.png").convert()
player = Shuttle()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print "Click!"

    screen.blit(bg, (0, 0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()

pygame.quit()
