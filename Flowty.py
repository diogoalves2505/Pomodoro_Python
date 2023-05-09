import pygame
import sys
from button import Button
import os
import time
 
filename = "level.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("1\n0")

with open(filename, "r") as f:
    level, xp = map(int, f.read().split())

pygame.init()

WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flowty")
icon = pygame.image.load("assets/tomato.png")
pygame.display.set_icon(icon)

CLOCK = pygame.time.Clock()
 
BACKDROP = pygame.image.load("assets/backdrop.png")
WHITE_BUTTON = pygame.image.load("assets/button.png")
 
FONT = pygame.font.Font("assets/digital-7.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))
 
START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#181818", "#0078d4")
POMODORO_BUTTON = Button(None, (WIDTH/2-150, HEIGHT/2-140), 120, 30, "Pomodoro", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#f1f1f1", "#c0c0c0")
SHORT_BREAK_BUTTON = Button(None, (WIDTH/2, HEIGHT/2-140), 120, 30, "Short Break", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#f1f1f1", "#c0c0c0")
LONG_BREAK_BUTTON = Button(None, (WIDTH/2+150, HEIGHT/2-140), 120, 30, "Long Break", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#f1f1f1", "#c0c0c0")
 
POMODORO_LENGTH = 1500 # 1500 secs / 25 mins
SHORT_BREAK_LENGTH = 300 # 300 secs / 5 mins
LONG_BREAK_LENGTH = 900 # 900 secs / 15 mins
 
current_seconds = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

font = pygame.font.Font('assets/ArialRoundedMTBold.ttf', 32)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open(filename, "w") as f:
                f.write(str(level) + "\n" + str(xp))
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                    START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#181818", "#0078d4")
                else:
                    started = True
                    START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "STOP", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#181818", "#0078d4")

            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                started = False
            
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                started = False

            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                started = False
                    
        if event.type == pygame.USEREVENT and started:
            current_seconds -=1
            

    SCREEN.fill("#181818")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())


    if current_seconds >=0:

        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
        timer_text = FONT.render(f"{display_minutes:02d}:{display_seconds:02d}", True, "white")
        SCREEN.blit(timer_text, timer_text_rect)


    if display_minutes == 0 and display_seconds == 0 :
        time.sleep(1)
        current_seconds = POMODORO_LENGTH
        xp += 10
        started = False
        START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#181818", "#0078d4")

 
    if xp >= 100:
        level += 1
        xp -= 100

    text = font.render(f"Nível: {level}     XP: {xp}", True, ("#f1f1f1"))
    SCREEN.blit(text, (600, 10))

    pygame.display.update()