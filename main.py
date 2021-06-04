import random
import time
import pygame
from pygame import sprite
from pygame.locals import *
import sys
import sys
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



pygame.font.init()
width, height = 600, 400


def Cal_Gain(value, item, k, bet):
    x, y, z = k[0], k[1], k[2]
    if x == y == z:
        return value[item.index(x)] * bet * 2
    elif x == y:
        return value[item.index(x)] * bet
    else:
        return 0


def load_image(name):
    asset_url = resource_path(name)
    image = pygame.image.load(asset_url)
    image = pygame.transform.scale(image, (width, height))
    return image


class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('static/casino_welcome_1.jpg'))
        self.images.append(load_image('static/casino_welcome_2.jpg'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 600, 400)

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


def casino(points, best, bet):
    item = ["Apple", "Cat", "Ace", "Huge"]
    value = [1, 2, 3, 5]
    gain = 0
    k = []
    if points >= bet:
        points = points - bet
        i = 0
        while i != 3:
            v = random.choice(item)
            k.append(v)
            i += 1
        gain = Cal_Gain(value, item, k, bet)

        points = points + gain
        if best < points:
            best = points
    return points, k, best, gain


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Casino')
    running = True

    # For display Welcome
    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)
    welcome = USEREVENT
    pygame.time.set_timer(welcome, 1)
    flag_0 = 0

    # For Display Start
    Start = USEREVENT + 4
    pygame.time.set_timer(Start, 1000)
    image_1 = load_image('static/Start_1.jpg')
    image_2 = load_image('static/Start_2.jpg')
    image_3 = load_image('static/Start_3.jpg')
    Start_Rect = pygame.Rect(80, 60, 120, 65)
    Quit_Rect = pygame.Rect(90, 148, 105, 50)
    flag_1 = 0
    flag_4 = 0  # For ending Start Display Event

    # For Slot
    image_4 = load_image('static/Slot_1.jpg')
    Slot_flag = 0  # Start of Slot Event

    # For Text_Point
    asset_url = resource_path("static/comic.ttf")
    font = pygame.font.Font(asset_url, 25)
    text_Point = font.render('Points: ', True, (0, 255, 0))
    text_Best = font.render('Best: ', True, (0, 255, 0))
    text_Win = font.render('Win: ', True, (0, 255, 0))

    # Push Slot
    image_5 = load_image('static/Slot_2.jpg')
    Push_Slot_Rect = pygame.Rect(470, 130, 30, 70)
    bg = image_4

    # Quit Slot
    Quit_Rect_2 = pygame.Rect(513, 271, 80, 39)
    image_7 = load_image('static/Slot_1Quit.jpg')

    # Plus
    Plus_Rect = pygame.Rect(19, 317, 37, 37)
    image_8 = load_image('static/Slot_Plus.jpg')

    # Minus
    Minus_Rect = pygame.Rect(79, 317, 37, 37)
    image_9 = load_image('static/Slot_Minus.jpg')

    # Bet Amount
    Bet_Amt = 100
    Bet_Amt_Text = font.render(str(Bet_Amt), True, (0, 255, 0))

    # Points
    Points = 1000
    Points_Amt_Text = font.render(str(Points), True, (0, 255, 0))

    # Best
    Best_Amt = Points
    Best_Amt_Text = font.render(str(Best_Amt), True, (0, 252, 0))

    #
    Gain_Amt = 0
    Gain_Amt_Text = font.render(str(Gain_Amt), True, (0, 252, 0))
    # Casino Guess
    Guess_1 = 'Apple'
    Guess_2 = 'Apple'
    Guess_3 = 'Apple'
    Guess_1Text = font.render(Guess_1, True, (0, 252, 0))
    Guess_2Text = font.render(Guess_2, True, (0, 252, 0))
    Guess_3Text = font.render(Guess_3, True, (0, 252, 0))

    # End
    font2 = pygame.font.Font(asset_url, 50)
    Lose_Text = font2.render('You Lose', True, (0, 252, 0))

    # Main Loop
    while running:
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                running = False
            if Slot_flag == 0:
                # Welcome
                if event.type == welcome:
                    my_group.update()
                    my_group.draw(screen)
                    pygame.display.flip()
                    flag_1 = 0
                # Start
                if flag_0 == 0 and Slot_flag == 0:
                    if event.type == Start:
                        flag_0 = 1
                if event.type == Start or (event.type == pygame.MOUSEBUTTONDOWN and flag_0 == 1):
                    if flag_1 == 0:
                        pygame.time.set_timer(welcome, 0)
                        pygame.time.set_timer(Start, 1)
                        screen.blit(image_1, [0, 0])
                        flag_1 = 1
                    if Start_Rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(image_2, [0, 0])
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                Slot_flag = 1
                    elif Quit_Rect.collidepoint(pygame.mouse.get_pos()):
                        screen.blit(image_3, [0, 0])
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                running = False
                    else:
                        screen.blit(image_1, [0, 0])
                        flag = 0
            # Slot
            else:
                # Ending Prev Event
                if flag_4 == 0:
                    flag_0 = 0
                    flag_4 = 1
                if Push_Slot_Rect.collidepoint(pygame.mouse.get_pos()):
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            bg = image_5

                            Points, [Guess_1, Guess_2, Guess_3], Best_Amt, Gain_Amt = casino(Points, Best_Amt, Bet_Amt)
                            Guess_1Text = font.render(Guess_1, True, (0, 252, 0))
                            Guess_2Text = font.render(Guess_2, True, (0, 252, 0))
                            Guess_3Text = font.render(Guess_3, True, (0, 252, 0))
                            Gain_Amt_Text = font.render(str(Gain_Amt), True, (0, 252, 0))
                            Best_Amt_Text = font.render(str(Best_Amt), True, (0, 252, 0))
                            Points_Amt_Text = font.render(str(Points), True, (0, 255, 0))

                    else:
                        bg = image_4
                elif Quit_Rect_2.collidepoint(pygame.mouse.get_pos()):
                    bg = image_7
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            running = False
                elif Plus_Rect.collidepoint(pygame.mouse.get_pos()):
                    bg = image_8
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            Bet_Amt += 100
                            Bet_Amt_Text = font.render(str(Bet_Amt), True, (0, 255, 0))
                elif Minus_Rect.collidepoint(pygame.mouse.get_pos()):
                    bg = image_9
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            Bet_Amt -= 100
                            if Bet_Amt < 100:
                                Bet_Amt = 100
                            Bet_Amt_Text = font.render(str(Bet_Amt), True, (0, 255, 0))
                else:
                    bg = image_4
                screen.blit(bg, [0, 0])
                screen.blit(text_Point, (0, 0))
                screen.blit(text_Best, (0, 40))
                screen.blit(text_Win, (190, 350))
                screen.blit(Bet_Amt_Text, (19, 220))
                screen.blit(Points_Amt_Text, (80, 0))
                screen.blit(Best_Amt_Text, (62, 40))
                screen.blit(Gain_Amt_Text, (250, 350))
                if Points < 100:
                    screen.blit(Lose_Text, (200, 65))
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            running = False
                else:
                    screen.blit(Guess_1Text, (190, 90))
                    screen.blit(Guess_2Text, (270, 90))
                    screen.blit(Guess_3Text, (350, 90))
                # pygame.draw.rect(screen,(0,0,0),(500,200,37,37))
        pygame.time.delay(100)
        pygame.display.update()
    # casino()
