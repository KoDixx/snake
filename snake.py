import pygame()

window = display.set_mode((700,500))
display.set_caption('snake')
window.fill((255,0,0))


game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish != True:
            window.blit(window.fill, (0,0))
            

