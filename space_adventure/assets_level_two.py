import pygame
import random
from assets import screen


class BackgroundLevelTwo:
    background_img = pygame.image.load("assets/deep_space_bg_1280x720.png")
    background_1_x = 0
    background_2_x = 1280
    background_increment = -1
    background_respwan = 1280

    def show_bg_level_two(self):
        screen.blit(self.background_img, (self.background_1_x, 0))
        screen.blit(self.background_img, (self.background_2_x, 0))

        self.background_1_x += self.background_increment
        if self.background_1_x <= -1280:
            self.background_1_x = self.background_respwan

        self.background_2_x += self.background_increment
        if self.background_2_x <= -1280:
            self.background_2_x = self.background_respwan


class SpaceHunter:
    hunter_img = pygame.image.load("assets/space_hunter.png")
    hunter_x = 1300
    hunter_y = 100
    hunter_rects = []
    hunter_speeds = []
    hunter_lifes = [3, 3, 3, 3, 3, 3, 3]
    for i in range(7):
        hunter_rects.append(hunter_img.get_rect(center=(hunter_x, hunter_y)))
        hunter_speeds.append(random.choice([4, -4]))
        hunter_y += 80

    def show_hunter(self):
        for index, hunter in enumerate(self.hunter_rects):
            screen.blit(self.hunter_img, hunter)
            if not hunter.x <= 1150:
                hunter.x += -2

            else:
                hunter.y += self.hunter_speeds[index]
                if hunter.top <= 0 or hunter.bottom >= 720:
                    self.hunter_speeds[index] *= -1

    def reset_hunter(self):
        self.hunter_x = 1300
        self.hunter_y = 100
        for i in range(7):
            self.hunter_rects.append(self.hunter_img.get_rect(center=(self.hunter_x, self.hunter_y)))
            self.hunter_speeds.append(random.choice([4, -4]))
            self.hunter_y += 80

        self.hunter_lifes = [3, 3, 3, 3, 3, 3, 3]
