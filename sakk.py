import pygame as pg
from pygame.locals import *


#Piece classes
class Piece:
    def __init__(self, y, x, vilagos):
        self.x = x
        self.y = y
        self.vilagos = vilagos
    def lepes(self,y,x):
        if self.vilagos:
            self.y -= y
            self.x -= x
            tabla[self.y][self.x] = self
            tabla[self.y+y][self.x+x] = 0
        else:
            self.y +=y
            self.x += x
            tabla[self.y][self.x] = self
            tabla[self.y-y][self.x-x] = 0
    def __str__(self):
            return f"{self.x},{self.y},{self.vilagos}"
class Pawn(Piece):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
        self.kep = whitePawn if self.vilagos else blackPawn
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
            
        return lephet + self.hova_uthet()
    def hova_uthet(self):
        uthet = []
        if self.vilagos:
            if tabla[self.y - 1][self.x - 1] ==0 and tabla[self.y - 1][self.x + 1] == 0:
                return [] 
            elif tabla[self.y - 1][self.x - 1] !=0 and tabla[self.y - 1][self.x - 1].vilagos == False: 
                uthet.append((self.y - 1,self.x - 1))
                if tabla[self.y - 1][self.x + 1] !=0 and tabla[self.y - 1][self.x + 1].vilagos == False: 
                    uthet.append((self.y - 1,self.x + 1))
            elif tabla[self.y - 1][self.x + 1] !=0 and tabla[self.y - 1][self.x + 1].vilagos == False: 
                uthet.append((self.y - 1,self.x + 1))
                if tabla[self.y - 1][self.x - 1] !=0 and tabla[self.y - 1][self.x - 1].vilagos == False: 
                    uthet.append((self.y - 1,self.x - 1))
        else:
            if tabla[self.y + 1][self.x - 1] == 0 and tabla[self.y + 1][self.x + 1] == 0:
                return [] 
            elif tabla[self.y + 1][self.x - 1] !=0 and tabla[self.y + 1][self.x - 1].vilagos: 
                uthet.append((self.y + 1,self.x - 1))
                if tabla[self.y + 1][self.x + 1] !=0 and tabla[self.y + 1][self.x + 1].vilagos: 
                    uthet.append((self.y + 1,self.x + 1))
            elif tabla[self.y + 1][self.x + 1] !=0 and tabla[self.y + 1][self.x + 1].vilagos: 
                uthet.append((self.y + 1,self.x + 1))
                if tabla[self.y + 1][self.x - 1] !=0 and tabla[self.y + 1][self.x - 1].vilagos: 
                    uthet.append((self.y + 1,self.x - 1))
        return uthet
class Knight(Piece):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
        self.kep = whiteKnight if self.vilagos else blackKnight
    def hova_lephet(self):
        lepes = []
        #mezo = 0 ??
        for i in [(self.y-2,self.x-1),(self.y-2,self.x+1),(self.y+2,self.x-1),(self.y+2,self.x+1),(self.y-1,self.x+2),(self.y-1,self.x-2),(self.y+1,self.x+2),(self.y+1,self.x-2)]:
            if (0 <= i[0] <= 7) and (0 <= i[1] <= 7):
                mezo = tabla[i[0]][i[1]]
            else: mezo = 1
            if mezo == 0:
                lepes.append(i)
            elif mezo == 1: pass # i have no idea
            else: lepes.append(i) if self.vilagos != mezo.vilagos else None
        return lepes
class Bishop(Piece):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
        self.kep = whiteBishop if self.vilagos else blackBishop
    def hova_lephet(self):
        lepes = []
        sor = self.y-1
        oszlop = self.x-1
        while sor >= 0 and oszlop >= 0:
            if tabla[sor][oszlop] != 0:
                lepes.append((sor,oszlop)) if tabla[sor][oszlop].vilagos != self.vilagos else None
                break
            else: lepes.append((sor,oszlop))
            sor -= 1
            oszlop -= 1
        sor = self.y+1
        oszlop = self.x+1
        while sor < 8 and oszlop < 8:
            if tabla[sor][oszlop] != 0:
                lepes.append((sor,oszlop)) if tabla[sor][oszlop].vilagos != self.vilagos else None
                break
            else: lepes.append((sor,oszlop))
            sor += 1
            oszlop +=1
        oszlop = self.x + 1
        sor = self.y - 1
        while oszlop < 8 and sor >= 0:
            if tabla[sor][oszlop] != 0:
                lepes.append((sor,oszlop)) if tabla[sor][oszlop].vilagos != self.vilagos else None
                break
            else: lepes.append((sor,oszlop))
            oszlop += 1
            sor -= 1
        sor = self.y + 1
        oszlop = self.x - 1
        while oszlop >= 0 and sor < 8:
            if tabla[sor][oszlop] != 0:
                lepes.append((sor,oszlop)) if tabla[sor][oszlop].vilagos != self.vilagos else None
                break
            else: lepes.append((sor,oszlop))
            oszlop -= 1
            sor += 1
        return lepes
class Rook(Piece):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
        self.kep = whiteRook if self.vilagos else blackRook
    def hova_lephet(self):
        lepes = []
        sor = self.y-1
        while sor >= 0:
            if tabla[sor][self.x] != 0:
                lepes.append((sor,self.x)) if tabla[sor][self.x].vilagos != self.vilagos else None
                break
            else: lepes.append((sor,self.x))
            sor -= 1
        sor = self.y+1
        while sor < 8:
            if tabla[sor][self.x] != 0:
                lepes.append((sor,self.x)) if tabla[sor][self.x].vilagos != self.vilagos else None
                break
            else: lepes.append((sor,self.x))
            sor += 1
        oszlop = self.x+1
        while oszlop < 8:
            if tabla[self.y][oszlop] != 0:
                lepes.append((self.y,oszlop)) if tabla[self.y][oszlop].vilagos != self.vilagos else None
                break
            else: lepes.append((self.y,oszlop))
            oszlop += 1
        oszlop = self.x-1
        while oszlop >= 0:
            if tabla[self.y][oszlop] != 0:
                lepes.append((self.y,oszlop)) if tabla[self.y][oszlop].vilagos != self.vilagos else None
                break
            else: lepes.append((self.y,oszlop))
            oszlop -= 1
        return lepes
class Queen(Rook,Bishop):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
        self.kep = whiteQueen if self.vilagos else blackQueen
    def hova_lephet(self):
        lepes = Rook.hova_lephet(self) + Bishop.hova_lephet(self)
        return lepes
class King(Piece):
    def __init__(self, y, x, vilagos):
        super().__init__(y, x, vilagos)
        self.kep = whiteKing if self.vilagos else blackKing
    def hova_lephet(self):
        lepes = []
        #mezo = 0 ??
        for i in [(self.y,self.x-1),(self.y,self.x+1),(self.y+1,self.x-1),(self.y+1,self.x+1),(self.y-1,self.x+1),(self.y-1,self.x-1),(self.y+1,self.x),(self.y+-1,self.x)]:
            if (0 <= i[0] <= 7) and (0 <= i[1] <= 7):
                mezo = tabla[i[0]][i[1]]
            else: mezo = 1
            if mezo == 0:
                lepes.append(i)
            elif mezo == 1: pass # i have no idea
            else: lepes.append(i) if self.vilagos != mezo.vilagos else None
        return lepes
#iniatialize pygame & variables
pg.init()
screen_size = (720, 720)
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Bolond sakk 2.0 update")
cell_size = screen_size[0] // 8
tabla =[[0 for i in range(9)] for j in range(8)]
lehetoseg_pos = []
kijelolt = 0
status = 0 #0: fehér lép #1:fekete lép
timer = pg.time.Clock()
fps = 60

#load images
whitePawn = pg.transform.scale(pg.image.load('assets/images/fehergyalog.png'),(72,72))
whiteRook = pg.transform.scale(pg.image.load('assets/images/feherbastya.png'),(72,72))
whiteKnight = pg.transform.scale(pg.image.load('assets/images/feherhuszar.png'),(72,72))
whiteBishop = pg.transform.scale(pg.image.load('assets/images/feherfuto.png'),(72,72))
whiteQueen = pg.transform.scale(pg.image.load('assets/images/fehervezer.png'),(72,72))
whiteKing = pg.transform.scale(pg.image.load('assets/images/feherkiraly.png'),(72,72))
blackPawn = pg.transform.scale(pg.image.load('assets/images/feketegyalog.png'),(72,72))
blackRook = pg.transform.scale(pg.image.load('assets/images/feketebastya.png'),(72,72))
blackKnight = pg.transform.scale(pg.image.load('assets/images/feketehuszar.png'),(72,72))
blackBishop = pg.transform.scale(pg.image.load('assets/images/feketefuto.png'),(72,72))
blackQueen = pg.transform.scale(pg.image.load('assets/images/feketevezer.png'),(72,72))
blackKing = pg.transform.scale(pg.image.load('assets/images/feketekiraly.png'),(72,72))

#Initialize starting positions
for i in range(8):
    if i == 0 or i == 7:
        tabla[0][i] = Rook(0,i,False)
        tabla[7][i] = Rook(7,i,True)
    elif i == 1 or i == 6:
        tabla[0][i] = Knight(0,i,False)
        tabla[7][i] = Knight(7,i,True)
    elif i == 2 or i == 5:
        tabla[0][i] = Bishop(0,i,False)
        tabla[7][i] = Bishop(7,i,True)
    elif i == 4:
        tabla[0][i] = King(0,i,False)
        tabla[7][i] = King(7,i,True)
    else:
        tabla[0][i] = Queen(0,i,False)
        tabla[7][i] = Queen(7,i,True)
    tabla[6][i] = Pawn(6, i, True)
    tabla[1][i] = Pawn(1, i, False)
    
#draw the board based on screen size
def draw_board():
    for sor in range(8):
        for oszlop in range(4):
            if sor % 2 == 0:
                #vilagos negyzet majd offset sötét négyzet
                pg.draw.rect(screen, (251, 244, 238), pg.Rect(oszlop * 2 * cell_size, sor*cell_size, cell_size, cell_size))
                pg.draw.rect(screen, (80, 81, 104), pg.Rect(oszlop * 2 * cell_size + cell_size, sor*cell_size, cell_size, cell_size))
            else:
                pg.draw.rect(screen, (251, 244, 238), pg.Rect(cell_size + oszlop * 2 * cell_size, sor*cell_size, cell_size, cell_size))
                pg.draw.rect(screen, (80, 81, 104), pg.Rect(oszlop * 2 * cell_size, sor*cell_size, cell_size, cell_size))
        for i in range(9):
            pg.draw.line(screen,'black',(0,i*cell_size),(720,i*cell_size),2)
            pg.draw.line(screen,'black',(i*cell_size,0),(i*cell_size,720),2)

#draw pieces onto board
def draw_pieces():
    for i in range(8):
        for j in range(8):
            if type(tabla[i][j]) != int:
                screen.blit(tabla[i][j].kep,(j*cell_size+9,i*cell_size+9))

#draw possible moves onto board
def draw_lehetoseg(y, x):
    if 0 <= y < 8 and 0 <= x < 8:
        pg.draw.circle(screen,((155,70,255) if tabla[y][x] == 0 else (255,0,0)),(x*cell_size + cell_size//2,y*cell_size + cell_size //2), 15,3) #//2 a középre igazításhoz cellán belül


#Main game
running = True
while running:
    timer.tick(fps)
    screen.fill('dark grey')
    draw_board()
    draw_pieces()
    for y, x in lehetoseg_pos: draw_lehetoseg(y, x)
    #Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pos_x, pos_y = event.pos
            pos_x //= cell_size #kattintás poziciójából mátrix index
            pos_y //= cell_size
            if type(tabla[pos_y][pos_x]) != int and tabla[pos_y][pos_x].vilagos if status == 0 else type(tabla[pos_y][pos_x]) != int and tabla[pos_y][pos_x].vilagos == False:
                kijelolt = tabla[pos_y][pos_x] #objektum
                lehetoseg_pos = kijelolt.hova_lephet()
            else:
                if (pos_y, pos_x) in lehetoseg_pos:
                    if kijelolt.vilagos:
                            kijelolt.lepes(kijelolt.y - pos_y, kijelolt.x - pos_x)
                            lehetoseg_pos = []
                            status = 1
                    elif kijelolt.vilagos == False:
                            kijelolt.lepes(pos_y - kijelolt.y, pos_x - kijelolt.x)
                            lehetoseg_pos = []
                            status = 0
                else:
                    lehetoseg_pos = []
    pg.display.flip()
pg.quit()