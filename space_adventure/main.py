import pygame
import sys
import main_menu
import space_adventure_level_one
import space_adventure_level_two
import space_adventure_final_boss
import controls
import objectives
pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_menu.play_main_menu()
    controls.play_controls()
    objectives.play_objective_one()
    space_adventure_level_one.play_level_one()
    objectives.play_objective_two()
    space_adventure_level_two.play_level_two()
    objectives.play_objective_three()
    space_adventure_final_boss.play_final_boss_fight()

pygame.quit()
