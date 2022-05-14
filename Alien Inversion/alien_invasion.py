import sys
import pygame
from pygame.sprite import Group

from button import Button
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from game_stats import GameStats

import game_functions as gf

def run_game():

    """Initialize game and create a screen object"""

    #Initialize game and creat screen object and screen settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                             ai_settings.screen_height))
    
    
    pygame.display.set_caption("Alien Invasion")

    #Make the Play button
    play_button = Button(ai_settings, screen, 'Play')

    #Create Instance to store game statistics
    stats = GameStats(ai_settings)

    #Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings , screen)
    
    #Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    
    #Create a fleet of alien

    gf.create_fleet(ai_settings, screen ,ship ,aliens)
    
    #Make score board
    sb = Scoreboard(ai_settings, screen, stats)


    #Start the main loop for the game
    while True:

        #Watch for key board and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
           bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship , aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship , aliens , bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
        play_button)
        
        
        

        
        
run_game()
