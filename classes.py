import pygame
from pygame.locals import *

class Tap(pygame.sprite.Sprite):
    def __init__(self, time, lane, type):
        self.time = time
        self.lane = lane
        self.type = type
        self.init = False
        self.speed = 8
        if self.type == "n":
            self.image = pygame.image.load("NormalTap.png").convert_alpha()
        else:
            self.image = pygame.image.load("SpecialTap.png").convert_alpha()
        if self.lane == "s":
            self.rect = self.image.get_rect(center = (60, -20))
        elif self.lane == "d":
            self.rect == self.image.get_rect(center = (180, -20))
        elif self.lane == "j":
            self.rect == self.image.get_rect(center = (300, -20))
        else:
            self.rect == self.image.get_rect(center = (420, -20))
    def update(self, frame, keys):
        pass

class Hold(pygame.sprite.Group):
    def __init__(self, startTime, endTime, lane, type):
        self.startTime = startTime
        self.endTime = endTime
        self.lane = lane
        self.type = type
        self.init = False
        self.startClick = False
        self.endClick = False
        self.speed = 8

        length = (int(endTime)-int(startTime))*8//10
        for i in range(length):
            x = pygame.sprite.Sprite()
            if i == 0:
                if self.type == "n":
                    x.image = pygame.image.load("HoldStart.png")
                else:
                    x.image = pygame.image.load("SpecialHoldStart.png")
            elif i == length - 1:
                if self.type == "n":
                    x.image = pygame.image.load("HoldEnd.png")
                else:
                    x.image = pygame.image.load("SpecialHoldEnd.png")
            else:
                if self.type == "n":
                    x.image = pygame.image.load("HoldMiddle.png")
                else:
                    x.image = pygame.image.load("SpecialHoldMiddle.png")

        