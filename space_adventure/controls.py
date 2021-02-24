import pygame
import sys
import assets

pygame.init()
clock = pygame.time.Clock()

arrow_img = pygame.transform.flip(pygame.image.load("assets/back.png"), True, False)
arrow_rect = arrow_img.get_rect(center=(640, 500))

controls_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 40)
controls_text_1 = controls_font.render("Controls", True, (255, 255, 255))
controls_rect_1 = controls_text_1.get_rect(center=(640, 300))

controls_text_2 = controls_font.render("Move Up --> Up Arrow", True, (255, 255, 255))
controls_rect_2 = controls_text_2.get_rect(center=(640, 350))

controls_text_3 = controls_font.render("Move Down --> Down Arrow", True, (255, 255, 255))
controls_rect_3 = controls_text_3.get_rect(center=(640, 400))

controls_text_4 = controls_font.render("Fire --> Space", True, (255, 255, 255))
controls_rect_4 = controls_text_4.get_rect(center=(640, 450))

def play_controls():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    running = False

        assets.screen.fill((0, 0, 0))
        assets.screen.blit(controls_text_1, controls_rect_1)
        assets.screen.blit(controls_text_2, controls_rect_2)
        assets.screen.blit(controls_text_3, controls_rect_3)
        assets.screen.blit(controls_text_4, controls_rect_4)
        assets.screen.blit(arrow_img, arrow_rect)

        # update&clock
        pygame.display.update()
        clock.tick(120)

#pygame.quit()