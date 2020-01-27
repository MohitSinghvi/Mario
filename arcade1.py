import pygame

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

pygame.init()

screen_height=500
screen_width=800

window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Arcade")

fps=30
clock=pygame.time.Clock()

font=pygame.font.Font(None,25)

def msgToScrn(msg,color,mx,my):
    screen_text=font.render(msg,True,color)
    window.blit(screen_text,[mx,my])

mario_height=50
mario_width=50



mariomover = pygame.image.load('Mario_Switch.png')
mariomover1 = pygame.image.load('Mario_Switch1.png')

mariostandr = pygame.image.load('smario.png')
mariomovel = pygame.image.load('Mario_SwitchLeft.png')
mariostandl= pygame.image.load('smarioLeft.png')

mariomover = pygame.transform.scale(mariomover, (mario_width,mario_height))
mariomover1 = pygame.transform.scale(mariomover1, (mario_width,mario_height))

mariomovel = pygame.transform.scale(mariomovel, (mario_width,mario_height))

mariostandr = pygame.transform.scale(mariostandr, (mario_width,mario_height))
mariostandl = pygame.transform.scale(mariostandl, (mario_width,mario_height))



def gameLoop():

    gameExit=False
    mario_x=0
    mario_y=screen_height-mario_height
    movex=0
    movey=0
    direction='left'
    bullet_direction=[]
    jump=False
    stand=True
    fire=False
    in_air1=False
    in_air2=False
    ldown=False
    rdown=False
    k=0

    jump1=False
    block_x=[0,100,0,100,0]
    block_y=[490,400,300,200,100]
    block_width=[screen_width-block_x[0],screen_width-block_x[1],screen_width-block_x[1],screen_width-block_x[1],screen_width-block_x[1]]
    block_height =10
    bullet_x=[]
    bullet_y=[]
    c=0
    floor=500
    obstaclex=[screen_width-mario_width]
    obstacley=[screen_height-mario_height]

    while gameExit==False:


        for i in range(0,len(block_x)):
            if(mario_x+mario_width in range(block_x[i],block_x[i]+block_width[i]+mario_width)):
                if(mario_y+mario_height==block_y[i]):
                    k=i
                    break
                l=i



        if jump==True and c<=10 and stand==True :
            # if(mario_y in range(block_y[k+1],block_y[k+1]+block_height) and mario_x+mario_width in range(block_x[k+1],block_x[k+1]+block_width[k+1]+mario_width)):
            #     mario_y=mario_y+10
            #     c=10
            #     in_air1 = True
            # else:
                mario_y=mario_y-10
                c=c+1
                in_air1=True


        if(c>=10):
            jump=False
            stand=False

        if jump==False and mario_y+mario_height<screen_height :
            if mario_x+mario_width in range(block_x[k],block_x[k]+block_width[k]+mario_width):
                if mario_y+mario_height==block_y[k]:
                    mario_y=mario_y
                    stand=True
                    in_air1=False
                    in_air2=False
                else:
                    mario_y = mario_y +10

            else:
                mario_y = mario_y + 10

        if(mario_y+mario_height==screen_height):
            stand=True
            in_air1 = False
            in_air2=False


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    movex=10
                    direction = 'right'
                    rdown=True
                    ldown=False
                if event.key==pygame.K_LEFT:
                    movex=-10
                    direction = 'left'
                    ldown=True
                    rdown=False
                if event.key==pygame.K_UP:
                    if(stand==True and in_air2==False ):
                        if in_air1==True:
                            in_air2=True
                        jump=True
                        movey=10
                        c=0
                if event.key==pygame.K_SPACE:
                    fire=True
                    bullet_x.append(int(mario_x+2*mario_width/2))
                    bullet_y.append(int(mario_y+mario_height/2))
                    bullet_direction.append(direction)


            if event.type==pygame.KEYUP:
                if event.key == pygame.K_RIGHT and ldown==False:
                    movex=0
                    direction='right'
                    rdown=False

                if event.key == pygame.K_LEFT and rdown==False:
                    ldown=True
                    movex=0
                    direction='left'







        window.fill(blue)

        for j in range(0,len(bullet_x)):
            if fire==True and bullet_x[j]<screen_width:
                pygame.draw.circle(window,red,(bullet_x[j],bullet_y[j]),2)
                if bullet_direction[j] == 'right':
                    bullet_x[j]=bullet_x[j]+15
                else:
                    bullet_x[j] = bullet_x[j] - 15




        if movex!=0:
            if(direction=='right'):
                if(mario_x<screen_width-50):
                    mario_x=mario_x+10

                window.blit(mariomover, (mario_x, mario_y))

            else:
                if (mario_x >0):
                    mario_x=mario_x-10
                window.blit(mariomovel, (mario_x, mario_y))

        else:
            if (direction == 'right'):
                window.blit(mariostandr, (mario_x, mario_y))


            else:
                window.blit(mariostandl, (mario_x, mario_y))

        for i in range(0,len(block_x)):
            pygame.draw.rect(window,green,[block_x[i],block_y[i],block_width[i],block_height])

        #pygame.draw.rect(window,black,[block_x,block_y,block_width,block_height])
        pygame.draw.rect(window, green, [obstaclex[0], obstacley[0],mario_width,mario_height])
        pygame.display.update()

        clock.tick(fps)
    pygame.quit()
    quit()

gameLoop()