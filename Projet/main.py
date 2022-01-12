from kandinsky import *
from time import *
from ion import *
from random import *

x = 30
y = 30
mx = 50
my = 50
fx = 0
fy = 0
s = 10
nnn = True
removenum = 2
size = 3
g1 = []
g2 = []
score = 0
sleeptime = 0
startsleep = 0.004
rangeofi = 20

def StartingMenu():
    fill_rect(0, 0, 320
              , 256, color(0, 0, 0))
    draw_string("Feed Me Fast V2", 100, 0, color(0,127,63), color(0,0,0))
    draw_string("Made by Farmeurimmo", 80, 30, color(0,127,63), color(0,0,0))
    draw_string("   Jouer   ", 110, 60, color(127, 0, 0), color(0, 0, 0))
    draw_string("   Crédits   ", 110, 90, color(127, 0, 0), color(0, 0, 0))
    pos=0
    surl=80
    surz=80
    sleep(0.3)
    while True:
        surl+=30
        surz+=30
        if keydown(KEY_DOWN):
            pos+=1
            if (pos == 2):
                pos = 0
            draw_string("   Jouer   ", 110, 60, color(255, 0, 0), color(0, 0, 0))
            draw_string("   Crédits   ", 110, 90, color(127, 0, 0), color(0, 0, 0))
        if keydown(KEY_UP):
            pos-=1
            if (pos == -1):
                pos = 1
            draw_string("   Jouer   ", 110, 60, color(255, 0, 0), color(0, 0, 0))
            draw_string("   Crédits   ", 110, 90, color(127, 0, 0), color(0, 0, 0))
        if pos == 0:
            draw_string(">> Jouer <<", 110, 60, color(surl, 255, surz), color(0, 0, 0))
        elif pos == 1:
            draw_string(">> Crédits << ", 110, 90, color(surl, 255, surz), color(0, 0, 0))
        if surl >= 240:
            surl=80
            surz=90
        if keydown(KEY_EXE) or keydown(KEY_OK):
            if pos == 1:
                continue
            break
        sleep(0.1)

StartingMenu()

def spawnPlayer():
    fill_rect(x - 2, y - 2, size * 10
              , size * 10,
              color(0
                    , 153, 204))
    fill_rect(x, y, size * 8
              , size * 8, color(80, 45, 50))


def spawnFood(x, y):
    sleep(0.03)
    fill_rect(x, y, size * 6
              , size * 6, color(255, 255, 0))


def clearFood(x, y):
    fill_rect(x - 20, y - 20, size * 25
              , size * 25,
              color(0
                    , 153, 204))


def Randnumn():
    g1.clear()
    g2.clear()
    mx = randrange(3, 30) * 10
    my = randrange(1, 20) * 10
    spawnFood(mx, my)
    nnn = True
    d = 0
    for i in range(rangeofi):
        g1.append(mx - d)
        d += 1
    d = 0
    for i in range(rangeofi):
        g1.append(mx + d)
        d += 1
    d = 0
    for i in range(rangeofi):
        g2.append(my - d)
        d += 1
    d = 0
    for i in range(rangeofi):
        g2.append(my + d)
        d += 1
    d = 0
    fill_rect(mx, my, size * 3
              , size * 3, color(255, 255, 0))


fill_rect(0, 0, 320, 222, color(255, 255, 255))
fill_rect(20, 100, 280, 10, color(0, 0, 0))
draw_string("Feed Me Fast V2", 100, 0)
draw_string("Made by Farmeurimmo", 80, 30)
for i in range(280):
    fill_rect(20, 100, i, 10, color(90, 180, 68))
    fill_rect(0, 0, 10, 100, color(255, 255, 255))
    sleep(startsleep)
    if i == 0:
        draw_string("Chargement en cours", 50, 120)
    if i == 30:
        draw_string("Chargement en cours.", 50, 120)
    if i == 60:
        draw_string("Chargement en cours..", 50, 120)
    if i == 90:
        draw_string("Chargement en cours...", 50, 120)
    if i == 130:
        draw_string("Lancement en cours    ", 50, 120)
    if i == 170:
        draw_string("Lancement en cours.    ", 50, 120)
    if i == 210:
        draw_string("Lancement en cours..     ", 50, 120)
    if i == 250:
        draw_string("Lancement en cours...     ", 50, 120)

fill_rect(0, 0, 322, 222, color(0, 153, 204))
spawnPlayer()
Randnumn()
while True:
    s = s + 1
    ox = x
    oy = y
    if keydown(KEY_UP):
        if y - removenum >= 0:
            y = y - removenum

    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y

    if keydown(KEY_DOWN):
        if y + removenum >= 0:
            if y + removenum <= 208:
                y = y + removenum

    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y

    if keydown(KEY_RIGHT):
        if x + removenum >= 0:
            if x + removenum <= 304:
                x = x + removenum

    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y

    if keydown(KEY_LEFT):
        if x - removenum >= 0:
            x = x - removenum

    if ox != x and oy != y or ox != x or oy != y:
        spawnPlayer()
    ox = x
    oy = y

    draw_string(str(score),
                0, 0)
    if x in g1 and y in g2:
        if nnn == True:
            fx = x
            fy = y
            clearFood(fx, fy)
            spawnPlayer()
            if s <= 150:
                score += 10
            else:
                score += 5
            s = 10
            Randnumn()
            nnn = True