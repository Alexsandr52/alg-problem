#Подключение нужных модулей
import pygame
from random import randint
pygame.init()


#создание окна игры
clock = pygame.time.Clock()
back = (255, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)


#цвета
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)


class TextArea():
   def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
       """ область: прямоугольник в нужном месте и нужного цвета """
       #запоминаем прямоугольник:
       self.rect = pygame.Rect(x, y, width, height)
       #цвет заливки - или переданный параметр, или общий цвет фона
       self.fill_color = color


   #установить текст
   def set_text(self, text, fsize=12, text_color=BLACK):
       self.text = text
       self.image = pygame.font.Font(None, fsize).render(text, True, text_color)
      
   #отрисовка прямоугольника с текстом
   def draw(self, shift_x=0, shift_y=0):
       pygame.draw.rect(mw, self.fill_color, self.rect)
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))   


#создание карточек
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
quest_card.set_text("Вопрос", 75)


ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.set_text("Ответ", 75)
while 1:
   quest_card.draw(10,10)
   ans_card.draw(10,10)
  
   pygame.display.update()
   clock.tick(40)  
