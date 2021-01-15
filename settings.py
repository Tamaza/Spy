import pygame
#screen res
screen_width = 700
screen_height = 700
intermediate = pygame.surface.Surface((700, 1000))
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
#colors
clock = pygame.time.Clock()

white = (255, 255, 255)
blue = (0, 0, 255)

basic_pack = ["Airpot","Bar","Cafe","Cinema","Circus","Concert Hall","Construction Site",
              "Forest","Gallery","Garage","Hospital","Office","Park","Parking",
              "Airplane","Pool","Ship","Sports Ground","Theatre","Sea"]

spy_img = pygame.image.load('img/spy.png')
spy_img = pygame.transform.scale(spy_img, (250,250))

iknow_img = pygame.image.load('img/iknow_img.png')
iknow_img = pygame.transform.scale(iknow_img, (200,200))

qa_img = pygame.image.load('img/qa.png')
qa_img = pygame.transform.scale(qa_img, (250,250))

players_img = pygame.image.load('img/players.png')
timer_img = pygame.image.load('img/thaimer.png')
begin_img = pygame.image.load('img/begin.png')


question_mark_img = pygame.image.load('img/question.png')
start_img = pygame.image.load('img/start.png')

player_count = 3
timer_min = 3
timer_sec = 60 * timer_min