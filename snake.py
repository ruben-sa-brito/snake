import pygame
from pygame.locals import *
from sys import exit 
from random import randint


pygame.init()

largura = 640
altura = 480
x = 300
y = 215
x_m = 0
y_m = 0
move = False
body = 2
snake = [(300, 215), (300,205), (300, 195)]
x_blue = randint(40,600)
y_blue = randint(50,430)
fonte = pygame.font.SysFont('lucidasans', 40, True, True)
pontos = 0
exit = False

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
mensagem = f'Pontos: {pontos}'


while True:
    
   
    relogio.tick(20)
    
    tela.fill((0,0,0))
    
    
    
    
    if exit:
        texto_formatado = fonte.render(mensagem, True, (255,255,255))
        tela.blit(texto_formatado, (200, 140))
        texto_formatado = fonte.render(f'Sua Pontuação: {pontos}', True, (255,255,255))
        tela.blit(texto_formatado, (170, 180))
        
        pygame.display.update()
    else:
        mensagem = f'Pontos: {pontos}'
    
        texto_formatado = fonte.render(mensagem, True, (255,255,255))    
        
        
      
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x_m = -5
                y_m = 0
                move = True
            if event.key == K_d:
                x_m = 5
                y_m = 0
                move = True        
            if event.key == K_w:
                x_m = 0
                y_m = -5
                move = True 
            if event.key == K_s:
                x_m = 0
                y_m = 5 
                move = True
                    
    if not exit:    
        if move:
            for i in range(len(snake)-1,0,-1):
                
                snake[i]=snake[i-1]
                
                
        snake[0] = (snake[0][0] + x_m, snake[0][1] + y_m)
        if snake[0][0] > 640:
            snake[0] = (0, snake[0][1])
        
        if snake[0][0] < 0:
            snake[0] = (640, snake[0][1])
        
        if snake[0][1] > 480:
            snake[0] = (snake[0][0], 0)
        
        if snake[0][1] < 0:
            snake[0] = (snake[0][0], 480)           
        
        
            
        for x in range(len(snake)):
            if x == 0:    
                ret_red = pygame.draw.rect(tela, (255,0,0), (snake[x][0], snake[x][1] ,10,10))
            else:
                pygame.draw.rect(tela, (255,0,0), (snake[x][0], snake[x][1] ,10,10))    
        ret_blue = pygame.draw.rect(tela, (0,0,255), (x_blue,y_blue,10,10))
        
        
        
        if ret_red.colliderect(ret_blue):
            x_blue = randint(40,600)
            y_blue = randint(50,430)
            snake.append((snake[-1][0]-x_m,snake[-1][1]-y_m ))
            
            pontos += 1
            
        for point in snake[3:]:
            
            if ret_red.collidepoint(point[0]+6, point[1]+6):
                exit = True
            
            
            
        tela.blit(texto_formatado, (420, 10))
        pygame.display.update()
    else:
        mensagem = f'GAME OVER'
        
        
           
    
  