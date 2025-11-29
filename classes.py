import pygame
from pygame.locals import *

class Tap(pygame.sprite.Sprite):
    def __init__(self, time, lane, type):
        super().__init__()
        self.time = int(time)
        self.lane = lane
        self.type = type
        self.init = False
        self.speed = 8
        if self.type == "n":
          self.image = pygame.image.load("NormalTap.png").convert_alpha()
        else:
            self.image = pygame.image.load("DoubleTap.png").convert_alpha()
        if self.lane == "s":
            self.rect = self.image.get_rect(center = (60, -20))
        elif self.lane == "d":
            self.rect = self.image.get_rect(center = (180, -20))
        elif self.lane == "j":
            self.rect = self.image.get_rect(center = (300, -20))
        else:
            self.rect = self.image.get_rect(center = (420, -20))
    def update(self, frame, keys, clicked_lanes, hold_clicked_lanes, score_time, active_holds):
        self.rect.move_ip(0, self.speed)
        if self.rect.centery > 810:
            self.kill()

        if self.type == "s":
            multi = 2
        else:
            multi = 1
        score = 0
        overlap = False
        for hold_note in active_holds:
            if abs(hold_note.startTime - frame) < abs(self.time - frame):
                overlap = True
        if overlap:
            score = 0
        else:
            if self.lane == "s" and not keys[K_s] or self.lane == "d" and not keys[K_d] or self.lane == "j" and not keys[K_j] or self.lane == "k" and not keys[K_k]:
                clicked_lanes[self.lane] = False
            if not clicked_lanes[self.lane] and not hold_clicked_lanes[self.lane]:
                if self.lane == "s" and keys[K_s] or self.lane == "d" and keys[K_d] or self.lane == "j" and keys[K_j] or self.lane == "k" and keys[K_k]:
                    clicked_lanes[self.lane] = True
                    if self.time - frame > -8 and self.time - frame < 8:
                        self.rect.x = -2000
                        self.init = False
                        self.kill()
                        score = round(1000000/score_time * multi)
                    elif self.time - frame > -12 and self.time - frame < 12:
                        self.rect.x = -2000
                        self.init = False
                        self.kill()
                        score = round(0.9*1000000/score_time * multi)
                    elif self.time - frame > -30 and self.time - frame < 30:
                        self.rect.x = -2000
                        self.init = False
                        self.kill()
                        score = round(0.6*1000000/score_time * multi)
        return clicked_lanes, score

class Hold(pygame.sprite.Group):
    def __init__(self, startTime, endTime, lane, type):
        super().__init__()
        self.startTime = int(startTime)
        self.endTime = int(endTime)
        self.lane = lane
        self.type = type
        self.init = False
        self.startClick = False
        self.endClick = False
        self.speed = 8
        self.held = False
        self.ended = False

        length = (int(endTime)-int(startTime)) * self.speed // 10

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
            if self.lane == "s":
                x.rect = x.image.get_rect(center=(60, -10*i - 20))
            elif self.lane == "d":
                x.rect = x.image.get_rect(center=(180, -10*i - 20))
            elif self.lane == "j":
                x.rect = x.image.get_rect(center=(300, -10*i - 20))
            else:
                x.rect = x.image.get_rect(center=(420, -10*i - 20))
            self.add(x)
    def update(self, frame, keys, clicked_lanes, tap_clicked_lanes, score_time):
        for sprite in self:
            sprite.rect.move_ip(0, self.speed)
            if sprite.rect.centery > 810:
                sprite.kill()

        score = 0
        if self.type == "s":
            multi = 2
        else:
            multi = 1
        
        in_hit_box = any(440 < sprite.rect.centery < 700 for sprite in self)

        if self.startClick and not self.held and frame > self.endTime:
            self.held = True
            if not self.ended:
                score = round(1000000/score_time * multi)
                self.ended = True
        
        if self.startClick:
            for sprite in self:
                if sprite.rect.centery > 650:
                    sprite.rect.x = -2000
                    sprite.kill()
                if self.lane == "s" and not keys[K_s] or self.lane == "d" and not keys[K_d] or self.lane == "j" and not keys[K_j] or self.lane == "k" and not keys[K_k]:
                    clicked_lanes[self.lane] = False
                    self.startClick = False
                    if self:
                        self.endClick = True
        elif self.endClick and not self.ended:
            if self.endTime - frame > -10 and self.endTime - frame < 8:
                score = round(1000000/score_time * multi)
            elif self.endTime - frame > -15 and self.endTime - frame < 12:
                score = round(0.9*1000000/score_time * multi)
            elif self.endTime - frame > -30 and self.endTime - frame < 30:
                score = round(0.6*1000000/score_time * multi)
            self.ended = True
        elif in_hit_box:
            if not clicked_lanes[self.lane] and not tap_clicked_lanes[self.lane]:
                if self.lane == "s" and keys[K_s] or self.lane == "d" and keys[K_d] or self.lane == "j" and keys[K_j] or self.lane == "k" and keys[K_k]:
                    clicked_lanes[self.lane] = True
                    if self.startTime - frame > -10 and self.startTime - frame < 8:
                        self.startClick = True
                        score = round(1000000/score_time * multi)
                    elif self.startTime - frame > -15 and self.startTime - frame < 12:
                        self.startClick = True
                        score = round(0.9*1000000/score_time * multi)
                    elif self.startTime - frame > -30 and self.startTime - frame < 30:
                        self.startClick = True
                        score = round(0.6*1000000/score_time * multi)
                    elif self.endTime < frame:
                        score = 0
        if (self.lane == "s" and not keys[K_s] or 
            self.lane == "d" and not keys[K_d] or 
            self.lane == "j" and not keys[K_j] or 
            self.lane == "k" and not keys[K_k]):
            clicked_lanes[self.lane] = False
            tap_clicked_lanes[self.lane] = False
        return clicked_lanes, score

