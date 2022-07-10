import pygame 


pygame.init() 
scr = pygame.display.set_mode((500,500)) 
color = (0,255,0) 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    pygame.draw.line(scr, color, (40, 300), (140, 300), 6)
    
    pygame.display.flip()
    
    
    
pygame.quit()