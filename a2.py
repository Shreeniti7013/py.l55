import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("game" )
bg=pygame.transform.scale(pygame.image.load("jpeg image.jpg"),(500,500))
text=pygame.font.Font(None,36).render(' Welcome to my app',True,pygame.Color(' white' ) )
text_rect=text.get_rect(center=(500//2,500//2))

done= False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
         pygame.quit()
            
    
    screen.blit(bg,(0,0))
    screen.blit(text,text_rect)
    pygame.display.flip()
