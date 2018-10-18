
from utils import *

class Card(object):

    LD = 0      #   LU - U - RU
    D = 1       #   |         |
    RD = 2      #   |         |
    R = 3       #   L         R
    RU = 4      #   |         |
    U = 5       #   |         |
    LU = 6      #   LD - D - RD
    L = 7

    def __init__(self, n, player, number, color):
        self.number = number
        self.x=None
        self.y=None
        self.px = 0
        self.py = 0
        
        self.player = player
        self.color = color
        self.name = str(self.number) + str(self.player)[0]
        self.arrows = {0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False}
        self.LP = 20-2*n
        self.maxLP = self.LP
        self.isSelected = False
        numberArrows = 0
        while numberArrows != n:
            random = randint(0, 7)
            if not self.arrows[random]:
                numberArrows += 1
                self.arrows[random]=True

    def __repr__(self):
        return str(self.__dict__)

    def isClickedOn(self, x, y):
        return x >= self.px and x <= self.px+cardwidth and y >= self.py and y <= self.py+cardheight

    def changePlayer(self, player, color):
        self.player = player
        self.color = color

    def reborn(self):
        self.LP = (self.maxLP)/2

    def set_positions(self):
        if self.player == 0:
            self.px = hand_p1_px + card_intern_interval
            self.py = hand_p1_py + card_intern_interval + (self.number-1)*(cardheight+card_extern_interval)
        elif self.player == 1:
            self.px = hand_p2_px + card_intern_interval
            self.py = hand_p2_py + card_intern_interval + (self.number-1)*(cardheight+card_extern_interval)

    def getName(self):
        return self.name+"("+str(self.LP).zfill(2)+"/"+str(self.maxLP).zfill(2)+self.player

    def draw(self,fenetre):
        pygame.draw.rect(fenetre, self.color, pygame.Rect(self.px, self.py, cardwidth, cardheight))
        for number in self.arrows.keys():
            if (self.arrows[number]):
                   self.drawArrow(fenetre,number)
        label = pygame.font.SysFont("monospace", 30).render(str(self.LP), 10, white)
        fenetre.blit(label, (self.px+cardwidth/2-10, self.py+cardheight/2-10))
        if self.isSelected:
            pygame.draw.rect(fenetre, red, pygame.Rect(self.px, self.py, cardwidth, cardheight), border)

    def draw_hidden(self,fenetre):
        pygame.draw.rect(fenetre, self.color, pygame.Rect(self.px, self.py, cardwidth, cardheight))

    def drawArrow(self,fenetre,number):
        if(number == 0):
            X = self.px + arrow_boarding
            Y = self.py + arrow_boarding
            pygame.draw.polygon(fenetre, white, [[X, Y], [X+arrow_size, Y], [X, Y+arrow_size]], 0)
        if(number == 1):
            X = self.px + cardwidth/2
            Y = self.py + arrow_boarding
            pygame.draw.polygon(fenetre, white, [[X, Y], [X+r2_arrow_size, Y+r2_arrow_size], [X-r2_arrow_size, Y+r2_arrow_size]], 0)
        if(number == 2):
            X = self.px + cardwidth - arrow_boarding
            Y = self.py + arrow_boarding
            pygame.draw.polygon(fenetre, white, [[X, Y], [X-arrow_size, Y], [X, Y+arrow_size]], 0)
        if(number == 3):
            X = self.px+cardwidth - arrow_boarding
            Y = self.py+cardheight/2
            pygame.draw.polygon(fenetre, white, [[X, Y], [X-r2_arrow_size, Y+r2_arrow_size], [X-r2_arrow_size, Y-r2_arrow_size]], 0)
        if(number == 4):
            X = self.px + cardwidth - arrow_boarding
            Y = self.py+cardheight - arrow_boarding
            pygame.draw.polygon(fenetre, white, [[X, Y], [X-arrow_size, Y], [X, Y-arrow_size]], 0)
        if(number == 5):
            X = self.px+cardwidth/2
            Y = self.py+cardheight - arrow_boarding
            pygame.draw.polygon(fenetre, white, [[X, Y], [X+r2_arrow_size, Y-r2_arrow_size], [X-r2_arrow_size, Y-r2_arrow_size]], 0)
        if(number == 6):
            X = self.px + arrow_boarding
            Y = self.py+cardheight - arrow_boarding
            pygame.draw.polygon(fenetre, white, [[X, Y], [X+arrow_size, Y], [X, Y-arrow_size]], 0)
        if(number == 7):
            X = self.px + arrow_boarding
            Y = self.py + cardheight/2
            pygame.draw.polygon(fenetre, white, [[X, Y], [X+r2_arrow_size, Y+r2_arrow_size], [X+r2_arrow_size, Y-r2_arrow_size]], 0)


def build_card_from_json(json_data):

    card = Card(0, json_data['player'], json_data['number'], json_data['color'])
    for key, value in json_data['arrows'].items():
        card.arrows[key] = value
    card.name = json_data['name']
    card.color = json_data['color']
    card.isSelected = json_data['isSelected']
    card.number = json_data['number']
    card.LP = json_data['LP']
    card.maxLP = json_data['maxLP']
    return card


if __name__ == '__main__':
    build_card_from_json(eval("{'maxLP': 12, 'name': '21', 'isSelected': False, 'color': (255, 0, 0), 'px': 528, 'py': 248, 'arrows': {0: True, 1: False, 2: False, 3: True, 4: True, 5: False, 6: True, 7: False}, 'number': 2, 'player': 1, 'LP': 12, 'y': 1, 'x': 3}"))