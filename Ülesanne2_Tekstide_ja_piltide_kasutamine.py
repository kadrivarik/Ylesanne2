import pygame  # impordin pygame mooduli
pygame.init()  # käivitan mooduli
#ekraani seaded
screen=pygame.display.set_mode([640,480])  # ekraani suurus
pygame.display.set_caption("ülesanne 2") # ekraani pealkiri
screen.fill([204, 255, 204])

bg = pygame.image.load("bg_shop.png") # taustapilt pood
screen.blit(bg,[0,0])  # üle kogu ekraani

seller = pygame.image.load("seller.png")  # müüja pilt
seller = pygame.transform.scale(seller,[255, 310]) # müüja suurus
screen.blit(seller,[107,158]) # müüja asukoht

chat = pygame.image.load("chat.png") # jutupilve pilt
chat = pygame.transform.scale(chat,[256, 197]) # jutupilve suurus
screen.blit(chat,[246,65])  # jutupilve asukoht


font = pygame.font.Font(None, 25)  # kirja suurus
text = font.render("Tere, olen Kadri Varik!", True, [255,255,255]) # Kiri ja värv
screen.blit(text, [285,150]) # kirja asukoht

pygame.display.flip()  # kuvab ekraanil/uuendab ekraani

# Hoiab ekraani avatuna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False   #