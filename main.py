import pygame
from pygame.locals import *
from pygame import mixer
from classes import Tap, Hold
import math

mixer.init(44100, -16, 2, 4096)
pygame.init()
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rhota - Rhythm Game")
mixer.music.set_volume(0.7)

#achromatic is misaligned, need to rewrite, nevermeetagain is on beat but started too early
songs = {"achromatic": ['s450n', 'd460n', 'j470n', 'k480n', 'j510n', 's540n', 'd562n', 'j570n', 's600n',
 'd622n', 'd630n', 's652n', 'k660n', 'j690n', 's720n', 'd750n', 'k780n', 'j810n',
 'd840n', 'j840n', 's870n', 'd900n', 'j900n', 'k930n', 'd960n', 'j990n', 'k1020n',
 'j1042n', 'd1050n', 's1080n', 'd1102n', 'd1110n', 's1132n', 'k1140n', 'j1170n',
 's1200n', 'd1230n', 'k1230n', 'k1260n', 'j1290n', 's1290n', 's1320n', 'd1320n',
 'j1320n', 'k1320n', 's1350n', 'd1350n', 'j1350n', 'k1350n', 's1410-1430n', 'k1440-1460n', 
 's1470-1490n', 'd1500-1520n', 'd1530n', 'j1560n', 'd1580n', 's1590n', 'd1590n', 'j1590n', 
 'k1590n', 's1640n', 'd1650-1670n', 'j1680-1700n', 'd1710-1730n', 'k1740-1760n', 's1770n', 
 'j1800-1820n', 's1830n', 'd1830n', 'j1830n', 'k1830n', 's1880n', 'd1890-1910n', 
 'j1920-1940n', 'd1950-1970n', 'k1980-2000n', 's2010n', 'j2040-2060n', 'k2070n', 'j2070n', 
 'd2070n', 's2070n', 's2100n', 'd2120n', 'j2130-2150n', 'j2180n', 'k2190-2210n', 's2220-2240n', 
 'd2250-2270n', 'j2280n', 'k2310-2370n', 'd2400n', 'j2430n', 'k2460n', 'k2490n', 'j2520n', 'd2550n', 
 's2580n', 's2610n', 'k2640n', 's2670n', 'd2670n', 'j2700n', 'k2700n', 's2730-2850s', 'd2730-2850s', 
 'j2730-2850s', 'k2730-2850s', 'd2880n', 'j2910n', 'k2940n', 'k2970n', 'j3000n', 'd3030n', 's3060n', 
 's3090n', 'd3090n', 'd3120n', 'j3120n', 'k3150n', 'j3150n', 's3180n', 'k3180n', 's3210n', 'd3210n', 
 'j3240n', 'k3240n', 's3270-3330s', 'd3270-3330s', 'j3270-3330s', 'k3270-3330s', 's3360n', 'k3390n', 
 'd3420n', 'j3440n', 's3450n', 'd3480n', 'j3500n', 'k3510n', 'j3530n', 'd3540n', 's3570n', 'd3600n', 
 'j3630n', 'k3660n', 'j3690n', 'k3710n', 's3720n', 'd3750n', 's3750n', 'd3770n', 'k3780n', 'j3800n', 
 'd3810n', 's3840n', 'd3860n', 'j3870n', 'k3900n', 'j3920n', 'd3930n', 'j3960n', 'k3980n', 'j3990n', 
 'd4010n', 's4020n', 'd4050n', 'j4070n', 'k4080n', 's4110n', 'd4130n', 'j4140n', 'd4170n', 's4190n', 
 'j4200n', 'k4220n', 'd4230n', 's4250n', 's4260-4310s', 'd4260-4310s', 'j4260-4310s', 'k4260-4310s', 
 's4320n', 'k4350n', 'd4380n', 'j4400n', 'k4410n', 'j4430n', 's4440n', 'd4460n', 'k4470n', 'j4500n', 
 'd4530n', 'j4560n', 'k4590n', 's4620n', 'd4640n', 'j4650n', 'k4670n', 'j4680n', 'k4700n', 'd4710n', 
 's4730n', 'j4740n', 'k4740n', 's4770n', 'd4790n', 'j4800n', 'k4800n', 'k4830n', 'j4850n', 'd4860n', 
 's4860n', 'k4890n', 's4910n', 'd4920n', 'j4940n', 's4950n', 'd4970n', 'j4980n', 'k4980n', 's5010n', 
 'd5030n', 'j5040n', 'k5060n', 's5070n', 'k5090n', 'd5100n', 'j5120n', 'k5130n', 'j5150n', 'd5160n', 
 's5160n', 's5190-5250ss', 'd5190-5250s', 'j5190-5250s', 'k5190-5250s'],
 
 "badapple": ["s140n","s166n","s192n","s218n","k224n","s231n","k237n","s244n","s270n","s296n","k322s",
 "k335s","s348n","s376n","s401n","s427n","k433n","s440n","k446n","s453n","s479n","s505n","k529s","k542s","s555n","d581n",
 "j607n","k632n","j638n","d645n","s651n","k658n","s683n","j709n","k727s","k740s","s753n","d779n","s805n","d831n","j837n",
 "d844n","j850n","s857n","k857n","d883n","j883n","d909n","j909n","s935s","d935s","j935s","k935s","s961-987n","d974n","k993n",
 "j1000n","k1006n","d1013-1039n","j1026n","s1045n","k1052n","s1058n","k1065-1091n","s1078n","j1097n","d1104n","j1110n","s1117n",
 "k1130n","j1137n","k1143n","s1156n","d1163n",],
 
 "nevermeetagain": ["s533-640n","d650n","j667n","k683n","j699n","k716n","j733n","k749n","s766-872n","d766-872n",
 "j917n","k933n","k950n","j967n","d983n","s1000n","d1017n","j1033-1160n","k1033-1160n","s1183n","d1200n","k1217n",
 "j1233n","d1250n","s1267n","k1283n","d1300-1450n","j1300-1450n"]
}
music = {"achromatic": "achromatic.mp3", "nevermeetagain":"不重逢.mp3", "badapple":"badapple.mp3"}
tap_notes_group = pygame.sprite.Group()
hold_notes_group = []
clicked_notes = {"s":False, "d":False, "j":False, "k":False}
hold_clicked_notes = {"s":False, "d":False, "j":False, "k":False}

start = True
status = 'home'
frame = 0
running = True
clock = pygame.time.Clock()
score = 0
while running:
    for event in pygame.event.get(): 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed()
    if status == "home":
        if start:
            for sprite in tap_notes_group:
                sprite.rect.x = -2000
                sprite.kill()
            for hold in hold_notes_group:
                for sprite in hold:
                    sprite.rect.x = -2000
                    sprite.kill()
            bg = pygame.image.load("HomeBG.png").convert_alpha()
            badapple_icon = pygame.image.load("BadApple.png").convert_alpha()
            achromatic_icon = pygame.image.load("Achromatic.png").convert_alpha()
            nevermeetagain_icon = pygame.image.load("Meeting.png").convert_alpha()
            icon_list = [badapple_icon, achromatic_icon, nevermeetagain_icon]
            font = pygame.font.Font("SFNSMono.ttf", 30)
            start = False
            downkey = False
            upkey = False
            enterkey = True
        if enterkey and not pressed_keys[K_RETURN]:
            enterkey = False
        if pressed_keys[K_DOWN] and not downkey:
            icon_list.append(icon_list[0])
            icon_list.pop(0)
            downkey = True
        elif pressed_keys[K_UP] and not upkey:
            icon_list.insert(0, icon_list[-1])
            icon_list.pop()
            upkey = True
        if upkey and not pressed_keys[K_UP]:
            upkey = False
        if downkey and not pressed_keys[K_DOWN]:
            downkey = False
        
        if icon_list[1] == achromatic_icon:
            song_text = "Self-Inflicted Achromatic"
            song_rend = font.render(song_text, True, (0,0,0))
        elif icon_list[1] == badapple_icon:
            song_text = "Bad Apple!!"
            song_rend = font.render(song_text, True, (0,0,0))
        elif icon_list[1] == nevermeetagain_icon:
            song_text = "Never Meet Again"
            song_rend = font.render(song_text, True, (0,0,0))
        song_rect = song_rend.get_rect(center = (240, 175))
        if pressed_keys[K_RETURN] and not enterkey:
            if icon_list[1] == badapple_icon:
                status = "badapple"
            elif icon_list[1] == nevermeetagain_icon:
                status = "nevermeetagain"
            elif icon_list[1] == achromatic_icon:
                status = "achromatic"
            start = True
            frame = 0
        screen.blit(bg, (0,0))
        screen.blit(icon_list[0], (90, -220))
        screen.blit(icon_list[1], (90, 250))
        screen.blit(icon_list[2], (90, 715))
        screen.blit(song_rend, song_rect)

    elif status != "score" and status != "home":
        score = min(1000000, score)
        if start:
            bg = pygame.image.load(status + "bg.png")
            start = False
            total_score_time = 0
            for note in songs[status]:
                if "-" in note:
                    print(note)
                    note_sep = note.split("-")
                    new_note = Hold(note_sep[0][1:], note_sep[1][:-1], note_sep[0][0], note_sep[1][-1])
                    hold_notes_group.append(new_note)
                    if new_note.type == "n":
                        total_score_time += 2
                    else:
                        total_score_time += 4
                else:
                    new_note = Tap(note[1:-1], note[0], note[-1])
                    tap_notes_group.add(new_note)
                    if new_note.type == "n":
                        total_score_time += 1
                    else:
                        total_score_time += 2
            score = 0
            mixer.music.load(music[status])
            mixer.music.play()
        if "-" in songs[status][-1][1:-1]:
            if frame >= int(songs[status][-1][songs[status][-1].index("-")+1:-1]) + 50:
                status = "score"
                start = True
        else:
            if frame >= int(songs[status][-1][1:-1]) + 50:
                status = "score"
                start = True

        frame += 1
        active_holds = {note for note in hold_notes_group if note.init and not note.endClick}
        for note in tap_notes_group:
            if not note.init and note.time - frame == 80:  
                note.init = True
            if note.init:
                clicked_notes, score_add = note.update(frame, pressed_keys, clicked_notes, hold_clicked_notes, total_score_time, active_holds)
                score += score_add
        for note in hold_notes_group:
            if not note.init and note.startTime - frame == 80:
                note.init = True
            if note.init:
                hold_clicked_notes, score_add = note.update(frame, pressed_keys, hold_clicked_notes, clicked_notes, total_score_time)
                score += score_add
        
        screen.blit(bg, (0, 0))
        font = pygame.font.Font("SFNSMono.ttf", 25)
        score_text = "0" * (7-len(str(score))) + str(score)
        score_rend = font.render(score_text, True, (255,255,255))
        score_rect = score_rend.get_rect(center = (60, 20))
        screen.blit(score_rend, score_rect)
        for note in hold_notes_group:
            note.draw(screen)
        tap_notes_group.draw(screen)
    elif status == "score":
        if start: 
            mixer.music.stop()
            if score/1000000 > 0.95:
                bg = pygame.image.load("100.png").convert_alpha()
            elif score/1000000 > 0.9:
                bg = pygame.image.load("90.png").convert_alpha()
            elif score/1000000 > 0.6:
                bg = pygame.image.load("60.png").convert_alpha()
            else:
                bg = pygame.image.load("10.png").convert_alpha()
            score_font = pygame.font.Font("SFNSMono.ttf", 65)
            percent_font = pygame.font.Font("SFNSMono.ttf", 50)

            score_text = "0" * (7-len(str(score))) + str(score)
            score_rend = score_font.render(score_text, True, (0,0,0))
            score_rect = score_rend.get_rect(center = (240, 400))
            percent_text = str(round(1000000/score * 100, 1)) + "%"
            percent_rend = percent_font.render(percent_text, True, (0,0,0))
            percent_rect = percent_rend.get_rect(center = (240, 480))
            start = False
        if pressed_keys[K_RETURN]:
            status = 'home'
            start = True
        screen.blit(bg, (0,0))
        screen.blit(score_rend, score_rect)
        screen.blit(percent_rend, percent_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit() 
