
import pygame, sys
import string
from settings import *
from button import Button

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('SPY')


font1 = pygame.font.SysFont('dejavusans', 15)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 30)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

mark_button = Button(screen_width-50,screen_height-690, question_mark_img)
start_button = Button(screen_width-  700,screen_height-690, start_img)




click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        #draw_text('main menu', font1, (255, 255, 255), screen, 20, 20)
        draw_text('Welcome To Spy', font2, (255, 255, 255), screen, screen_width // 3 ,screen_height // 2.5)
        screen.blit(spy_img, ( screen_width // 3 ,screen_height // 2))




        #button_1 = pygame.Rect(50, 100, 200, 50)
        #button_2 = pygame.Rect(50, 200, 200, 50)
        if mark_button.draw():
            rules()

        if start_button.draw():
            game()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('game', font1, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def rules():
    i_a = intermediate.get_rect()
    x1 = i_a[0]
    x2 = x1 + i_a[2]
    a, b = (255, 0, 0), (60, 255, 120)
    y1 = i_a[1]
    y2 = y1 + i_a[3]
    h = y2 - y1
    rate = (float((b[0] - a[0]) / h),
            (float(b[1] - a[1]) / h),
            (float(b[2] - a[2]) / h)
            )
    for line in range(y1, y2):
        color = (min(max(a[0] + (rate[0] * line), 0), 255),
                 min(max(a[1] + (rate[1] * line), 0), 255),
                 min(max(a[2] + (rate[2] * line), 0), 255)
                 )
        pygame.draw.line(intermediate, color, (x1, line), (x2, line))

    y = 20
    f = pygame.font.SysFont('', 17)
    for l in string.ascii_uppercase:
        intermediate.fill((0, 0, 0))
        intermediate.blit(qa_img, (screen_width // 3, screen_height - 700))

        y += 20



    scroll_y = 0


    running = True
    while running:


        draw_text('Rules', font1, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                if event.button == 5: scroll_y = max(scroll_y - 15, -300)

        screen.blit(intermediate, (0, scroll_y))
        draw_text('WHAT DO WE START WITH ?', font3, "red", intermediate, screen_width // 18, screen_height // 2.5)
        draw_text('CHOOSE THE GAME SETTINGS: A WORD PACK, PLAYING TIME, THE NUMBER OF PLAYERS AND SPIES. ',
                  font1, "white", intermediate, screen_width // 18, screen_height // 2.2)
        draw_text('WHAT NEXT ?', font3, "red", intermediate, screen_width // 18, screen_height // 2)
        draw_text('THERE ARE TWO TYPES OF ROLES: LOCALS AND SPIES.TAP THE SCREEN WHEN IT IS YOUR TURN ',font1, "white",
                  intermediate, screen_width // 18, screen_height // 1.8)
        draw_text('AND YOU WILL SEE YOUR CARD. ', font1, "white",
                  intermediate, screen_width // 18, screen_height // 1.7)
        draw_text('CAN ANOTHER PLAYER SEE MY ROLE?', font3, "red", intermediate, screen_width // 18, screen_height // 1.5)
        draw_text('NO THEY CAN\'T.WHEN YOU TAP THE CARD ONLY YOU ARE ABLE TO SEE IT ', font1, "white",
                  intermediate, screen_width // 18, screen_height // 1.4)
        draw_text('HOW DO WE PLAY?', font3, "red", intermediate, screen_width // 18,
                  screen_height // 1.3)
        draw_text('AFTER EVERYONE HAS GOT THEIR ROLE, START ASKING EACH OTHER QUESTIONS CONNECTED WITH  ', font1, "white",
                  intermediate, screen_width // 18, screen_height // 1.2)
        draw_text('THE LOCATION.FOR EXAMPLE : "HOW OFTEN TO YOU GO THERE?"  ', font1,
                  "white",
                  intermediate, screen_width // 18, screen_height // 1.15)
        draw_text('I HAVE A GUESS ABOUT WHO THE SPY IS. WHAT SHOULD I DO?', font3, "red", intermediate, screen_width // 18,
                  screen_height // 1.1)
        draw_text('PRESS THE "I KNOW" BUTTON. THEN AFTER 3 SECONDS ALL THE PLAYERS SHOULD CHOOSE ',font1, "white",
                  intermediate, screen_width // 18, screen_height // 1.05)
        draw_text('THE PERSON WHO IS THE SPY IN THEIR VIEW.IF ALL THE PLAYERS HAVE CHOSEN THE SAME PERSON ',font1, "white",
                  intermediate, screen_width // 18, screen_height// 1.02 )
        draw_text('THE PERSON REVEALS THE CARD.IF THE PERSON IS SPY, LOCALS WIN,IF NOT, SPY WINS ', font1,
                  "white",
                  intermediate, screen_width // 18, screen_height + 7)
        draw_text('I AM THE SPY AND I KNOW THE WORD, WHAT SHOULD I DO?', font3, "red", intermediate,
                  screen_width // 18,  screen_height + 35)
        draw_text('PRESS "I KNOW" BUTTON AND IF YOU ARE RIGHT - YOU WIN. IF NOT - YOU LOOSE ', font1,
                  "white",
                  intermediate, screen_width // 18, screen_height + 60)


        pygame.display.flip()
        mainClock.tick(60)


main_menu()