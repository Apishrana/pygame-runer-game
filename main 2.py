# imports
import pygame
import random

# functions
def player_ani():
    global player_surf , pi
    if pr.bottom < 275 :
        player_surf = player3
    else:
        pi +=0.1
        if pi >= len(player_list):
            pi =0
        player_surf = player_list[int(pi)]
def en_ani():
    global  en_surf, eni
    eni += 0.07
    if eni >= len(en_list):
        eni = 0
    en_surf = en_list[int(eni)]

# fixed information
pygame.mixer.init()
pygame.init()
piche = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runer game")
ics = pygame.image.load('items/icon/icon.png').convert_alpha()
pygame.display.set_icon(ics)
ghadi = pygame.time.Clock()
pygame.display.update()
# importent
ad=True
by = True
aa = True
ac = True
l = True
l2 = False
font_1 = pygame.font.Font('items/text/Pixeltype.ttf',55)
font_2 = pygame.font.Font(None,200)
font_3 = pygame.font.Font(None,70)
with open('items/others/hiscore','r')as u:
    hiscore = u.read()
l_l = [l2,l]
li = 0
ls = l_l[li]
# random wala var

col = random.randint(0,255)
col2 = random.randint(0,255)
col3 = random.randint(0,255)
uuu = random.randint(900,1100)
l = random.randint(4,6)

# var
tm = 0

# font var
st4 = font_3.render('Press spacebar or click to retry', False , (0,0,0))
st4r = st4.get_rect(midbottom = (400,380))
st2 = font_2.render('Game over', False , (0,0,0))
st2r = st2.get_rect(center = (400,200))

# background
s1 = pygame.image.load('items/bground/sky.png').convert()
s2 = pygame.image.load('items/bground/ground.png').convert()
retry = pygame.image.load('items/icon/relode.png').convert_alpha()
rs = retry.get_rect(midtop = (400,240))

# player
aaa = 4.5
player = pygame.image.load('items/player/player_walk_1.png').convert_alpha()
player2 = pygame.image.load('items/player/player_walk_2.png').convert_alpha()
player_list = [player,player2]
pi = 0
player3 = pygame.image.load('items/player/jump.png').convert_alpha()
player_surf = player_list [pi]
pr = player.get_rect(midbottom = (200,275))
pg = 0

# enemy
en1 = pygame.image.load('items/snale/snail1.png').convert_alpha()
en2 = pygame.image.load('items/snale/snail2.png').convert_alpha()
en_list = [en1,en2]
eni = 0
en_surf = en_list[eni]
sr = en1.get_rect(bottomleft = (550,275))

# pause
pause = pygame.image.load('items/icon/pause.png').convert_alpha()
ps = pause.get_rect(topright = (800,0))
p1 = pygame.image.load('items/bground/p.png').convert()
p1r = p1.get_rect(center = (400,200))

# timers
# ll = pygame.USEREVENT + 1
# pygame.time.set_timer(ll, random.randint(1200, 1500))
ll2 = pygame.USEREVENT + 1
pygame.time.set_timer(ll2, 1000)

# loop
while by :
    # handeling event
    for event in pygame.event.get():

        # exit
        if event.type == pygame.QUIT:
            by  = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pr.collidepoint(event.pos) and pr.bottom >=275 :
                pg = -25
        if ac:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and pr.bottom >=275 :
                    pg = -25
            # if event.type == ll:
            #     piche.blit(en1,sr2)
            if event.type == ll2:
                tm += 1
    if aa:
        sr.x -= aaa
        if sr.x <= -36:
            sr.x = 800
    if ad :
        st1 = font_1.render('Score: ' + f'{tm}', False, (0, 0, 0))
        st1r = st1.get_rect(topleft =  (5, 5))
        st3 = font_1.render('High Score: '+ f'{hiscore}',False , (0,0,0))
        st3r = st3.get_rect(topright = (795,5))
        piche.blit(s1,(0,0))
        piche.blit(s2,(0,275))
        piche.blit(st3 , st3r)
        piche.blit(st1, st1r)
        en_ani()
        piche.blit(en_surf , sr)
        player_ani()
        piche.blit(player_surf, pr)
        pg +=1
        pr.y += pg
        if pr.bottom > 275:
            pr.bottom = 275
        if pr.top < 50:
            pr.top = 50
        if tm >= int(hiscore):
            hiscore = tm
        if pr.colliderect(sr) == 1:
            pygame.mixer.music.load('items/sound/end.mp3')
            pygame.mixer.music.play()
            ad = False
            ac = False
    else:
        st5 = font_3.render('Score achived: ' + f'{tm}', False, (0, 0, 0))
        st5r = st5.get_rect(center=(400,50))
        piche.fill((col, col2, col3))
        piche.blit(st2, st2r)
        piche.blit(retry,rs)
        piche.blit(st4, st4r)
        piche.blit(st5,st5r)
        aa = False
        with open('items/others/hiscore', 'w') as p:
            p.write(str(hiscore))
        sr.x = 550
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rs.collidepoint(event.pos):
                    ad = True
                    aa = True
                    ac = True
                    tm = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ad = True
                    aa = True
                    ac = True
                    tm = 0
    pygame.display.update()
    ghadi.tick(60)
pygame.quit()
quit()