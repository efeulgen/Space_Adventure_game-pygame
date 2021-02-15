import pygame
from pygame import mixer
import random

screen = pygame.display.set_mode((1280, 720))


def play_music():
    mixer.music.load("sounds/scifi_game_music.wav")
    mixer.music.play(-1)


class Background:
    background_img = pygame.image.load("assets/bg_moonsurface.png")
    bg_1_x = 0
    bg_2_x = 1280
    bg_increment = -1
    bg_respawn_point = 1280

    def show_background(self):
        screen.blit(self.background_img, (self.bg_1_x, 0))
        screen.blit(self.background_img, (self.bg_2_x, 0))
        self.bg_1_x += self.bg_increment
        if self.bg_1_x <= -1280:
            bg_1_x = self.bg_respawn_point

        self.bg_2_x += self.bg_increment
        if self.bg_2_x <= -1280:
            bg_2_x = self.bg_respawn_point


class Player:
    player__img = pygame.image.load("assets/spaceship_yeni.png")
    player_img = pygame.transform.rotate(player__img, -90)
    player_pos_x = 150
    player_pos_y = 0
    player_rect = player_img.get_rect(center=(player_pos_x, player_pos_y))

    def show_player(self):
        screen.blit(self.player_img, self.player_rect)
        if self.player_rect.top <= 0:
            self.player_rect.top = 30
        elif self.player_rect.bottom >= 720:
            self.player_rect.bottom = 720


class Enemy:
    bug_img = pygame.image.load("assets/hostile_ai_spawns.png")
    bug_rect_list = []
    bug_speeds = []
    for i in range(15):
        bug_rect_list.append(bug_img.get_rect(center=([random.randint(1300, 1400), random.randint(200, 600)])))
        bug_speeds.append([random.choice([3, 2, -2, -3]), random.choice([3, 2, -2, -3])])

    bug_rect_list.sort(key=lambda item: item[0])
    bugs_in_arena = False

    def move_bugs_to_arena(self):
        if not self.bugs_in_arena:
            for bug_rect in self.bug_rect_list:
                screen.blit(self.bug_img, bug_rect)
                bug_rect.x -= 4
            if self.bug_rect_list[-1][0] <= 1200:
                self.bugs_in_arena = True

    def show_bugs(self):
        if self.bugs_in_arena:
            for index, bug_rect in enumerate(self.bug_rect_list):
                screen.blit(self.bug_img, bug_rect)
                bug_rect.x += self.bug_speeds[index][0]
                bug_rect.y += self.bug_speeds[index][1]

                if 0 >= bug_rect.left or 1280 <= bug_rect.right:
                    self.bug_speeds[index][0] *= -1

                if 0 >= bug_rect.top or 720 <= bug_rect.bottom:
                    self.bug_speeds[index][1] *= -1


class Laser:
    laser__img = pygame.image.load("assets/laser.png")
    laser_img = pygame.transform.rotate(laser__img, 90)
    laser_rect_list = []

    def fire(self):
        for laser_pos in self.laser_rect_list:
            screen.blit(self.laser_img, (laser_pos.x + 70, laser_pos.y + 30))
            laser_pos[0] += 8
            if laser_pos[0] >= 1290:
                self.laser_rect_list.remove(laser_pos)


class GroundMissile:
    missile__img = pygame.image.load("assets/missile.png")
    missile_img = pygame.transform.rotate(missile__img, 45)
    missile_rect_list = []
    def shoot_missile(self):
        for missile_rect in self.missile_rect_list:
            screen.blit(self.missile_img, missile_rect)
            missile_rect.x -= 4
            missile_rect.y -= 4


class Life:
    player_life_img = pygame.image.load("assets/life_sign_1.png")
    player_life_x = 20
    player_life_rect_list = []
    for i in range(3):
        player_life_rect_list.append(player_life_img.get_rect(center=(player_life_x, 20)))
        player_life_x += 30

    def show_life(self):
        for life in self.player_life_rect_list:
            screen.blit(self.player_life_img, life)


class GameOverSign:
    gameOver_img = pygame.image.load("assets/game_over.png")
    gameOver_rect = gameOver_img.get_rect(center=(640, 360))


class LevelOverSign:
    levelOver_img = pygame.image.load("assets/level_complete.png")
    levelOver_rect = levelOver_img.get_rect(center=(640, 360))
