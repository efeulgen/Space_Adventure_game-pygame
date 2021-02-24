import pygame
import assets


def mission_message():
    message_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 15)
    mission_message_text = message_font.render("Kill all alien spawns.", True, (255, 255, 255))
    mission_message_rect = mission_message_text.get_rect(center=(1080, 670))
    assets.screen.blit(mission_message_text, mission_message_rect)


def sun_damage_message():
    message_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 15)
    sun_damage_message_text = message_font.render("You are too close sun, lower altitude.", True, (255, 255, 255))
    sun_damage_message_rect = sun_damage_message_text.get_rect(center=(1080, 670))
    assets.screen.blit(sun_damage_message_text, sun_damage_message_rect)


def missile_range_message():
    message_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 15)
    missile_range_message_text = message_font.render("You are in the missile range.", True, (255, 255, 255))
    missile_range_message_rect = missile_range_message_text.get_rect(center=(1080, 670))
    assets.screen.blit(missile_range_message_text, missile_range_message_rect)


def play_again_message():
    message_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 40)
    play_again_message_text = message_font.render("(P)lay Again/ (Q)uit", True, (255, 255, 255))
    play_again_message_rect = play_again_message_text.get_rect(center=(640, 500))
    assets.screen.blit(play_again_message_text, play_again_message_rect)


def you_win_message():
    message_font = pygame.font.Font("fonts/LazenbyCompSmooth.ttf", 80)
    you_win_message_text = message_font.render("You Win!", True, (255, 255, 255))
    you_win_message_rect = you_win_message_text.get_rect(center=(640, 360))
    assets.screen.blit(you_win_message_text, you_win_message_rect)
