import pygame as pg
import sys
from pygame.locals import *
#Az első stabil verzió amit én csináltam
class Piece:
    def __init__(self, y, x, vilagos):
        self.x = x
        self.y = y
        self.vilagos = vilagos
    def __str__(self):
            return f"{self.x},{self.y},{self.vilagos}"
class Pawn(Piece):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
    def hova_lephet(self):
        lephet = []
        if self.vilagos:
            if tabla[self.y -1][self.x] != 0:
                return []
            
            if self.y == 6 and tabla[self.y - 2][self.x] == 0:
                lephet.append((self.y - 2, self.x))

            if tabla[self.y - 1][self.x] == 0:
                lephet.append((self.y - 1, self.x))

        else:
            if tabla[self.y +1][self.x] != 0:
                return []
            
            if self.y == 1 and tabla[self.y + 2][self.x] == 0:
                lephet.append((self.y + 2,self.x))

            if tabla[self.y + 1][self.x] == 0:
                lephet.append((self.y + 1,self.x))
            
        return lephet
    def hova_uthet(self):
        uthet = []
        if self.vilagos:
            if tabla[self.y -1][self.x-1] != 0:
                return []
            
            if self.y == 6 and tabla[self.y - 2][self.x] == 0:
                uthet.append((self.y - 2, self.x))

            if tabla[self.y - 1][self.x] == 0:
                uthet.append((self.y - 1, self.x))

        else:
            if tabla[self.y +1][self.x] != 0:
                return []
            
            if self.y == 1 and tabla[self.y + 2][self.x] == 0:
                uthet.append((self.y + 2,self.x))

            if tabla[self.y + 1][self.x] == 0:
                uthet.append((self.y + 1,self.x))
            
        return uthet 
    def lepes(self, hany):
        if self.vilagos:
            self.y -= hany
            tabla[self.y][self.x] = self
            tabla[self.y+hany][self.x] = 0
        else: 
            self.y +=hany
            tabla[self.y][self.x] = self
            tabla[self.y-hany][self.x] = 0


pg.init()
screen_size = (720, 720)
screen = pg.display.set_mode(screen_size)
cell_size = screen_size[0] // 8
tabla =[[0 for i in range(8)] for j in range(8)]
def draw_board():
    for i in range(8):
        for j in range(4):
            if i % 2 == 0:
                pg.draw.rect(screen, (251, 244, 238), pg.Rect(j * 2 * cell_size, i*cell_size, cell_size, cell_size))
                pg.draw.rect(screen, (80, 81, 104), pg.Rect(j * 2 * cell_size + cell_size, i*cell_size, cell_size, cell_size))
            else:
                pg.draw.rect(screen, (251, 244, 238), pg.Rect(cell_size + j * 2 * cell_size, i*cell_size, cell_size, cell_size))
                pg.draw.rect(screen, (80, 81, 104), pg.Rect(j * 2 * cell_size, i*cell_size, cell_size, cell_size))
def draw_pieces():
    for i in range(8):
        for j in range(8):
            if type(tabla[i][j]) == Pawn:
                pg.draw.circle(screen,(170,180,255),(j * cell_size + cell_size//2,i*cell_size + cell_size //2), 30) if tabla[i][j].vilagos == True else pg.draw.circle(screen,(170,90,155),(j * cell_size + cell_size//2,i*cell_size + cell_size //2), 30)

def draw_lehetoseg(y, x):
    pg.draw.circle(screen,(155,70,255),(x*cell_size + cell_size//2,y*cell_size + cell_size //2), 10) #//2 a középre igazításhoz cellán belül

lehetoseg_pos = []
kijelolt = 0
tabla[6] = [Pawn(6, i, True) for i in range(8)]
tabla[1] = [Pawn(1, i, False) for i in range(8)]
running = True
while running:
    #EVENT LOOP
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pos_x, pos_y = event.pos
            pos_x //= cell_size #kattintás poziciójából mátrix index
            pos_y //= cell_size
            if type(tabla[pos_y][pos_x]) == Pawn:
                kijelolt = tabla[pos_y][pos_x]
                print(kijelolt.vilagos)
                lehetoseg_pos = kijelolt.hova_lephet()
                print(lehetoseg_pos)
                
            else:
                if (pos_y, pos_x) in lehetoseg_pos:
                    kijelolt.lepes(kijelolt.y - pos_y if kijelolt.vilagos else pos_y - kijelolt.y)
                    lehetoseg_pos = []
                else:
                    lehetoseg_pos = []
    draw_board()
    draw_pieces()
    for y, x in lehetoseg_pos:
        draw_lehetoseg(y, x)
    pg.display.update()

pg.quit()