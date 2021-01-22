import random
from settings import *
import pygame

import sys
from button import Button



COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
player_count = 2
basic_pack = ["Airpot","Bar","Cafe","Cinema","Circus","Concert Hall","Construction Site",
              "Forest","Gallery","Garage","Hospital","Office","Park","Parking",
              "Airplane","Pool","Ship","Sports Ground","Theatre","Sea"]


iknow_button = Button( screen_width // 2.7, screen_height // 9,iknow_img)


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





class Game:
    def __init__(self, id):
        self.p1_got_card = False
        self.p2_got_card= False
        self.ready = False
        self.moves = [None, None]
        self.id = id
        self.timer = False
        self.word_array = ["You are SPY!"]
        self.word = random.choice(basic_pack)
        self.pressed = False


        for _ in range(0, player_count - 1):
            self.word_array.append(self.word)

        self.spy = ""
        self.p1_card = ""
        self.p2_card = ""


    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def random_string_to_screen(self,screen, pack):
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

    def play(self, player):


        if player == 0:
            #screen.blit(self.p1_card, (400, 350))
            pygame.display.flip()

            self.p1_got_card = True
        else:
            #screen.blit(self.p2_card, (100, 350))
            self.p2_got_card = True
            pygame.display.flip()
        pygame.display.flip()

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1_got_card and self.p2_got_card

    def voting_menu(self):
        global player_count
        global timer_min
        global timer_sec

        running = True
        screen.fill((0, 0, 0))
        start_ticks = pygame.time.get_ticks()  #
        counter, text = 100, f'10'.rjust(5)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        input_box1 = InputBox(250, 300, 500, 32)
        input_boxes = [input_box1]

        while running:

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 10 else 'Complete!'
                    # iknow_button.draw()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                for box in input_boxes:
                    box.handle_event(event)



            else:
                screen.fill((0, 0, 0))
                draw_text("Enter Spy's name", font3, (255, 255, 255), screen, screen_width - 435, screen_height - 425)
                screen.blit(font2.render(text, True, (255, 255, 255, 255)), (270, 200))
                for box in input_boxes:
                    box.update()

                for box in input_boxes:
                    box.draw(screen)

                pygame.display.flip()
                clock.tick(60)
                continue
            pygame.display.update()
            mainClock.tick(60)

    def timer_screen(self,player,n):

        global player_count
        global timer_min
        global timer_sec
        running = True
        screen.fill((0, 0, 0))
        start_ticks = pygame.time.get_ticks()  #
        counter, text = timer_sec, f'{str(timer_sec)}'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        while running:

            try:
                game = n.send("get")
            except:
                running = False
                print("Couldn't get game")
                break

            if iknow_button.collide() and self.connected():
                n.send("vote")





            if game.pressed:
                self.voting_menu()
                print(self.pressed, "salamuukk")

            print(self.pressed,"salam")

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    timer_sec -= 1
                    text = str(timer_sec).rjust(3) if timer_sec > 0 else 'SPY Won'
                    iknow_button.draw()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            else:
                screen.fill((0, 0, 0))
                screen.blit(font2.render(text, True, (255, 255, 255, 255)), (300, 250))
                iknow_button.draw()

                pygame.display.flip()
                clock.tick(60)
                continue
            pygame.display.update()
            mainClock.tick(60)






