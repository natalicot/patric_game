import pygame
import sys, random
import caracters
import time




#init

pygame.init()
width, height = 800,800
x,y=50,600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


patrik = pygame.image.load(r"patrik.png")
player = caracters.good_guy(x,y,patrik)
soap = pygame.image.load(r"soap.png")
wood = pygame.image.load(r"wood.png")
water = pygame.image.load(r"water.png")
enemies_list=pygame.sprite.Group()
enemy_crietion_counting=0

steps_list=[]
steps_crietion_counting=65
corentStep=caracters.steps(width+1,random.randint(450,550),wood)

bullets = []
shootFleg = 0

bg = pygame.image.load(r"bg.png")
bg =pygame.transform.scale(bg,(width,height))
bgX=0
bgX2=bg.get_width()

youlose=pygame.image.load(r"youlose.png")
youlose =pygame.transform.scale(youlose,(width,height))

youwin=pygame.image.load(r"youwin.png")
youwin =pygame.transform.scale(youwin,(width,height))


isJump = False
jumpCount = 10
isCol=False

score=0
font = pygame.font.SysFont("comicsans", 30, True)

#heart bar
heart_img = pygame.image.load(r"heart.png")
life_bar1 = caracters.heart(width-50,10,heart_img)
life_bar2 = caracters.heart(width-100,10,heart_img)
life_bar3 = caracters.heart(width-150,10,heart_img)
life_bars = [life_bar1,life_bar2,life_bar3]

loseorwin=0


def gravity(player,steps_list):
    
        player.rect.y += 20 # how fast player falls
        if player.rect.y == y:
            return
        for step in steps_list:
            if player.checkCollision(step):
                
                player.rect.y=step.rect.y-player.height+10
                print("col in grav")
                return
        return
            
    
        

    
    



#game loop

run = True
while run:


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                buletFlag=1


    
    #fill screen
    screen.fill((255,255,255))
    screen.blit(bg,(bgX,0))
    screen.blit(bg,(bgX2,0))

    


    #creating enemies
    enemy_crietion_counting +=1
    if enemy_crietion_counting==70:
            enemy_crietion_counting=0
            new_enemy = caracters.enemy_class(width+5,random.randint(400,500),soap)
            enemies_list.add(new_enemy)
    for enemy in enemies_list:
        if player.rect.x>200 :
            enemy.rect.x -= 5
            enemy.draw(screen)
        if player.checkCollision(enemy):
            enemies_list.remove(enemy)
            
            if len(life_bars)==1:
                run=False
                loseorwin=1
            life_bars.pop()
            

        else:
            enemy.rect.x -= 5
            enemy.draw(screen)
            if enemy.rect.x < -200: 
                enemies_list.remove(enemy)


    
    
    #handling events

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and player.rect.x<(width-player.width):
        if player.rect.x>200 :
            bgX -=5
            bgX2 -=5
            if bgX <= bg.get_width() * -1:  # If our bg is at the -width then reset its position
                bgX = bg.get_width() - 5
            if bgX2 <= bg.get_width() * -1:
                bgX2 = bg.get_width()-5
            


            #creating steps
            steps_crietion_counting +=1
            if steps_crietion_counting==70:
                steps_crietion_counting=0
                new_step = caracters.steps(width+1,random.randint(450,550),wood)
                steps_list.append(new_step)
            
            for step in steps_list:
                step.rect.x -= 5
                step.draw(screen)
                if step.rect.x < -200: 
                    steps_list.remove(step)
        else:
            player.rect.x+=5
    if keys[pygame.K_LEFT]and player.rect.x>0:
        player.rect.x -= 5
    

    shootFleg +=1
    #shooting

    if keys[pygame.K_SPACE] != keys[pygame.KEYDOWN] and shootFleg>10:
        new_bullet = caracters.bullet(round(player.rect.x + player.width//2),round(player.rect.y + player.height//2),water)
        bullets.append(new_bullet)
        shootFleg =0 
    



    #jumping

    if not(isJump):
        if keys[pygame.K_UP]:
            isJump=True
                    
    else:
        if jumpCount >= -10 and not isCol:
            neg=1
            if jumpCount < 0:
                neg=-1
            player.rect.y -= (int)((jumpCount ** 2) * 0.5 * neg)
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
            isCol=False




        for step in steps_list:
            if step.checkCollision(player):    
                player.rect.y=step.rect.y-player.height+5
                corentStep=step
                print("step col")
                

   
    if player.rect.y<=y and not keys[pygame.K_UP]:
        if player.rect.x>corentStep.rect.x+corentStep.width or player.rect.x+player.width>corentStep.rect.x:
            gravity(player,steps_list)
    

    #redraw screen
    
    
    for step in steps_list:
        step.draw(screen)
    
    for bullet in bullets:
        bullet.rect.x += bullet.speed
        bullet.draw(screen)
        if bullet.rect.x > width+10:
            bullets.remove(bullet)
        for enemy in enemies_list:
            if bullet.checkCollision(enemy):
                score+=100
                enemies_list.remove(enemy)
                bullets.remove(bullet)
                if score==500:
                    loseorwin=2
                    run=False

    text = font.render('Score: ' + str(score), 1, (0,0,0))
    screen.blit(text, (10, 10))

    for life in life_bars:
        life.draw(screen)

    player.draw(screen)
    pygame.display.update()
    clock.tick(27)



screen.fill((255,255,255))
if loseorwin==1:
    screen.blit(youlose,(0,0))
elif loseorwin==2:
    screen.blit(youwin,(0,0))
pygame.display.flip()
time.sleep(3)

pygame.quit()
