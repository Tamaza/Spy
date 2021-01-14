import pygame
#screen res
screen_width = 700
screen_height = 700
intermediate = pygame.surface.Surface((700, 1000))
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
#colors

white = (255, 255, 255)
blue = (0, 0, 255)


spy_img = pygame.image.load('img/spy.png')
spy_img = pygame.transform.scale(spy_img, (250,250))
qa_img = pygame.image.load('img/qa.png')
qa_img = pygame.transform.scale(qa_img, (250,250))
question_mark_img = pygame.image.load('img/question.png')
start_img = pygame.image.load('img/start.png')
