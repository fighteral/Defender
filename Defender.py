_author__ = "Rishav Gupta"
__copyright__ = "Copyright (C) 2016 Rishav Gupta"
__license__ = "Public Domain"
__version__ = "1.0"




import pygame
import random
from os import path
display_width= 1100
display_height = 600
fps = 30
pygame.init()
pygame.mixer.init()
# define colors
control_color=(150,150,200)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue=(0,0,150)
red=(255,0,0)
orange=(250,255,0)
menu_color=(165,42,42)
POWER_TIME=5000
#file for highscore

#assets

#img_dir=path.join(path.dirname(__file__),'img')
#sound_dir=path.join(path.dirname(__file__),'sound')

font_name=pygame.font.match_font('times new roman')
font_name_menu=pygame.font.match_font('calibri')
gameDisplay1 = pygame.display.set_mode((display_width, display_height))

def draw_end(surf,text,size,x,y):
    background_menu =pygame.image.load("back1.png")
    gameDisplay.blit(background_menu,(0,0))
    font=pygame.font.Font(font_name_menu,size)
    text_surface = font.render(text,True,red)
    text_rect= text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

def pause():

    gameDisplay1 = pygame.display.set_mode((display_width, display_height))
    background_menu =pygame.image.load("back1.png")
    gameDisplay1.blit(background_menu,(0,0))
    draw(gameDisplay1,"Pause ",40,display_width/2,display_height/7)
    draw_menu(gameDisplay1," Continue:C",30,100,500)
    draw_menu(gameDisplay1," Quit:Q",30,1000,500)
    pygame.display.flip()

    paused= False
    while  not paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=True

def about():
    gameDisplay1 = pygame.display.set_mode((display_width, display_height))
    gameDisplay1.fill(black)
    draw(gameDisplay1,"About ",40,display_width/2,display_height/7)
    draw_controls(gameDisplay1, 'Defender is all about playing and relaxing your mind from all the tension.',20,display_width/2,display_height/3.7)
    draw_controls(gameDisplay1,'In this game a player has to save himself from various enemies ship and small meteriod.',20,display_width/2,display_height/3)
    draw_controls(gameDisplay1,' A player is given 3 lives at a time,if you hit an enemy you are rewarded with 1 point and 5 points if you hit an meteriod.',20,display_width/2,display_height/2.5)
    draw_controls(gameDisplay1,' Similarly if an meteriod hits you -50 is deduced from your sheild and -25 when an enemy hits you.',20,display_width/2,display_height/2.1)
    draw_controls(gameDisplay1, ' So buckle up yourself for the best game of your life.' ,20,display_width/2,display_height/1.5)
    draw_controls(gameDisplay1,"Main menu:0",30,100,display_height/1.2)
    pygame.display.flip()


def controls_settings():

    gameDisplay1 = pygame.display.set_mode((display_width, display_height))
    gameDisplay1.fill(blue)
    draw(gameDisplay1,"Controls ",40,display_width/2,display_height/7)
    draw_controls(gameDisplay1,"Right - d/right_arrow_key ",30,display_width/2,display_height/3.5)
    draw_controls(gameDisplay1,"Left- a/left_arrow_key",30,display_width/2,display_height/2.6)
    draw_controls(gameDisplay1,"shooting: spacebar/left-mouse",30,display_width/2,display_height/2)
    draw_controls(gameDisplay1,"Escape:esc",30,display_width/2,display_height/1.6)
    draw_controls(gameDisplay1,"Main menu:0",30,display_width/2,display_height/1.2)

    pygame.display.flip()

def draw_controls(surf,text,size,x,y):
    font=pygame.font.Font(font_name_menu,size)
    text_surface = font.render(text,True,control_color)
    text_rect= text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

#def scores():
#    all_sprites = pygame.sprite.Group()
#    bullets=pygame.sprite.Group()
#    meteriod=pygame.sprite.Group()
#    player = Player()
#    enemy=pygame.sprite.Group()#enemy sprite so that there can be repition
#    all_sprites.add(player)
#    hits=pygame.sprite.groupcollide(meteriod,bullets,True,True)
#    for hit in hits:
#        score += 5

#    hit=pygame.sprite.groupcollide(enemy,bullets,True,True)
#    for hits in hit:
#        score += 1

def credits():

    gameDisplay1 = pygame.display.set_mode((display_width, display_height))
    draw(gameDisplay1,"Credits ",40,display_width/2,display_height/7)
    draw_controls(gameDisplay1,"Mentor: Rohit Bhullar",30,display_width/2,display_height/3.5)
    draw_controls(gameDisplay1,"Rishav Gupta-14BCS1376",30,display_width/2,display_height/2.6)

    draw_controls(gameDisplay1,"Main menu:0",30,display_width/2,display_height/1.2)
    pygame.display.flip()
    #gameDisplay1.fill(black)

def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name_menu,size)
    text_surface = font.render(text,True,control_color)
    text_rect= text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

def draw_menu(surf,text,size,x,y):
    font=pygame.font.Font(font_name_menu,size)
    text_surface = font.render(text,True,menu_color)
    text_rect= text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

def draw(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,orange)
    text_rect= text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)

def newenemy():
    m=Enemy()#where enemy function is stored
    all_sprites.add(m)#adding m into all_sprites
    enemy.add(m)


def newmet():
    m=mit()
    all_sprites.add(m)
    meteriod.add(m)

def draw_shield(surf,x,y,per):
    if per < 0:
        per=0
    lenght=100
    height=10
    fill=(player.shield/100)*100
    outer_rect=pygame.Rect(x,y,lenght,height)
    inner_rect=pygame.Rect(x,y,fill,height)
    pygame.draw.rect(gameDisplay,green,inner_rect)
    pygame.draw.rect(gameDisplay,red,outer_rect,2)


def draw_lives(surf,x,y,img,lives):
    for i in range(lives):
        img_rect=img.get_rect()
        img_rect.x=x+30*i
        img_rect.y=y
        surf.blit(img,img_rect)

def end_screen():
    Highscore=0
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    background_menu =pygame.image.load("back1.png")
    gameDisplay.blit(background_menu,(0,0))
    draw(gameDisplay,"GAME OVER!",70,display_width/2,display_height/4)
    draw(gameDisplay," Main Menu:M",40,160,500)
    draw(gameDisplay," Quit:Q",40,1000,500)
    draw_menu(gameDisplay," Score:"+str(score),26,display_width/2,display_height/2)
    pygame.display.flip()
    waiting=False

    while not waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_m:
                    waiting=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()


def show_screen():

    background_menu =pygame.image.load("back1.png")
    gameDisplay.blit(background_menu,(0,0))
    draw(gameDisplay,"DEFENDER!",70,display_width/2,display_height/4)
    draw_menu(gameDisplay," Play(P)",30,100,500)
    draw_menu(gameDisplay," Quit(Q)",30,1000,500)
    draw_menu(gameDisplay," Credits(C)",26,display_width/2,display_height/1.8)
    draw_menu(gameDisplay," Controls(S)",26,display_width/2,display_height/1.6)
    draw_menu(gameDisplay," About(A)",26,display_width/2,display_height/1.44)



    pygame.display.flip()
    waiting=False


    while not waiting:
        clock.tick(fps)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    credits()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_0:
                    show_screen()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    controls_settings()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    about()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    waiting=True
class Pow(pygame.sprite.Sprite ):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type=random.choice(['shield','gun'])
        self.image=powerup_images[self.type]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center=center
        self.speedy= 5
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > display_height:#to kill a laser when it out of the screen
            self.kill
#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)#built in function
        self.image = player_image
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius=int(19)
        #pygame.draw.circle(self.image,green,self.rect.center,self.radius)
        self.rect.centerx = display_width / 2
        self.rect.bottom=display_height-10
        self.speedx=0
        self.shield=100
        self.lives=3
        self.hidden_player=False #flag having 2 values true or False
        self.hide_timer=pygame.time.get_ticks()
        self.power=1
        self.power_timer=pygame.time.get_ticks()


    def update(self):
        if self.power >= 2 and pygame.time.get_ticks()-self.power_timer > POWER_TIME:
            self.power -=1
            self.power_timer=pygame.time.get_ticks()
        if self.hidden_player and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden_player=False
            self.rect.centerx = display_width / 2
            self.rect.bottom=display_height - 10
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:#control
            self.speedx =-5
        if keystate[pygame.K_RIGHT]:#control
            self.speedx = +5
        if keystate[pygame.K_a]:#control
            self.speedx =-5
        if keystate[pygame.K_d]:#control
            self.speedx = +5
        self.rect.x += self.speedx
        if self.rect.left < 0:#boundary
            self.rect.left = 0
        if self.rect.right > display_width:#boundary
            self.rect.right = display_width

    def powerup(self):
        self.power+=1
        self.power_timer=pygame.time.get_ticks()


    def shoot_enemy(self):
        if self.power==1:
            bullet=Bullet_player(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            laser_sound_player.play()
        if self.power>=2:
                bullet1=Bullet_player(self.rect.left,self.rect.centery)
                bullet2=Bullet_player(self.rect.right,self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                laser_sound_player.play()
    def hide(self): # to hide the defender for some millisecond
        self.hidden_player=True
        self.hide_timer=pygame.time.get_ticks()
        self.rect.center=(display_width/2,display_height+200)
#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius=int(16)
        #pygame.draw.circle(self.image,green,self.rect.center,self.radius)
        self.rect.x=random.randrange(display_width - self.rect.width)#where will enemy occur
        self.rect.y=random.randrange(-100,-40)#position for Enemy
        self.speedy=random.randrange(3,6)#for enemy down movement
        self.speedx=random.randrange(-3,3)#for enemy left right movement

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > display_height or self.rect.left < -20 or self.rect.right>display_width+20:
            self.rect.x=random.randrange(display_width - self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(3,8)


#player laser
class Bullet_player(pygame.sprite.Sprite ):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=player_laser
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy= -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:#to kill a laser when it out of the screen
            self.kill

class mit(pygame.sprite.Sprite ):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=mit_image
        #self.image = pygame.image.load(os.path.join(img_folder,"square2.png")).convert_alpha()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius=int(12.5)
        #pygame.draw.circle(self.image,green,self.rect.center,self.radius)
        self.rect.x=random.randrange(display_width - self.rect.width)#where will enemy occur
        self.rect.y=random.randrange(-100,-40)#position for Enemy
        self.speedy=random.randrange(3,6)#for enemy down movement
        self.speedx=random.randrange(-3,3)#for enemy left right movement

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > display_height or self.rect.left < -20 or self.rect.right>display_width+20:
            self.rect.x=random.randrange(display_width - self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(3,8)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center=center
        self.frame=0 #frames movement
        self.last_update=pygame.time.get_ticks()#when the last tym it was updated
        self.frame_wait=40# how quickly the explosion happens

    def update(self):
        instance = pygame.time.get_ticks()
        if instance - self.last_update > self.frame_wait:
            self.last_update = instance
            self.frame +=1
            if self.frame == len(explosion[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion[self.size][self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center


# graphics
background =pygame.image.load("bg2.jpg")
background_rect=background.get_rect()
player_image = pygame.image.load("xwing.png")
player_mini=pygame.transform.scale(player_image,(30,30))
enemy_image = pygame.image.load("square2.png")
mit_image = pygame.image.load("mit.png")
player_laser=pygame.image.load("lazerblu.png")
background =pygame.image.load("bg2.jpg")

powerup_images={}
powerup_images['shield']=pygame.image.load("shield.png")
powerup_images['gun']=pygame.image.load("power.png")

#sound
pygame.mixer.music.load('done.mp3')
pygame.mixer.music.set_volume(60)

death_sound=pygame.mixer.Sound('Explosion2.wav')
laser_sound_player=pygame.mixer.Sound('Laser_Shoot7.wav')
explosion_sound=[]
for snd in ['Explosion1.wav','Explosion6.wav']:
    explosion_sound.append(pygame.mixer.Sound(snd))

#explosion using dictonary
explosion={}
explosion['large']=[]
explosion['small']=[]
explosion['player']=[]
for i in range(9):
    file_exp='regularExplosion0{}.png'.format(i)
    exp_image=pygame.image.load(file_exp)
    exp_image.set_colorkey(black)
    img_large=pygame.transform.scale(exp_image,(80,80))
    explosion['large'].append(img_large)
    img_small=pygame.transform.scale(exp_image,(38,38))
    explosion['small'].append(img_small)
    file_exp='sonicExplosion0{}.png'.format(i)
    img=pygame.transform.scale(exp_image,(80,80))
    explosion['player'].append(img)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Defender")
clock = pygame.time.Clock()
HighScore=0
pygame.mixer.music.play(loops = -1)


# Game loop
gameOver=False
gameExit = False
while not gameExit:
    if not gameOver:
        gameDisplay.fill(black)
        show_screen()
        gameOver=True

        all_sprites = pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        powerups=pygame.sprite.Group()
        meteriod=pygame.sprite.Group()
        player = Player()
        enemy=pygame.sprite.Group()#enemy sprite so that there can be repition
        all_sprites.add(player)
        for x in range(2):
            newmet()

        for i in range(8):# how many enemy should apear together on the screen
            newenemy()

        score = 0
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot_enemy()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot_enemy()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause()
    #gameDisplay.blit(background,(0,0))
    # Update
    all_sprites.update()
    hits=pygame.sprite.groupcollide(meteriod,bullets,True,True)
    for hit in hits:
        score += 5
        random.choice(explosion_sound).play()
        expl=Explosion(hit.rect.center,'large')
        all_sprites.add(expl)
        if random.random()>.5:
            pow=Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmet()

    hits=pygame.sprite.spritecollide(player,meteriod ,True,pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= 50
        expl=Explosion(hit.rect.center,'small')
        all_sprites.add(expl)
        newmet()
        if player.shield <=0:
            death_sound.play()
            player_expl=Explosion(player.rect.center,'player')
            all_sprites.add(player_expl)
            player.hide()
            player.lives -=1
            player.shield=100

    hits=pygame.sprite.spritecollide(player,powerups,True)

    for hit in hits:
        if hit.type =='shield':
            player.shield +=random.randrange(10,30)
            if player.shield >=100:
                player.shield=100
        if hit.type =="gun":
            player.powerup()
    # when the player has died and there is an explosion_sound
    if player.lives == 0 and not player_expl.alive(): #pygame function to tell where sprite is alive or not

        end_screen()
        gameOver=False

    hit=pygame.sprite.groupcollide(enemy,bullets,True,True)
    for hits in hit:
        score += 1
        random.choice(explosion_sound).play()
        expl=Explosion(hits.rect.center,'large')
        all_sprites.add(expl)
        if random.random()>.7 :
            pow=Pow(hits.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newenemy()

    hit=pygame.sprite.spritecollide(player,enemy,True,pygame.sprite.collide_circle)

                                #sprite u wanna check,
                                #group you wanna check,
                                #and False/true tells whether collided items should be delted or not
    for hits in hit:
        player.shield -= 25
        expl=Explosion(hits.rect.center,'small')
        all_sprites.add(expl)
        newenemy()
        if player.shield <=0:
            death_sound.play()
            player_expl=Explosion(player.rect.center,'player')
            all_sprites.add(player_expl)
            player.hide()
            player.lives -=1
            player.shield=100

    hit=pygame.sprite.spritecollide(player,powerups,True)
    for hits in hit:
        if hits.type =='shield':
            player.shield +=random.randrange(10,30)
            if player.shield >=100:
                player.shield=100
        if hits.type =="gun":
            player.powerup()

    if player.lives == 0 and not player_expl.alive(): #pygame function to tell where sprite is alive or not

            end_screen()
            gameOver=False

    # Draw
    gameDisplay.fill(white)
    gameDisplay.blit(background,background_rect)
    all_sprites.draw(gameDisplay)



    #draw(gameDisplay,str(HighScore),18,display_width/3,10)
    draw(gameDisplay,str(score),18,display_width/2,10)
    draw_shield(gameDisplay,5,5,player.shield)
    draw_lives(gameDisplay,display_width-100,5,player_mini,player.lives)
    pygame.display.flip()


pygame.quit()
