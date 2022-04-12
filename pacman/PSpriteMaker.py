import pygame

def psm():
    pO=pygame.image.load('sprites/p_s/pO.png')
    p01=pygame.image.load('sprites/p_s/p01.png')
    p02=pygame.image.load('sprites/p_s/p02.png')
    p11=pygame.image.load('sprites/p_s/p11.png')
    p12=pygame.image.load('sprites/p_s/p12.png')
    p21=pygame.image.load('sprites/p_s/p21.png')
    p22=pygame.image.load('sprites/p_s/p22.png')
    p31=pygame.image.load('sprites/p_s/p31.png')
    p32=pygame.image.load('sprites/p_s/p32.png')
    psprites=[[pO,p01,p02,p01],[pO,p11,p12,p11],[pO,p21,p22,p21],[pO,p31,p32,p31]]

    return psprites

def pdsm():
    pd0=pygame.image.load('sprites/p_s/death/pd0.png')
    pd1=pygame.image.load('sprites/p_s/death/pd1.png')
    pd2=pygame.image.load('sprites/p_s/death/pd2.png')
    pd3=pygame.image.load('sprites/p_s/death/pd3.png')
    pd4=pygame.image.load('sprites/p_s/death/pd4.png')
    pd5=pygame.image.load('sprites/p_s/death/pd5.png')
    pd6=pygame.image.load('sprites/p_s/death/pd6.png')
    pd7=pygame.image.load('sprites/p_s/death/pd7.png')
    pd8=pygame.image.load('sprites/p_s/death/pd8.png')
    pd9=pygame.image.load('sprites/p_s/death/pd9.png')
    pd10=pygame.image.load('sprites/p_s/death/pd10.png')
    pdeaths=[pd0,pd1,pd2,pd3,pd4,pd5,pd6,pd7,pd8,pd9,pd10]

    return pdeaths
