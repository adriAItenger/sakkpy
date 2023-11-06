# Python sakk
Egyszerű sakk pythonban, alapja a pygame library.
## A kód struktúrája
A kód több osztályból és funkcióból áll:
Piece: Ez az osztály képviseli a sakkbábukat. Minden bábuhoz tartozik egy pozíció (y, x) és egy szín (világos vagy sötét).
Pawn, Rook, Knight, Bishop, Queen, King: Ezek az osztályok a Piece osztályból származnak, és képviselik a különböző sakkbábukat. Minden osztályhoz tartoznak saját mozgási szabályok.
draw_board(): Ez a funkció rajzolja meg a sakktáblát.
draw_pieces(): Ez a funkció rajzolja meg a bábukat a táblán.
draw_lehetoseg(y, x): Ez a funkció kiemeli a lehetséges lépéseket a megadott bábu számára.
```
def draw_board():
    for sor in range(8):
        for oszlop in range(4):
            if sor % 2 == 0:
                # világos négyzet majd offset sötét négyzet
                pg.draw.rect(screen, (251, 244, 238), pg.Rect(oszlop * 2 * cell_size, sor*cell_size, cell_size, cell_size))
                pg.draw.rect(screen, (80, 81, 104), pg.Rect(oszlop * 2 * cell_size + cell_size, sor*cell_size, cell_size, cell_size))
            else:
                pg.draw.rect(screen, (251, 244, 238), pg.Rect(cell_size + oszlop * 2 * cell_size, sor*cell_size, cell_size, cell_size))
                pg.draw.rect(screen, (80, 81, 104), pg.Rect(oszlop * 2 * cell_size, sor*cell_size, cell_size, cell_size))
        for i in range(9):
            pg.draw.line(screen,'black',(0,i*cell_size),(720,i*cell_size),2)
            pg.draw.line(screen,'black',(i*cell_size,0),(i*cell_size,720),2)
```
