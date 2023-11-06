# sakkpy
Egyszerű sakk pythonban, alapja a pygame library.
A bábuk a **Piece** osztály alosztályai, közös tulajdonságuk az **x** és **y** pozíció, valamint a **világos** igaz/hamis változó. Ezenfelül a *Piece* osztály tartalmaz egy **lepes** függvényt is.
A konkrét bábuosztályok tartalmazzák a bábura vonatkozó **képet** és a bábu saját **hova_lephet** függvényét.
A **hova_lephet** függvény valid pozíciókat (*tuple formában*) ad vissza ahová a kattintással kiválasztott bábu léphet, ezeket a **draw_lehetoseg** függvény rajzolja a táblára.
