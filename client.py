import string
import sys
import random
import pygame


from network import Network
from settings import *
from button import Button
pygame.init()
pygame.font.init()





font1 = pygame.font.SysFont('dejavusans', 15)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 30)
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

pygame.display.set_caption('SPY')
mainClock = pygame.time.Clock()

mark_button = Button(screen_width-50,screen_height-690, question_mark_img)
start_button = Button(screen_width- 690,screen_height-690, start_img)
players_button = Button(50, 20, players_img)
timer_button = Button(50,100,timer_img)
begin_button = Button( screen_width/2 -begin_img.get_size()[0]/2,screen_width/2-begin_img.get_size()[1],begin_img)
spy_button = Button( screen_width // 3, screen_height // 2,spy_img)



class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
       # self.image = pygame.transform.scale(image, (10,10))
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):

        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 10)


    def collide(self):
        # get mouse position
        action = False
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
        # draw button

btns = [Button(  screen_width/2 -spy_img.get_size()[0]/2,  screen_width/2 -begin_img.get_size()[1]-200,spy_img),]

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font1.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font1.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

run = True
def main_menu():

    while run:
        pygame.draw.rect(screen, (255, 255, 255), mark_button, 10)
        screen.fill((0, 0, 0))
        mark_button.draw()
        start_button.draw()


        draw_text('Welcome To Spy', font2, (255, 255, 255), screen, screen_width // 3 ,screen_height // 2.5)
        screen.blit(spy_img, ( screen_width // 3 ,screen_height // 2))


        if mark_button.collide():
            rules()


        if start_button.collide():
            game_settings_menu()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def check(win, game, p):
    win.fill((0,0,0))


    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)

        move1 = game.p1_card
        move2 = game.p2_card
        print(game.p1_got_card,game.p2_got_card)


        text1 = font.render(str(move1), 1, (255, 0, 0))
        text2 = font.render(str(move2), 1, (255, 0, 0))




        if game.p1_got_card and p == 0:
            text1 = font.render(move1, 1, (0, 0, 0))


        if game.p2_got_card and p == 1:

            text2 = font.render(move2, 1, (255,0,0))


        if p == 1:
            win.blit(text2, (screen_width/2 - text2.get_width()/2, screen_height/2 - text2.get_height()/2))

        if p == 0:
            win.blit(text1, (screen_width/2 - text1.get_width()/2, screen_height/2 - text1.get_height()/2))


        for btn in btns:
            btn.draw()


    pygame.display.update()


def game_settings_menu():
    global player_count
    global timer_min
    running = True



    clock = pygame.time.Clock()

    done = False

    while running:
        screen.fill((0, 0, 0))





        players_button.draw()
        timer_button.draw()
        begin_button.draw()
        screen.blit(spy_img, (screen_width/2 - spy_img.get_size()[0]/2, screen_height/2 - spy_img.get_size()[0]/10))

        if players_button.collide():
            player_count += 1
        if timer_button.collide():
            timer_min += 1
        if begin_button.collide():

            start_game()

        draw_text(f'{player_count}', font2, (255, 255, 255), screen, screen_width - 50, 20)
        draw_text(f'{timer_min}', font2, (255, 255, 255), screen, screen_width - 50, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        pygame.display.update()
        mainClock.tick(60)


def start_game():
    global player_count
    global timer_min
    last = pygame.time.get_ticks()
    cooldown = 10000

    running = True
    screen.fill((0, 0, 0))
    p_num = 0

    n = Network()
    player = int(n.getP())
    print("You are player", player)
    spy_button.draw()

    draw_text('Enter Your Name', font3, (255, 255, 255), screen, screen_width // 2.4, screen_height // 6)
    input_box1 = InputBox(275, 170, 500, 32)
    input_boxes = [input_box1]
    spy_button.draw()




    while running:

        clock.tick(60)
        try:
            game = n.send("get")
        except:
            running = False
            print("Couldn't get game")
            break

        try:
             n.send("words")
        except:
            running = False
            print("Couldn't get words")
            break



        if game.bothWent():
            pygame.display.flip()
            pygame.time.delay(500)
            try:
                print("sending timer request")
                n.send("timer")

            except:
                run = False
                print("error sending timer request")
                break



        if game.timer:
            # now = pygame.time.get_ticks()
            # if now - last >= cooldown:
            pygame.time.delay(1000)
            game.timer_screen(player,n)




        # if game.pressed == True:
        #     voting_menu()

        #
        # if spy_button.collide() and game.connected():
        #     if player == 0:
        #         if not game.p1_got_card:
        #             n.send("player 1 got card")
        #         else:
        #             if not game.p2_got_card:
        #                 n.send("player 2 got card")



        for btn in btns:
            if btn.collide() and game.connected():
                print("pressed")
                if player == 0:
                    if not game.p1_got_card:
                        #random_string_to_screen(screen,game.word_array)
                        print("1 pressed")
                        n.send("player 1 got card")
                else:
                    if not game.p2_got_card:
                        #random_string_to_screen(screen,game.word_array)
                        print("2 pressed")
                        n.send("player 2 got card")






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            for box in input_boxes:
                player_names.append(box.handle_event(event))



        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        check(screen, game, player)
        pygame.display.update()
        mainClock.tick(60)





def random_string_to_screen(screen, pack):
    str = random.choice(pack)
    split = str.split()

    if len(split) == 1:
        draw_text(f"{str}", font2, (255, 255, 255), screen, screen_width // 2.1, screen_height // 2.5)
    elif len(split) == 3:
        draw_text(f"{split[0]} {split[0]} {split[2]} ", font2, (255, 255, 255), screen, screen_width // 2.5,
                  screen_height // 2.5)
    # draw_text(f"{split[0]} {split[1]}", font2, (255, 255, 255), screen, screen_width // 2.5, screen_height // 3)
    else:
        draw_text(f"{split[0]}", font2, (255, 255, 255), screen, screen_width // 2.3, screen_height // 3)
        draw_text(f"{split[1]}", font2, (255, 255, 255), screen, screen_width // 2.3, screen_height // 2.3)
    return str




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

    for _ in string.ascii_uppercase:
        intermediate.fill((0, 0, 0))
        intermediate.blit(qa_img, (screen_width // 3, screen_height - 700))

        y += 20



    scroll_y = 0


    running = True
    while running:


        draw_text('Rules', font1, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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