import pygame
import sys
import assets

pygame.init()
clock = pygame.time.Clock()

arrow_img = pygame.transform.flip(pygame.image.load("assets/back.png"), True, False)
arrow_rect = arrow_img.get_rect(center=(640, 550))

controls_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 40)
controls_text_1 = controls_font.render("Objective:", True, (255, 255, 255))
controls_rect_1 = controls_text_1.get_rect(center=(640, 300))

controls_text_2 = controls_font.render("Kill all alien spawns", True, (255, 255, 255))
controls_rect_2 = controls_text_2.get_rect(center=(640, 350))

controls_text_3 = controls_font.render("--------------------", True, (255, 255, 255))
controls_rect_3 = controls_text_3.get_rect(center=(640, 400))

controls_text_4 = controls_font.render("If you fly too high, you will get sun damage.", True, (255, 255, 255))
controls_rect_4 = controls_text_4.get_rect(center=(640, 450))

controls_text_5 = controls_font.render("If you fly too low, ground defenses will be triggered.", True, (255, 255, 255))
controls_rect_5 = controls_text_5.get_rect(center=(640, 500))

# objective two
controls_text_6 = controls_font.render("Kill all space hunters", True, (255, 255, 255))
controls_rect_6 = controls_text_6.get_rect(center=(640, 350))

controls_text_8 = controls_font.render("Level two", True, (255, 255, 255))
controls_rect_8 = controls_text_8.get_rect(center=(640, 150))

# objective three
controls_text_7 = controls_font.render("Kill final boss", True, (255, 255, 255))
controls_rect_7 = controls_text_7.get_rect(center=(640, 350))

controls_text_9 = controls_font.render("Level three", True, (255, 255, 255))
controls_rect_9 = controls_text_9.get_rect(center=(640, 150))


def play_objective_one():
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
        assets.screen.blit(controls_text_5, controls_rect_5)
        assets.screen.blit(arrow_img, arrow_rect)

        # update&clock
        pygame.display.update()
        clock.tick(120)


def play_objective_two():
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
        assets.screen.blit(controls_text_6, controls_rect_6)
        assets.screen.blit(controls_text_8, controls_rect_8)
        assets.screen.blit(arrow_img, arrow_rect)

        # update&clock
        pygame.display.update()
        clock.tick(120)


def play_objective_three():
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
        assets.screen.blit(controls_text_7, controls_rect_7)
        assets.screen.blit(controls_text_9, controls_rect_9)
        assets.screen.blit(arrow_img, arrow_rect)

        # update&clock
        pygame.display.update()
        clock.tick(120)


#pygame.quit()