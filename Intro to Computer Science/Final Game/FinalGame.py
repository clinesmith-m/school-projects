import pygame
from pygame.locals import *
from random import randint

pygame.init()

sw = 800
sh = 600
screensize = [sw, sh]
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Nicolas Cage!")

clock = pygame.time.Clock()

white  = (255, 255, 255)
black  = (  0,   0,   0)
red    = (255,   0,   0)
green  = (  0, 255,   0)
blue   = (  0,   0, 255)
purple = (180,   0, 180)
yellow = (255, 255,   0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("baseCage.jpg")
        self.rect = self.image.get_rect()
        
class AltarEgos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(choose_cage())
        self.rect = self.image.get_rect()
        self.starsign = randint(0,1)

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("BossCage2.jpg")
        self.rect = self.image.get_rect()
        self.starsign = randint(0,1)

class Bullets(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        
class Oscar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("trophy.jpg")
        self.rect = self.image.get_rect()

def choose_cage():
    roll = randint(0, 3)
    if roll == 0:
        return "BadCage1.jpg"
    elif roll == 1:
        return "BadCage2.jpg"
    elif roll == 2:
        return "BadCage3.jpg"
    elif roll == 3:
        return "BadCage4.jpg"
    
def check_keys():
    global Player
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and goodNic.rect.x + 48 < sw:
        goodNic.rect.x += 9
    if keys[K_LEFT] and goodNic.rect.x > 5:
        goodNic.rect.x -= 9
    if keys[K_UP] and goodNic.rect.y > 5:
        goodNic.rect.y -= 9
    if keys[K_DOWN] and goodNic.rect.y + goodNic.rect.height < sh:
        goodNic.rect.y += 9

def spawn(round):
    global badNics, bossNics, trophies
    if round == 0 or round == 2 or round == 4:
        for i in range(0, round + 1):
            badNics = AltarEgos()
            badNics.rect.x = randint(0,sw-100)
            badNics.rect.y = 0
            badNic.add(badNics)
            enemies.add(badNics)
            allsprites.add(badNics)
    elif round == 1 or round == 3:
        for i in range(0, round):
            bossNics = Boss()
            bossNics.rect.x = 400
            bossNics.rect.y = 0
            bossNic.add(bossNics)
            enemies.add(bossNics)
            allsprites.add(bossNics)
    elif round == 5:
        trophies = Oscar()
        trophies.rect.x = 400
        trophies.rect.y = 50
        trophy.add(trophies)
        allsprites.add(trophies)
    
def move_enemies():
    for guy in enemies:
        if guy.starsign == 0 and guy.rect.x <= 700:
            guy.rect.x += 5
        elif guy.starsign == 0 and guy.rect.x > 700:
            guy.starsign = 1
        if guy.starsign == 1 and guy.rect.x > 0:
            guy.rect.x -= 5
        elif guy.starsign == 1 and guy.rect.x <= 0:
            guy.starsign = 0
            guy.rect.x += 5
    
def reset():
    global goodNic
    goodNic.rect.x = 400
    goodNic.rect.y = 500

def die_roll():
    number = randint(0,30)
    if number < 3:
        shoot_bullet()

def die_roll_boss():
    number = randint(0,30)
    if number < 3:
        boss_shoot()

def shoot_bullet():
    generic_enemies = pygame.sprite.Group.sprites(badNic)
    for guy in generic_enemies:
        bullet = Bullets()
        bullet.rect.x = guy.rect.x + 30
        bullet.rect.y = guy.rect.y + 50
        bullets.add(bullet)
        allsprites.add(bullet)

def boss_shoot():
    boss = pygame.sprite.Group.sprites(bossNic)
    # Fires three bullets
    for guy in boss:
        # Far left bullet
        bullet1 = Bullets()
        bullet1.rect.x = guy.rect.x
        bullet1.rect.y = guy.rect.y + 95
        bullets.add(bullet1)
        allsprites.add(bullet1)
        # Middle bullet
        bullet2 = Bullets()
        bullet2.rect.x = guy.rect.x + 48
        bullet2.rect.y = guy.rect.y + 95
        bullets.add(bullet2)
        allsprites.add(bullet2)
        # Far right bullet
        bullet3 = Bullets()
        bullet3.rect.x = guy.rect.x + 97
        bullet3.rect.y = guy.rect.y + 95
        bullets.add(bullet3)
        allsprites.add(bullet3)

def remove_bullets():
    for bullet in bullets:
        allsprites.remove(bullet)
    pygame.sprite.Group.empty(bullets)

goodNic = Player()
goodNic.rect.x = 400
goodNic.rect.y = 500

allsprites = pygame.sprite.Group()
allsprites.add(goodNic)

badNic = pygame.sprite.Group()

bossNic = pygame.sprite.Group()

enemies = pygame.sprite.Group()

trophy = pygame.sprite.Group()

bullets = pygame.sprite.Group()

done = False
score = 0
round = 0
spawn(round)
round += 1
win = False
lose = False

pygame.mixer.music.load("musicCage.wav")
pygame.mixer.music.play(loops = 0, start = 0.0)

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    check_keys()
    
    # Check for victory/defeat.
    if win == True:
        screen.fill(white)
        font = pygame.font.Font(None, 72)
        text = font.render("YOU WIN!!!", True, black)
        screen.blit(text, [300, 200])
        pygame.display.flip()
    elif lose == True:
        screen.fill(white)
        font = pygame.font.Font(None, 72)
        text = font.render("YOU LOSE.", True, black)
        screen.blit(text, [300, 200])
        pygame.display.flip()
    else:

        # 2. Program logic, change variables, etc.
        collideList = pygame.sprite.spritecollide(goodNic, badNic, True)
        for badguy in collideList:
            allsprites.remove(badguy)
            badNic.remove(badguy)
            score += 1
        
        collideList1 = pygame.sprite.spritecollide(goodNic, bossNic, True)
        for badguy in collideList1:
            allsprites.remove(badguy)
            bossNic.remove(badguy)
            score += 5
        
        # Checks to see if you get shot.
        collideList2 = pygame.sprite.spritecollide(goodNic, bullets, True)
        if collideList2 != []:
            lose = True        
        collideList3 = pygame.sprite.spritecollide(goodNic, trophy, True)
        if collideList3 != []:
            win = True
        
        # Determining enemy spawns.
        try:
            enemy_alive = pygame.sprite.Sprite.alive(badNics)
        except:
            enemy_alive = False
        try:
            boss_alive = pygame.sprite.Sprite.alive(bossNics)
        except:
            boss_alive = False
        try:
            trophy_alive = pygame.sprite.Sprite.alive(trophies)
        except:
            trophy_alive = False
        if  enemy_alive == False and boss_alive == False and trophy_alive == False:
                remove_bullets()
                reset()
                spawn(round)
                round += 1
        
        move_enemies()
        
        # die_roll also calls the shoot_bullet function
        die_roll()
        
        if boss_alive == True:
            die_roll_boss()
        
        for item in bullets:
            item.rect.y += 4
                
            # 3. Draw stuff
        screen.fill(white)
        #bgSurface = pygame.image.load("backgroundCage.jpg")

        allsprites.draw(screen)

        # Draws "Score: " in the default font at 72 point size.
        font = pygame.font.Font(None, 72)
        text = font.render("Score: %d" % score, True, black)
        screen.blit(text, [300, 200])
        
        pygame.display.flip()
        clock.tick(20)

##while True:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            break
##        elif win == True:
##            font = pygame.font.Font(None, 72)
##            text = font.render("YOU WIN!!!", True, black)
##            screen.blit(text, [300, 200])
##        elif win == False:
##            font = pygame.font.Font(None, 72)
##            text = font.render("YOU LOSE.", True, black)
##            screen.blit(text, [300, 200])            

pygame.quit()