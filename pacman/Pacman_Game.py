import pygame
import GridMaker
import PSpriteMaker
pygame.init()

def checkmovep():
    global moving,movingM
    if ([xp+vxp,yp+vyp] not in grid):
        moving=5
    if kinp==0 and ([xp,yp-v] in grid):
        moving=0
        movingM=0
    if kinp==1 and ([xp+v,yp] in grid):
        moving=1
        movingM=1
    if kinp==2 and ([xp,yp+v] in grid):
        moving=2
        movingM=2
    if kinp==3 and ([xp-v,yp] in grid):
        moving=3
        movingM=3
    
        
def movep():
    global xp,yp,vxp,vyp
    if moving==0:
        vxp=0
        vyp=-v
    if moving==1:
        vxp=+v
        vyp=0
    if moving==2:
        vxp=0
        vyp=+v
    if moving==3:
        vxp=-v
        vyp=0
    if moving==5:
        vxp=0
        vyp=0
    yp+=vyp
    xp+=vxp
    if xp==474:
        xp=-2
    elif xp==-2:
        xp=474

disp=pygame.display.set_mode((500,600))
bg=pygame.image.load('sprites/map.png')
bg=pygame.transform.scale(bg,(500,600))

#pacman1=pygame.transform.scale(pacman1,(26,26))

psprites=PSpriteMaker.psm()
pdeaths=PSpriteMaker.pdsm()

grid=GridMaker.make()
#start point = [236,414]
xp=236
yp=414
vxp=0
vyp=0
v=2
kinp=5
moving=5
movingM=5
done=0
pscounter=0
gameC=0
danimeC=0
while not done:
    disp.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                kinp=0
            if event.key==pygame.K_RIGHT:
                kinp=1
            if event.key==pygame.K_DOWN:
                kinp=2
            if event.key==pygame.K_LEFT:
                kinp=3

            if event.key==pygame.K_ESCAPE:
                done=1
    checkmovep()
    movep()
    if moving!=5:
        disp.blit(psprites[moving][pscounter],(xp,yp))
    elif movingM!=5:
        disp.blit(psprites[movingM][1],(xp,yp))
    else:
        disp.blit(psprites[0][0],(xp,yp))
    if gameC%3==0:
        pscounter+=1
        if pscounter==4:
            pscounter=0
    #print("xp=",xp," yp=",yp)
    pygame.draw.rect(disp,(0,0,0),pygame.Rect(0,270,26,28))
    pygame.draw.rect(disp,(0,0,0),pygame.Rect(474,270,26,28))
    pygame.display.update()
    gameC+=1
    pygame.time.Clock().tick(70)

done=0
waitC=0
while not done:
    disp.blit(bg,(0,0))

    if movingM==5:
        disp.blit(psprites[0][1],(xp,yp))
    else:
        disp.blit(psprites[movingM][1],(xp,yp))
    #print("xp=",xp," yp=",yp)
    if waitC>2:
        waitC+=1
    else:
        done=1
    pygame.draw.rect(disp,(0,0,0),pygame.Rect(0,270,26,28))
    pygame.draw.rect(disp,(0,0,0),pygame.Rect(474,270,26,28))
    pygame.display.update()
    pygame.time.Clock().tick(1)

done=0
while not done:
    disp.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_ESCAPE:
                done=1
    if danimeC<=10:
        disp.blit(pdeaths[danimeC],(xp,yp))
    #print("xp=",xp," yp=",yp)
    pygame.draw.rect(disp,(0,0,0),pygame.Rect(0,270,26,28))
    pygame.draw.rect(disp,(0,0,0),pygame.Rect(474,270,26,28))
    pygame.display.update()
    danimeC+=1
    pygame.time.Clock().tick(15)

pygame.quit()
