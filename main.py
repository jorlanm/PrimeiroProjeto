import pygame


display = pygame.display.set_mode((1280,720))

player1 = pygame.Rect(0,0,30,150) #formato na tela, pygame.rect é 'retangulo'
player2 = pygame.Rect(1250,0,30,150)
ball = pygame.Rect(600, 350, 15, 15)
loop = True
while loop:

    #lista de eventos com for

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False # fecha a janela do gayme 

        if event.type == pygame.KEYDOWN:#keydown verificando se esta preciona uma tecla
            if event.key == pygame.k_a: #K_a tecla 'a' 
                loop = False # precionar tecla 'a' e fecha a janela 

    display.fill((0,0,0))
    pygame.draw.rect(display, "white", player1)# pygame.draw 'desenha na tela'.rect 'retangulo'
    pygame.draw.rect(display, "white", player2)
    pygame.draw.circle(display, "white", ball.center, 8)
    pygame.display.flip()