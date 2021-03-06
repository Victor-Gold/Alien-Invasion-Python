import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and its starting positions."""
        
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #movement of ship
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship at its current location"""
        
        self.screen.blit(self.image, self.rect)

        #Update rect object from self.center
        
        self.rect.centerx = self.center

    def update(self):   #To update the ship center value not rect
        """Update the ship position based on the movement flag"""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            
        if self.moving_left and self.rect.left > 0:
            
            self.center -= self.ai_settings.ship_speed_factor

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx


    


            
            
        
        
        
        
        
